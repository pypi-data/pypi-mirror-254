"""
Type annotations for pca-connector-ad service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_pca_connector_ad.client import PcaConnectorAdClient

    session = get_session()
    async with session.create_client("pca-connector-ad") as client:
        client: PcaConnectorAdClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .paginator import (
    ListConnectorsPaginator,
    ListDirectoryRegistrationsPaginator,
    ListServicePrincipalNamesPaginator,
    ListTemplateGroupAccessControlEntriesPaginator,
    ListTemplatesPaginator,
)
from .type_defs import (
    AccessRightsTypeDef,
    CreateConnectorResponseTypeDef,
    CreateDirectoryRegistrationResponseTypeDef,
    CreateTemplateResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetConnectorResponseTypeDef,
    GetDirectoryRegistrationResponseTypeDef,
    GetServicePrincipalNameResponseTypeDef,
    GetTemplateGroupAccessControlEntryResponseTypeDef,
    GetTemplateResponseTypeDef,
    ListConnectorsResponseTypeDef,
    ListDirectoryRegistrationsResponseTypeDef,
    ListServicePrincipalNamesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateGroupAccessControlEntriesResponseTypeDef,
    ListTemplatesResponseTypeDef,
    TemplateDefinitionTypeDef,
    VpcInformationTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PcaConnectorAdClient",)

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
    ValidationException: Type[BotocoreClientError]

class PcaConnectorAdClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PcaConnectorAdClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#close)
        """

    async def create_connector(
        self,
        *,
        CertificateAuthorityArn: str,
        DirectoryId: str,
        VpcInformation: VpcInformationTypeDef,
        ClientToken: str = ...,
        Tags: Mapping[str, str] = ...,
    ) -> CreateConnectorResponseTypeDef:
        """
        Creates a connector between Amazon Web Services Private CA and an Active
        Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.create_connector)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#create_connector)
        """

    async def create_directory_registration(
        self, *, DirectoryId: str, ClientToken: str = ..., Tags: Mapping[str, str] = ...
    ) -> CreateDirectoryRegistrationResponseTypeDef:
        """
        Creates a directory registration that authorizes communication between Amazon
        Web Services Private CA and an Active Directory See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/pca-connector-ad-2018-05-10/CreateDirectoryRegistration).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.create_directory_registration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#create_directory_registration)
        """

    async def create_service_principal_name(
        self, *, ConnectorArn: str, DirectoryRegistrationArn: str, ClientToken: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a service principal name (SPN) for the service account in Active
        Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.create_service_principal_name)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#create_service_principal_name)
        """

    async def create_template(
        self,
        *,
        ConnectorArn: str,
        Definition: TemplateDefinitionTypeDef,
        Name: str,
        ClientToken: str = ...,
        Tags: Mapping[str, str] = ...,
    ) -> CreateTemplateResponseTypeDef:
        """
        Creates an Active Directory compatible certificate template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.create_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#create_template)
        """

    async def create_template_group_access_control_entry(
        self,
        *,
        AccessRights: AccessRightsTypeDef,
        GroupDisplayName: str,
        GroupSecurityIdentifier: str,
        TemplateArn: str,
        ClientToken: str = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Create a group access control entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.create_template_group_access_control_entry)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#create_template_group_access_control_entry)
        """

    async def delete_connector(self, *, ConnectorArn: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a connector for Active Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.delete_connector)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#delete_connector)
        """

    async def delete_directory_registration(
        self, *, DirectoryRegistrationArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a directory registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.delete_directory_registration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#delete_directory_registration)
        """

    async def delete_service_principal_name(
        self, *, ConnectorArn: str, DirectoryRegistrationArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the service principal name (SPN) used by a connector to authenticate
        with your Active
        Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.delete_service_principal_name)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#delete_service_principal_name)
        """

    async def delete_template(self, *, TemplateArn: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.delete_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#delete_template)
        """

    async def delete_template_group_access_control_entry(
        self, *, GroupSecurityIdentifier: str, TemplateArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a group access control entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.delete_template_group_access_control_entry)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#delete_template_group_access_control_entry)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#generate_presigned_url)
        """

    async def get_connector(self, *, ConnectorArn: str) -> GetConnectorResponseTypeDef:
        """
        Lists information about your connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_connector)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_connector)
        """

    async def get_directory_registration(
        self, *, DirectoryRegistrationArn: str
    ) -> GetDirectoryRegistrationResponseTypeDef:
        """
        A structure that contains information about your directory registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_directory_registration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_directory_registration)
        """

    async def get_service_principal_name(
        self, *, ConnectorArn: str, DirectoryRegistrationArn: str
    ) -> GetServicePrincipalNameResponseTypeDef:
        """
        Lists the service principal name that the connector uses to authenticate with
        Active
        Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_service_principal_name)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_service_principal_name)
        """

    async def get_template(self, *, TemplateArn: str) -> GetTemplateResponseTypeDef:
        """
        Retrieves a certificate template that the connector uses to issue certificates
        from a private
        CA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_template)
        """

    async def get_template_group_access_control_entry(
        self, *, GroupSecurityIdentifier: str, TemplateArn: str
    ) -> GetTemplateGroupAccessControlEntryResponseTypeDef:
        """
        Retrieves the group access control entries for a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_template_group_access_control_entry)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_template_group_access_control_entry)
        """

    async def list_connectors(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListConnectorsResponseTypeDef:
        """
        Lists the connectors that you created by using the
        [https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector)
        action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.list_connectors)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#list_connectors)
        """

    async def list_directory_registrations(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListDirectoryRegistrationsResponseTypeDef:
        """
        Lists the directory registrations that you created by using the
        [https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration)
        action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.list_directory_registrations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#list_directory_registrations)
        """

    async def list_service_principal_names(
        self, *, DirectoryRegistrationArn: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListServicePrincipalNamesResponseTypeDef:
        """
        Lists the service principal names that the connector uses to authenticate with
        Active
        Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.list_service_principal_names)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#list_service_principal_names)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags, if any, that are associated with your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#list_tags_for_resource)
        """

    async def list_template_group_access_control_entries(
        self, *, TemplateArn: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListTemplateGroupAccessControlEntriesResponseTypeDef:
        """
        Lists group access control entries you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.list_template_group_access_control_entries)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#list_template_group_access_control_entries)
        """

    async def list_templates(
        self, *, ConnectorArn: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListTemplatesResponseTypeDef:
        """
        Lists the templates, if any, that are associated with a connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.list_templates)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#list_templates)
        """

    async def tag_resource(
        self, *, ResourceArn: str, Tags: Mapping[str, str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#tag_resource)
        """

    async def untag_resource(
        self, *, ResourceArn: str, TagKeys: Sequence[str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes one or more tags from your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#untag_resource)
        """

    async def update_template(
        self,
        *,
        TemplateArn: str,
        Definition: TemplateDefinitionTypeDef = ...,
        ReenrollAllCertificateHolders: bool = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update template configuration to define the information included in
        certificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.update_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#update_template)
        """

    async def update_template_group_access_control_entry(
        self,
        *,
        GroupSecurityIdentifier: str,
        TemplateArn: str,
        AccessRights: AccessRightsTypeDef = ...,
        GroupDisplayName: str = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update a group access control entry you created using
        [CreateTemplateGroupAccessControlEntry](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplateGroupAccessControlEntry.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.update_template_group_access_control_entry)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#update_template_group_access_control_entry)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_connectors"]) -> ListConnectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_directory_registrations"]
    ) -> ListDirectoryRegistrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_principal_names"]
    ) -> ListServicePrincipalNamesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_group_access_control_entries"]
    ) -> ListTemplateGroupAccessControlEntriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_templates"]) -> ListTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/#get_paginator)
        """

    async def __aenter__(self) -> "PcaConnectorAdClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pca-connector-ad.html#PcaConnectorAd.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/client/)
        """
