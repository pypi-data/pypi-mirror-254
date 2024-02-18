from enum import Enum
from typing import Union

import antimatter.client as openapi_client


class WriteContextHookMode(str, Enum):
    """
    Class representing the mode of the WriteContextHook.
    """
    Sync = "sync"
    Async = "async"


class WriteContextBuilder:
    """
    Builder class for creating WriteContext objects.
    """
    def __init__(self) -> None:
        """
        Initialize a new instance of WriteContextBuilder.
        """
        self.write_context = openapi_client.AddWriteContext(
            summary="",
            description="",
            config=openapi_client.WriteContextConfigInfo(
                requiredHooks=[],
            )
        )

    def set_summary(self, summary: str) -> 'WriteContextBuilder':
        """
        Set the summary of the WriteContext.

        :param summary: The summary to set.
        :return: The WriteContextBuilder instance.
        """
        self.write_context.summary = summary
        return self
    
    def set_description(self, description: str) -> 'WriteContextBuilder':
        """
        Set the description of the WriteContext.

        :param description: The description to set.
        :return: The WriteContextBuilder instance.
        """
        self.write_context.description = description
        return self
    
    def add_hook(self, name: str, constraint: str, mode: Union[WriteContextHookMode, str]) -> 'WriteContextBuilder':
        """
        Add a hook to the WriteContext.

        :param name: The name of the hook.
        :param constraint: The constraint of the hook.
        :param mode: The mode of the hook.
        :return: The WriteContextBuilder instance.
        """
        self.write_context.config.required_hooks.append(openapi_client.WriteContextConfigInfoRequiredHooksInner(
            hook=name,
            constraint=constraint,
            mode=WriteContextHookMode(mode).value,
        ))
        return self
    
    def build(self) -> openapi_client.AddWriteContext:
        """
        Build the WriteContext.

        :return: The built WriteContext.
        """
        return self.write_context


class WriteContextConfigurationBuilder:
    """
    Builder class for creating WriteContextConfigInfo objects.
    """

    def __init__(self) -> None:
        """
        Initialize a new instance of WriteContextConfigurationBuilder.
        """
        self._write_context_config = openapi_client.WriteContextConfigInfo(requiredHooks=[])

    def add_hook(
        self, name: str, constraint: str, mode: Union[WriteContextHookMode, str],
    ) -> 'WriteContextConfigurationBuilder':
        """
        Add a hook to the WriteContextConfigurationBuilder.

        :param name: The name of the hook.
        :param constraint: The constraint of the hook.
        :param mode: The mode of the hook.
        :return: The WriteContextConfigurationBuilder instance.
        """
        self._write_context_config.required_hooks.append(
            openapi_client.WriteContextConfigInfoRequiredHooksInner(
                hook=name,
                constraint=constraint,
                mode=WriteContextHookMode(mode).value,
            )
        )
        return self

    def build(self) -> openapi_client.WriteContextConfigInfo:
        """
        Build the WriteContextConfigInfo.

        :return: The built WriteContextConfigInfo.
        """
        return self._write_context_config
