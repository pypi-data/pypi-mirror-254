import antimatter.client as openapi_client


class ReadContextBuilder:
    """
    A builder class for constructing a ReadContext object.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the ReadContextBuilder class.
        """
        self.read_context = openapi_client.AddReadContext(
            summary="",
            description="",
            readParameters=[],
            requiredHooks=[],
        )

    def set_summary(self, summary: str) -> 'ReadContextBuilder':
        """
        Sets the summary of the ReadContext.

        :param summary: The summary to set.
        :return: The instance of the builder.
        """
        self.read_context.summary = summary
        return self
    
    def set_description(self, description: str) -> 'ReadContextBuilder':
        """
        Sets the description of the ReadContext.

        :param description: The description to set.
        :return: The instance of the builder.
        """
        self.read_context.description = description
        return self
    
    def add_required_hook(self, name: str, constraint: str, write_context: str = None) -> 'ReadContextBuilder':
        """
        Adds a required hook to the ReadContext.

        :param name: The name of the hook.
        :param constraint: The constraint of the hook.
        :param write_context: The write context for the hook

        :return: The instance of the builder.
        """
        self.read_context.required_hooks.append(openapi_client.ReadContextRequiredHook(
            hook=name,
            constraint=constraint,
            write_context=write_context,
        ))
        return self

    def add_read_parameter(self, key: str, required: bool, description: str) -> 'ReadContextBuilder':
        """
        Adds a read parameter to the ReadContext.

        :param key: The key of the parameter.
        :param required: Whether the parameter is required.
        :param description: The description of the parameter.

        :return: The instance of the builder.
        """
        self.read_context.read_parameters.append(openapi_client.ReadContextParameter(
            key=key,
            required=required,
            description=description,
        ))
        return self
    
    def build(self) -> openapi_client.AddReadContext:
        """
        Builds the ReadContext and returns it.

        :return: The built ReadContext.
        """
        return self.read_context
