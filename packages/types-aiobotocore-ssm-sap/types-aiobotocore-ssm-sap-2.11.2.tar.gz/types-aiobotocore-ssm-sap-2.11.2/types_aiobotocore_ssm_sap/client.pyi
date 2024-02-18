"""
Type annotations for ssm-sap service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_ssm_sap.client import SsmSapClient

    session = get_session()
    async with session.create_client("ssm-sap") as client:
        client: SsmSapClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import ApplicationTypeType
from .paginator import (
    ListApplicationsPaginator,
    ListComponentsPaginator,
    ListDatabasesPaginator,
    ListOperationsPaginator,
)
from .type_defs import (
    ApplicationCredentialTypeDef,
    BackintConfigTypeDef,
    DeleteResourcePermissionOutputTypeDef,
    FilterTypeDef,
    GetApplicationOutputTypeDef,
    GetComponentOutputTypeDef,
    GetDatabaseOutputTypeDef,
    GetOperationOutputTypeDef,
    GetResourcePermissionOutputTypeDef,
    ListApplicationsOutputTypeDef,
    ListComponentsOutputTypeDef,
    ListDatabasesOutputTypeDef,
    ListOperationsOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutResourcePermissionOutputTypeDef,
    RegisterApplicationOutputTypeDef,
    StartApplicationRefreshOutputTypeDef,
    UpdateApplicationSettingsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SsmSapClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SsmSapClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SsmSapClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#close)
        """

    async def delete_resource_permission(
        self,
        *,
        ResourceArn: str,
        ActionType: Literal["RESTORE"] = ...,
        SourceResourceArn: str = ...,
    ) -> DeleteResourcePermissionOutputTypeDef:
        """
        Removes permissions associated with the target database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.delete_resource_permission)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#delete_resource_permission)
        """

    async def deregister_application(self, *, ApplicationId: str) -> Dict[str, Any]:
        """
        Deregister an SAP application with AWS Systems Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.deregister_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#deregister_application)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#generate_presigned_url)
        """

    async def get_application(
        self, *, ApplicationId: str = ..., ApplicationArn: str = ..., AppRegistryArn: str = ...
    ) -> GetApplicationOutputTypeDef:
        """
        Gets an application registered with AWS Systems Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.get_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#get_application)
        """

    async def get_component(
        self, *, ApplicationId: str, ComponentId: str
    ) -> GetComponentOutputTypeDef:
        """
        Gets the component of an application registered with AWS Systems Manager for
        SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.get_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#get_component)
        """

    async def get_database(
        self,
        *,
        ApplicationId: str = ...,
        ComponentId: str = ...,
        DatabaseId: str = ...,
        DatabaseArn: str = ...,
    ) -> GetDatabaseOutputTypeDef:
        """
        Gets the SAP HANA database of an application registered with AWS Systems
        Manager for
        SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.get_database)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#get_database)
        """

    async def get_operation(self, *, OperationId: str) -> GetOperationOutputTypeDef:
        """
        Gets the details of an operation by specifying the operation ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.get_operation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#get_operation)
        """

    async def get_resource_permission(
        self, *, ResourceArn: str, ActionType: Literal["RESTORE"] = ...
    ) -> GetResourcePermissionOutputTypeDef:
        """
        Gets permissions associated with the target database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.get_resource_permission)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#get_resource_permission)
        """

    async def list_applications(
        self, *, NextToken: str = ..., MaxResults: int = ..., Filters: Sequence[FilterTypeDef] = ...
    ) -> ListApplicationsOutputTypeDef:
        """
        Lists all the applications registered with AWS Systems Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.list_applications)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#list_applications)
        """

    async def list_components(
        self, *, ApplicationId: str = ..., NextToken: str = ..., MaxResults: int = ...
    ) -> ListComponentsOutputTypeDef:
        """
        Lists all the components registered with AWS Systems Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.list_components)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#list_components)
        """

    async def list_databases(
        self,
        *,
        ApplicationId: str = ...,
        ComponentId: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListDatabasesOutputTypeDef:
        """
        Lists the SAP HANA databases of an application registered with AWS Systems
        Manager for
        SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.list_databases)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#list_databases)
        """

    async def list_operations(
        self,
        *,
        ApplicationId: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ListOperationsOutputTypeDef:
        """
        Lists the operations performed by AWS Systems Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.list_operations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#list_operations)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags on an SAP HANA application and/or database registered with AWS
        Systems Manager for
        SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#list_tags_for_resource)
        """

    async def put_resource_permission(
        self, *, ActionType: Literal["RESTORE"], SourceResourceArn: str, ResourceArn: str
    ) -> PutResourcePermissionOutputTypeDef:
        """
        Adds permissions to the target database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.put_resource_permission)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#put_resource_permission)
        """

    async def register_application(
        self,
        *,
        ApplicationId: str,
        ApplicationType: ApplicationTypeType,
        Instances: Sequence[str],
        SapInstanceNumber: str = ...,
        Sid: str = ...,
        Tags: Mapping[str, str] = ...,
        Credentials: Sequence[ApplicationCredentialTypeDef] = ...,
        DatabaseArn: str = ...,
    ) -> RegisterApplicationOutputTypeDef:
        """
        Register an SAP application with AWS Systems Manager for SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.register_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#register_application)
        """

    async def start_application_refresh(
        self, *, ApplicationId: str
    ) -> StartApplicationRefreshOutputTypeDef:
        """
        Refreshes a registered application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.start_application_refresh)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#start_application_refresh)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Creates tag for a resource by specifying the ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Delete the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#untag_resource)
        """

    async def update_application_settings(
        self,
        *,
        ApplicationId: str,
        CredentialsToAddOrUpdate: Sequence[ApplicationCredentialTypeDef] = ...,
        CredentialsToRemove: Sequence[ApplicationCredentialTypeDef] = ...,
        Backint: BackintConfigTypeDef = ...,
        DatabaseArn: str = ...,
    ) -> UpdateApplicationSettingsOutputTypeDef:
        """
        Updates the settings of an application registered with AWS Systems Manager for
        SAP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.update_application_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#update_application_settings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_components"]) -> ListComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_databases"]) -> ListDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_operations"]) -> ListOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/#get_paginator)
        """

    async def __aenter__(self) -> "SsmSapClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html#SsmSap.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/client/)
        """
