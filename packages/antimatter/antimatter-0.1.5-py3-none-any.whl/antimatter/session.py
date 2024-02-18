import json
import os
from dataclasses import dataclass
from typing import Any, List, Optional, Union

import antimatter_engine as am
from antimatter.filetype.extract import extract_from_file
from antimatter.filetype.infer import infer_filetype

import antimatter.client as openapi_client
import antimatter.handlers as handlers
from antimatter.cap_prep.prep import Preparer
from antimatter.tags import ColumnTag, SpanTag
from antimatter.capsule import Capsule, CapsuleBindings
from antimatter.client import ApiClient, Configuration, DefaultApi
from antimatter.datatype.datatypes import Datatype
from antimatter.datatype.infer import infer_datatype
from antimatter.errors import errors
from antimatter.extra_helper import extra_for_session
from antimatter.session_mixins import *


@dataclass
class EncapsulateResponse:
    """
    EncapsulateResponse contains metadata from encapsulating data, including
    the capsule ID or IDs, and the raw bytes if the capsule was not exported.
    """
    capsule_ids: List[str]
    raw: Optional[bytes]


def new_domain(email: str):
    """
    This is temporary
    """
    host = os.getenv("ANTIMATTER_API_URL", "https://api.antimatter.io/v1")
    client = DefaultApi(
        api_client=ApiClient(
            configuration=Configuration(
                host=host
            )
        )
    )
    dm = client.domain_add_new(openapi_client.NewDomain(admin_email=email))
    return Session(domain=dm.id, api_key=dm.api_key)


class Session(
    CapabilityMixin, CapsuleMixin, DomainMixin, EncryptionMixin,
    FactMixin, GeneralMixin, IdentityProviderMixin, PolicyRuleMixin,
    ReadContextMixin, WriteContextMixin,
):
    """
    The Session establishes auth and the domain you are working with, providing
    both a standard instantiation or a context manager in which a Capsule and
    its underlying data can be interacted with.
    """

    def __init__(self, domain: str, api_key: str):
        self._domain = domain
        self._api_key = api_key
        os.environ['ANTIMATTER_API_KEY'] = api_key
        host = os.environ.get("ANTIMATTER_API_URL")
        self._session = am.PySession(domain)

        self._client = DefaultApi(
            api_client=ApiClient(
                configuration=Configuration(
                    host=host, access_token=self._api_key
                )
            )
        )
        super().__init__(domain=domain, api_key=api_key, client=self._client, session=self._session)

    @property
    def domain_id(self):
        """
        Return the current domain ID
        """
        return self._domain

    @property
    def api_key(self):
        """
        Return the api key in use by this session
        """
        return self._api_key

    def __enter__(self):
        # TODO: handle any resources/auth; call python rust wrapper to create a rust session
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: close any resources/auth; call python rust wrapper to close the rust session
        return

    def load_capsule(
        self,
        path: Optional[str] = None,
        data: Optional[Union[bytes, EncapsulateResponse]] = None,
        read_context: str = None,
    ) -> Optional[Capsule]:
        """
        load_capsule creates a capsule, extracting data from an Antimatter
        Capsule binary blob, either provided in raw bytes or as a string path
        to a local or remote file.

        If the `as_datatype` parameter is supplied and the data is a binary blob
        Antimatter Capsule, the data will be extracted in that format. If the
        data is data for saving to an Antimatter Capsule, `as_datatype` will
        specify the default format for the data when loaded from the blob.

        :param path: The location of the Capsule as a local or remote path.
        :param data: The data to load into an Antimatter Capsule.
        :param read_context: The name of the role policy to use for reading data
        """
        if not read_context:
            raise errors.CapsuleLoadError("specify a 'read_context' when loading a capsule")

        if not path and not data:
            raise errors.CapsuleLoadError("specify a 'path' or the raw 'data' when loading a capsule")

        if data and isinstance(data, EncapsulateResponse):
            data = data.raw

        (capsule_session, failed_capsules) = self._session.open_capsule(path, data, read_context)

        try:
            cap = CapsuleBindings(capsule_session, failed_capsules)

            capsule = Capsule(capsule_binding=cap)
            return capsule

        except RuntimeError as e:
            raise errors.CapsuleLoadError("loading data from capsule") from e

    def encapsulate(
        self,
        data: Any = None,
        write_context: str = None,
        span_tags: List[SpanTag] = None,
        column_tags: List[ColumnTag] = None,
        as_datatype: Union[Datatype, str] = Datatype.Unknown,
        skip_classify_on_column_names: List[str] = None,
        path: Optional[str] = None,
        subdomains_from: Optional[str] = None,
        create_subdomains: Optional[bool] = False,
        data_file_path: Optional[str] = None,
        data_file_hint: Optional[str] = None,
        **kwargs,
    ) -> EncapsulateResponse:
        """
        Saves the provided Capsule's data, or the provided data using the provided
        write context. If 'as_datatype' is provided, the default datatype for the
        raw data will use the specified type.

        One of 'capsule', 'data' or 'data_file_path' must be provided. If and only
        if a read context is supplied, the capsule will be returned unsealed.

        :param data: Raw data in a Capsule-supported format
        :param write_context: The name of the role policy to use for writing data
        :param span_tags: The span tags to manually apply to the data
        :param column_tags: Tags to apply to entire columns by name
        :param as_datatype:
        The datatype to override the provided data with when the capsule is read
        :param skip_classify_on_column_names: List of columns to skip classifying
        :param path: If provided, the local or remote path to save the capsule to
        :param subdomains_from: column in the raw data that represents the subdomain
        :param create_subdomains: allow missing subdomains to be created
        :param data_file_path:
        Optional path to a file containing data to be read. If provided, data from
        this file will be used instead of the 'data' parameter.
        :param data_file_hint:
        Optional hint indicating the format of the data in the file specified by
        'data_file_hint'. Supported formats include 'json', 'csv', 'txt', 'parquet'.
        If not specified, data will be read as plain text.
        :return: The response containing capsule metadata and the raw blob of the
        capsule if no path was provided.
        """
        as_datatype = Datatype(as_datatype)
        if column_tags is None:
            column_tags = []
        if span_tags is None:
            span_tags = []
        if skip_classify_on_column_names is None:
            skip_classify_on_column_names = []

        if not write_context:
            raise errors.CapsuleSaveError("specify a 'write_context' when creating a capsule")

        if data_file_path:
            if not data_file_hint:
                data_file_hint = infer_filetype(data_file_path)
                if not data_file_hint:
                    raise errors.CapsuleDataInferenceError(
                        "unable to infer data file type, provide 'data_file_hint' argument")
            data = extract_from_file(data_file_path, data_file_hint)

        dt = infer_datatype(data)
        if dt is Datatype.Unknown:
            if as_datatype is Datatype.Unknown:
                raise errors.CapsuleDataInferenceError("unable to infer type of data, provide 'as_datatype' argument")
            dt = as_datatype

        h = handlers.factory(dt)
        col_names, raw, extra = h.to_generic(data)
        extra = extra_for_session(dt, {**extra, **kwargs})
        jextra = json.dumps(extra)

        # if a cell path is not specified, assume it means the first cell
        for idx, st in enumerate(span_tags):
            if not st.cell_path:
                span_tags[idx].cell_path = f"{col_names[0]}[0]"

        raw, capsule_ids = self._session.encapsulate(
            *Preparer.prepare(col_names, column_tags, skip_classify_on_column_names, raw, span_tags, extra),
            write_context,
            path,
            [],
            jextra,
            subdomains_from,
            create_subdomains)
        if raw is not None:
            raw = bytes(raw)
        return EncapsulateResponse(capsule_ids=capsule_ids, raw=raw)

    def refresh_token(self):
        return self._client.domain_authenticate(
            self._domain,
            domain_authenticate=openapi_client.DomainAuthenticate(token=self._api_key)).token

    def with_new_peer_domain(
        self,
        import_alias_for_child: str,
        display_name_for_child: str,
        nicknames: Optional[List[str]] = None,
        import_alias_for_parent: Optional[str] = None,
        display_name_for_parent: Optional[str] = None,
        link_all: bool = True,
        link_identity_providers: bool = None,
        link_facts: bool = None,
        link_read_contexts: bool = None,
        link_write_contexts: bool = None,
        link_capabilities: bool = None,
        link_domain_policy: bool = None,
        link_capsule_access_log: bool = None,
        link_control_log: bool = None,
        link_capsule_manifest: bool = None,
    ) -> "Session":
        """
        Creates a new peer domain, returning the authenticated session for that
        new domain.
        """
        dm = self.new_peer_domain(
            import_alias_for_child=import_alias_for_child,
            display_name_for_child=display_name_for_child,
            nicknames=nicknames,
            import_alias_for_parent=import_alias_for_parent,
            display_name_for_parent=display_name_for_parent,
            link_all=link_all,
            link_identity_providers=link_identity_providers,
            link_facts=link_facts,
            link_read_contexts=link_read_contexts,
            link_write_contexts=link_write_contexts,
            link_capabilities=link_capabilities,
            link_domain_policy=link_domain_policy,
            link_capsule_access_log=link_capsule_access_log,
            link_control_log=link_control_log,
            link_capsule_manifest=link_capsule_manifest,
        )
        return Session(dm.get("id"), dm.get("api_key"))
