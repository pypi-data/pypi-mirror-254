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

@dataclass(frozen=True)
class FOCIClients:
    """
        A data class containing client IDs for FOCI Clients

        Taken from here: https://github.com/secureworks/family-of-client-ids-research/blob/main/known-foci-clients.csv
    """
    Office365Management="00b41c95-dab0-4487-9791-b9d2c32c80f2"
    MicrosoftAzurePowershell="1950a258-227b-4e31-a9cf-717495945fc2"
    MicrosoftAzureCLI="04b07795-8ddb-461a-bbee-02f9e1bf7b46"
    MicrosoftTeams="1fec8e78-bce4-4aaf-ab1b-5451cc387264"
    WindowsSearch="26a7ee05-5602-4d76-a7ba-eae8b7b67941"
    OutlookMobile="27922004-5251-4030-b22d-91ecd9a37ea4"
    MicrosoftAuthenticatorApp="4813382a-8fa7-425e-ab75-3b753aab3abb"
    OneDriveSyncEngine="ab9b8c07-8f02-4f72-87fa-80105867a763"
    MicrosoftOffice="d3590ed6-52b3-4102-aeff-aad2292ab01c"
    VisualStudio="872cd9fa-d31f-45e0-9eab-6e460a02d1f1"
    OneDriveiOSApp="af124e86-4e96-495a-b70a-90f90ab96707"
    MicrosoftBingSearchForMicrosoftEdge="2d7f3606-b07d-41d1-b9d2-0d0c9296a6e8"
    MicrosoftStreamMobileNative="844cca35-0656-46ce-b636-13f48b0eecbd"
    MicrosoftTeamsDeviceAdminAgent="87749df4-7ccf-48f8-aa87-704bad0e0e16"
    MicrosoftBingSearch="cf36b471-5b44-428c-9ce7-313bf84528de"
    OfficeUWPPWA="0ec893e0-5785-4de6-99da-4ed124e5296c"
    MicrosoftToDoClient="22098786-6e16-43cc-a27d-191a01a1e3b5"
    PowerApps="4e291c71-d680-4d0e-9640-0a3358e31177"
    MicrosoftWhiteboardClient="57336123-6e14-4acc-8dcf-287b6088aa28"
    MicrosoftFlow="57fcbcfa-7cee-4eb1-8b25-12d2030b4ee0"
    MicrosoftPlanner="66375f6b-983f-4c2c-9701-d680650f588f"
    MicrosoftIntuneCompanyPortal="9ba1a5c7-f17a-4de9-a1f1-6178c8d51223"
    AccountsControlUI="a40d7d7d-59aa-447e-a655-679a4107e548"
    YammeriPhone="a569458c-7f2b-45cb-bab9-b7dee514d112"
    OneDrive="b26aadf8-566f-4478-926f-589f601d9c74"
    MicrosoftPowerBI="c0d2a505-13b8-4ae0-aa9e-cddd5eab0b12"
    SharePoint="d326c1ce-6cc6-4de2-bebc-4591e5e13ef0"
    MicrosoftEdge="e9c51622-460d-4d3d-952d-966a5b1da34c"
    MicrosoftTunnel="eb539595-3fe1-474e-9c1d-feb3625d1be5"
    MicrosoftEdge2="ecd6b820-32c2-49b6-98a6-444530e5a77a"
    SharePointAndroid="f05ff7c9-f75a-4acd-a3b5-f4b6a870245d"
    MicrosoftEdge3="f44b1140-bc5e-48c6-8dc0-5cf5a53c0e34"
    M365ComplianceDriveClient="be1918be-3fe3-4be9-b32b-b542fc27f02e"
    MicrosoftDefenderPlatform="cab96880-db5b-4e15-90a7-f3f1d62ffe39"
    MicrosoftEdgeEnterpriseNewTabPage="d7b530a4-7680-4c23-a8bf-c52c121d2e87"
    MicrosoftDefenderForMobile="dd47d17a-3194-4d86-bfd5-c6ae6f5651e3"
    OutlookLite="e9b154d0-7658-433b-bb25-6b8e0a8a7c59"

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
