"""Module containing constants in azol"""
from dataclasses import dataclass
from pathlib import Path

ARMURL="https://management.azure.com"
GRAPHBETAURL="https://graph.microsoft.com/beta"
GRAPHV1URL="https://graph.microsoft.com/v1.0"
KEYVAULTURL="https://vault.azure.net"
KEYVAULTOAUTHRESOURCEID="https://vault.azure.net/"
KEYVAULTAPIVERSION="7.3"
IDENTITYPLATFORMURL="https://login.microsoftonline.com"
GRAPHOAUTHRESOURCEID="https://graph.microsoft.com/"
ARMOAUTHRESOURCEID="https://management.azure.com/"
DEFAULTSCOPE=".default"

homeDirectory = Path.home()
AZOL_HOME = str(homeDirectory) + "/.azol"
PROVIDER_CACHE_DIR = AZOL_HOME + "/provider_cache"
PROVIDER_CACHE = AZOL_HOME + "/provider_cache/refresh"
AZOLSECRETPROVIDERFOLDER = AZOL_HOME + "/secrets"
TOKENCACHEDIR = AZOL_HOME + "/token_cache"

@dataclass(frozen=True)
class OAUTHFLOWS:
    """
        A data class containing constant strings for OAuth flow types
    """
    CLIENT_CREDENTIALS="client_credential"
    DEVICE_CODE="device_code"
    REFRESH_TOKEN="refresh_token"
    RAW_TOKEN="raw_token"
    AUTHORIZATION_CODE="authorization_code"


# A mapping of the built in applications to their client_ids an reply URLs
application_map = {
    "AzurePowershell": {
        "client_id": "1950a258-227b-4e31-a9cf-717495945fc2",
        "replyUrl": "http://localhost:8400",
        "replyPort": 8400
    },
    "AzureCLI": {
        "client_id": "04b07795-8ddb-461a-bbee-02f9e1bf7b46",
        "replyUrl": "http://localhost:21282",
        "replyPort": 21282
    }
}
