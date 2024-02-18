from antimatter.client import DefaultApi
from antimatter.session_mixins.token import exec_with_token


class EncryptionMixin:
    """
    Session mixin defining CRUD functionality for encryption functionality.
    """

    def __init__(self, domain: str, client: DefaultApi, **kwargs):
        try:
            super().__init__(domain=domain, client=client, **kwargs)
        except TypeError:
            super().__init__()  # If this is last mixin, super() will be object()
        self._domain = domain
        self._client = client

    @exec_with_token
    def flush_encryption_keys(self):
        """
        Flush all keys in memory. The keys will be immediately reloaded from persistent
        storage, forcing a check that the domain's root key is still available
        """
        self._client.domain_flush_encryption_keys(domain_id=self._domain)
