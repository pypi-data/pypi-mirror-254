from enum import Enum


class ProviderType(str, Enum):
    GoogleOAuth = "GoogleOAuth"
    ApiKey = "APIKey"


class PrincipalType(str, Enum):
    ApiKey = "APIKey"
    Email = "Email"
    HostedDomain = "HostedDomain"
