from antimatter.dependencies.package_hint import as_install_hint


class CapsuleError(Exception):
    """Base class for Capsule errors."""
    pass


class CapsuleDataInferenceError(CapsuleError):
    """Error when inferring a DataType fails."""
    pass


class CapsuleLocationInferenceError(CapsuleError):
    """Error when inferring a path's location type fails."""
    pass


class HandlerError(Exception):
    """Base error for handler failures."""
    pass


class HandlerFactoryError(HandlerError):
    """Error when creating a handler in the handler factory."""
    pass


class DataFormatError(HandlerError):
    """Error indicating data is not in a supported format."""
    pass


class CapsuleLoadError(CapsuleError):
    """Error when loading a Capsule."""
    pass


class CapsuleSaveError(CapsuleError):
    """Error when saving a Capsule."""
    pass


class CapsuleIsSealed(CapsuleError):
    """Error when reading data from a sealed Capsule"""
    pass


class TokenError(Exception):
    """Base error for token failures."""
    pass


class TokenExpiredError(TokenError):
    """Error for when a token has expired"""
    pass


class TokenMalformed(TokenError):
    """Error for when a token is malformed"""
    pass


class MissingDependency(Exception):
    """Human friendly error for missing dependencies"""

    def __init__(self, err: ModuleNotFoundError, override: str = None):
        self.err = err.msg
        self.hint = as_install_hint(override or err.name)

    def __str__(self):
        return f"{self.err}. {self.hint}"
