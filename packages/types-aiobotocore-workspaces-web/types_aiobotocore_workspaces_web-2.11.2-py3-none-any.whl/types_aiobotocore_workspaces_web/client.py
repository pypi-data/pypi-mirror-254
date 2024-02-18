"""
Type annotations for workspaces-web service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_workspaces_web.client import WorkSpacesWebClient

    session = get_session()
    async with session.create_client("workspaces-web") as client:
        client: WorkSpacesWebClient
    ```
"""

from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import AuthenticationTypeType, EnabledTypeType, IdentityProviderTypeType
from .type_defs import (
    AssociateBrowserSettingsResponseTypeDef,
    AssociateIpAccessSettingsResponseTypeDef,
    AssociateNetworkSettingsResponseTypeDef,
    AssociateTrustStoreResponseTypeDef,
    AssociateUserAccessLoggingSettingsResponseTypeDef,
    AssociateUserSettingsResponseTypeDef,
    BlobTypeDef,
    CookieSynchronizationConfigurationTypeDef,
    CreateBrowserSettingsResponseTypeDef,
    CreateIdentityProviderResponseTypeDef,
    CreateIpAccessSettingsResponseTypeDef,
    CreateNetworkSettingsResponseTypeDef,
    CreatePortalResponseTypeDef,
    CreateTrustStoreResponseTypeDef,
    CreateUserAccessLoggingSettingsResponseTypeDef,
    CreateUserSettingsResponseTypeDef,
    GetBrowserSettingsResponseTypeDef,
    GetIdentityProviderResponseTypeDef,
    GetIpAccessSettingsResponseTypeDef,
    GetNetworkSettingsResponseTypeDef,
    GetPortalResponseTypeDef,
    GetPortalServiceProviderMetadataResponseTypeDef,
    GetTrustStoreCertificateResponseTypeDef,
    GetTrustStoreResponseTypeDef,
    GetUserAccessLoggingSettingsResponseTypeDef,
    GetUserSettingsResponseTypeDef,
    IpRuleTypeDef,
    ListBrowserSettingsResponseTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListIpAccessSettingsResponseTypeDef,
    ListNetworkSettingsResponseTypeDef,
    ListPortalsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrustStoreCertificatesResponseTypeDef,
    ListTrustStoresResponseTypeDef,
    ListUserAccessLoggingSettingsResponseTypeDef,
    ListUserSettingsResponseTypeDef,
    TagTypeDef,
    UpdateBrowserSettingsResponseTypeDef,
    UpdateIdentityProviderResponseTypeDef,
    UpdateIpAccessSettingsResponseTypeDef,
    UpdateNetworkSettingsResponseTypeDef,
    UpdatePortalResponseTypeDef,
    UpdateTrustStoreResponseTypeDef,
    UpdateUserAccessLoggingSettingsResponseTypeDef,
    UpdateUserSettingsResponseTypeDef,
)

__all__ = ("WorkSpacesWebClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class WorkSpacesWebClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WorkSpacesWebClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#exceptions)
        """

    async def associate_browser_settings(
        self, *, browserSettingsArn: str, portalArn: str
    ) -> AssociateBrowserSettingsResponseTypeDef:
        """
        Associates a browser settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.associate_browser_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#associate_browser_settings)
        """

    async def associate_ip_access_settings(
        self, *, ipAccessSettingsArn: str, portalArn: str
    ) -> AssociateIpAccessSettingsResponseTypeDef:
        """
        Associates an IP access settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.associate_ip_access_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#associate_ip_access_settings)
        """

    async def associate_network_settings(
        self, *, networkSettingsArn: str, portalArn: str
    ) -> AssociateNetworkSettingsResponseTypeDef:
        """
        Associates a network settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.associate_network_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#associate_network_settings)
        """

    async def associate_trust_store(
        self, *, portalArn: str, trustStoreArn: str
    ) -> AssociateTrustStoreResponseTypeDef:
        """
        Associates a trust store with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.associate_trust_store)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#associate_trust_store)
        """

    async def associate_user_access_logging_settings(
        self, *, portalArn: str, userAccessLoggingSettingsArn: str
    ) -> AssociateUserAccessLoggingSettingsResponseTypeDef:
        """
        Associates a user access logging settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.associate_user_access_logging_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#associate_user_access_logging_settings)
        """

    async def associate_user_settings(
        self, *, portalArn: str, userSettingsArn: str
    ) -> AssociateUserSettingsResponseTypeDef:
        """
        Associates a user settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.associate_user_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#associate_user_settings)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#close)
        """

    async def create_browser_settings(
        self,
        *,
        browserPolicy: str,
        additionalEncryptionContext: Mapping[str, str] = ...,
        clientToken: str = ...,
        customerManagedKey: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateBrowserSettingsResponseTypeDef:
        """
        Creates a browser settings resource that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_browser_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#create_browser_settings)
        """

    async def create_identity_provider(
        self,
        *,
        identityProviderDetails: Mapping[str, str],
        identityProviderName: str,
        identityProviderType: IdentityProviderTypeType,
        portalArn: str,
        clientToken: str = ...,
    ) -> CreateIdentityProviderResponseTypeDef:
        """
        Creates an identity provider resource that is then associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_identity_provider)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#create_identity_provider)
        """

    async def create_ip_access_settings(
        self,
        *,
        ipRules: Sequence[IpRuleTypeDef],
        additionalEncryptionContext: Mapping[str, str] = ...,
        clientToken: str = ...,
        customerManagedKey: str = ...,
        description: str = ...,
        displayName: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateIpAccessSettingsResponseTypeDef:
        """
        Creates an IP access settings resource that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_ip_access_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#create_ip_access_settings)
        """

    async def create_network_settings(
        self,
        *,
        securityGroupIds: Sequence[str],
        subnetIds: Sequence[str],
        vpcId: str,
        clientToken: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateNetworkSettingsResponseTypeDef:
        """
        Creates a network settings resource that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_network_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#create_network_settings)
        """

    async def create_portal(
        self,
        *,
        additionalEncryptionContext: Mapping[str, str] = ...,
        authenticationType: AuthenticationTypeType = ...,
        clientToken: str = ...,
        customerManagedKey: str = ...,
        displayName: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreatePortalResponseTypeDef:
        """
        Creates a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_portal)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#create_portal)
        """

    async def create_trust_store(
        self,
        *,
        certificateList: Sequence[BlobTypeDef],
        clientToken: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateTrustStoreResponseTypeDef:
        """
        Creates a trust store that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_trust_store)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#create_trust_store)
        """

    async def create_user_access_logging_settings(
        self, *, kinesisStreamArn: str, clientToken: str = ..., tags: Sequence[TagTypeDef] = ...
    ) -> CreateUserAccessLoggingSettingsResponseTypeDef:
        """
        Creates a user access logging settings resource that can be associated with a
        web
        portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_user_access_logging_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#create_user_access_logging_settings)
        """

    async def create_user_settings(
        self,
        *,
        copyAllowed: EnabledTypeType,
        downloadAllowed: EnabledTypeType,
        pasteAllowed: EnabledTypeType,
        printAllowed: EnabledTypeType,
        uploadAllowed: EnabledTypeType,
        additionalEncryptionContext: Mapping[str, str] = ...,
        clientToken: str = ...,
        cookieSynchronizationConfiguration: CookieSynchronizationConfigurationTypeDef = ...,
        customerManagedKey: str = ...,
        disconnectTimeoutInMinutes: int = ...,
        idleDisconnectTimeoutInMinutes: int = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CreateUserSettingsResponseTypeDef:
        """
        Creates a user settings resource that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_user_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#create_user_settings)
        """

    async def delete_browser_settings(self, *, browserSettingsArn: str) -> Dict[str, Any]:
        """
        Deletes browser settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_browser_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#delete_browser_settings)
        """

    async def delete_identity_provider(self, *, identityProviderArn: str) -> Dict[str, Any]:
        """
        Deletes the identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_identity_provider)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#delete_identity_provider)
        """

    async def delete_ip_access_settings(self, *, ipAccessSettingsArn: str) -> Dict[str, Any]:
        """
        Deletes IP access settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_ip_access_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#delete_ip_access_settings)
        """

    async def delete_network_settings(self, *, networkSettingsArn: str) -> Dict[str, Any]:
        """
        Deletes network settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_network_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#delete_network_settings)
        """

    async def delete_portal(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Deletes a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_portal)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#delete_portal)
        """

    async def delete_trust_store(self, *, trustStoreArn: str) -> Dict[str, Any]:
        """
        Deletes the trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_trust_store)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#delete_trust_store)
        """

    async def delete_user_access_logging_settings(
        self, *, userAccessLoggingSettingsArn: str
    ) -> Dict[str, Any]:
        """
        Deletes user access logging settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_user_access_logging_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#delete_user_access_logging_settings)
        """

    async def delete_user_settings(self, *, userSettingsArn: str) -> Dict[str, Any]:
        """
        Deletes user settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_user_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#delete_user_settings)
        """

    async def disassociate_browser_settings(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Disassociates browser settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.disassociate_browser_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#disassociate_browser_settings)
        """

    async def disassociate_ip_access_settings(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Disassociates IP access settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.disassociate_ip_access_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#disassociate_ip_access_settings)
        """

    async def disassociate_network_settings(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Disassociates network settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.disassociate_network_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#disassociate_network_settings)
        """

    async def disassociate_trust_store(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Disassociates a trust store from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.disassociate_trust_store)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#disassociate_trust_store)
        """

    async def disassociate_user_access_logging_settings(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Disassociates user access logging settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.disassociate_user_access_logging_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#disassociate_user_access_logging_settings)
        """

    async def disassociate_user_settings(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Disassociates user settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.disassociate_user_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#disassociate_user_settings)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#generate_presigned_url)
        """

    async def get_browser_settings(
        self, *, browserSettingsArn: str
    ) -> GetBrowserSettingsResponseTypeDef:
        """
        Gets browser settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_browser_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#get_browser_settings)
        """

    async def get_identity_provider(
        self, *, identityProviderArn: str
    ) -> GetIdentityProviderResponseTypeDef:
        """
        Gets the identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_identity_provider)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#get_identity_provider)
        """

    async def get_ip_access_settings(
        self, *, ipAccessSettingsArn: str
    ) -> GetIpAccessSettingsResponseTypeDef:
        """
        Gets the IP access settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_ip_access_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#get_ip_access_settings)
        """

    async def get_network_settings(
        self, *, networkSettingsArn: str
    ) -> GetNetworkSettingsResponseTypeDef:
        """
        Gets the network settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_network_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#get_network_settings)
        """

    async def get_portal(self, *, portalArn: str) -> GetPortalResponseTypeDef:
        """
        Gets the web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_portal)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#get_portal)
        """

    async def get_portal_service_provider_metadata(
        self, *, portalArn: str
    ) -> GetPortalServiceProviderMetadataResponseTypeDef:
        """
        Gets the service provider metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_portal_service_provider_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#get_portal_service_provider_metadata)
        """

    async def get_trust_store(self, *, trustStoreArn: str) -> GetTrustStoreResponseTypeDef:
        """
        Gets the trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_trust_store)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#get_trust_store)
        """

    async def get_trust_store_certificate(
        self, *, thumbprint: str, trustStoreArn: str
    ) -> GetTrustStoreCertificateResponseTypeDef:
        """
        Gets the trust store certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_trust_store_certificate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#get_trust_store_certificate)
        """

    async def get_user_access_logging_settings(
        self, *, userAccessLoggingSettingsArn: str
    ) -> GetUserAccessLoggingSettingsResponseTypeDef:
        """
        Gets user access logging settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_user_access_logging_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#get_user_access_logging_settings)
        """

    async def get_user_settings(self, *, userSettingsArn: str) -> GetUserSettingsResponseTypeDef:
        """
        Gets user settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_user_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#get_user_settings)
        """

    async def list_browser_settings(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListBrowserSettingsResponseTypeDef:
        """
        Retrieves a list of browser settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_browser_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#list_browser_settings)
        """

    async def list_identity_providers(
        self, *, portalArn: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListIdentityProvidersResponseTypeDef:
        """
        Retrieves a list of identity providers for a specific web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_identity_providers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#list_identity_providers)
        """

    async def list_ip_access_settings(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListIpAccessSettingsResponseTypeDef:
        """
        Retrieves a list of IP access settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_ip_access_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#list_ip_access_settings)
        """

    async def list_network_settings(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListNetworkSettingsResponseTypeDef:
        """
        Retrieves a list of network settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_network_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#list_network_settings)
        """

    async def list_portals(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListPortalsResponseTypeDef:
        """
        Retrieves a list or web portals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_portals)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#list_portals)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves a list of tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#list_tags_for_resource)
        """

    async def list_trust_store_certificates(
        self, *, trustStoreArn: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListTrustStoreCertificatesResponseTypeDef:
        """
        Retrieves a list of trust store certificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_trust_store_certificates)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#list_trust_store_certificates)
        """

    async def list_trust_stores(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListTrustStoresResponseTypeDef:
        """
        Retrieves a list of trust stores.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_trust_stores)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#list_trust_stores)
        """

    async def list_user_access_logging_settings(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListUserAccessLoggingSettingsResponseTypeDef:
        """
        Retrieves a list of user access logging settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_user_access_logging_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#list_user_access_logging_settings)
        """

    async def list_user_settings(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListUserSettingsResponseTypeDef:
        """
        Retrieves a list of user settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_user_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#list_user_settings)
        """

    async def tag_resource(
        self, *, resourceArn: str, tags: Sequence[TagTypeDef], clientToken: str = ...
    ) -> Dict[str, Any]:
        """
        Adds or overwrites one or more tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#untag_resource)
        """

    async def update_browser_settings(
        self, *, browserSettingsArn: str, browserPolicy: str = ..., clientToken: str = ...
    ) -> UpdateBrowserSettingsResponseTypeDef:
        """
        Updates browser settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_browser_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#update_browser_settings)
        """

    async def update_identity_provider(
        self,
        *,
        identityProviderArn: str,
        clientToken: str = ...,
        identityProviderDetails: Mapping[str, str] = ...,
        identityProviderName: str = ...,
        identityProviderType: IdentityProviderTypeType = ...,
    ) -> UpdateIdentityProviderResponseTypeDef:
        """
        Updates the identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_identity_provider)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#update_identity_provider)
        """

    async def update_ip_access_settings(
        self,
        *,
        ipAccessSettingsArn: str,
        clientToken: str = ...,
        description: str = ...,
        displayName: str = ...,
        ipRules: Sequence[IpRuleTypeDef] = ...,
    ) -> UpdateIpAccessSettingsResponseTypeDef:
        """
        Updates IP access settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_ip_access_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#update_ip_access_settings)
        """

    async def update_network_settings(
        self,
        *,
        networkSettingsArn: str,
        clientToken: str = ...,
        securityGroupIds: Sequence[str] = ...,
        subnetIds: Sequence[str] = ...,
        vpcId: str = ...,
    ) -> UpdateNetworkSettingsResponseTypeDef:
        """
        Updates network settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_network_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#update_network_settings)
        """

    async def update_portal(
        self,
        *,
        portalArn: str,
        authenticationType: AuthenticationTypeType = ...,
        displayName: str = ...,
    ) -> UpdatePortalResponseTypeDef:
        """
        Updates a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_portal)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#update_portal)
        """

    async def update_trust_store(
        self,
        *,
        trustStoreArn: str,
        certificatesToAdd: Sequence[BlobTypeDef] = ...,
        certificatesToDelete: Sequence[str] = ...,
        clientToken: str = ...,
    ) -> UpdateTrustStoreResponseTypeDef:
        """
        Updates the trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_trust_store)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#update_trust_store)
        """

    async def update_user_access_logging_settings(
        self,
        *,
        userAccessLoggingSettingsArn: str,
        clientToken: str = ...,
        kinesisStreamArn: str = ...,
    ) -> UpdateUserAccessLoggingSettingsResponseTypeDef:
        """
        Updates the user access logging settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_user_access_logging_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#update_user_access_logging_settings)
        """

    async def update_user_settings(
        self,
        *,
        userSettingsArn: str,
        clientToken: str = ...,
        cookieSynchronizationConfiguration: CookieSynchronizationConfigurationTypeDef = ...,
        copyAllowed: EnabledTypeType = ...,
        disconnectTimeoutInMinutes: int = ...,
        downloadAllowed: EnabledTypeType = ...,
        idleDisconnectTimeoutInMinutes: int = ...,
        pasteAllowed: EnabledTypeType = ...,
        printAllowed: EnabledTypeType = ...,
        uploadAllowed: EnabledTypeType = ...,
    ) -> UpdateUserSettingsResponseTypeDef:
        """
        Updates the user settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_user_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/#update_user_settings)
        """

    async def __aenter__(self) -> "WorkSpacesWebClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/client/)
        """
