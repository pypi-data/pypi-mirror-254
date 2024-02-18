"""
Type annotations for marketplace-deployment service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_marketplace_deployment.client import MarketplaceDeploymentServiceClient

    session = get_session()
    async with session.create_client("marketplace-deployment") as client:
        client: MarketplaceDeploymentServiceClient
    ```
"""

from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .type_defs import (
    DeploymentParameterInputTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutDeploymentParameterResponseTypeDef,
    TimestampTypeDef,
)

__all__ = ("MarketplaceDeploymentServiceClient",)

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

class MarketplaceDeploymentServiceClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MarketplaceDeploymentServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/client/#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/client/#generate_presigned_url)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags that have been added to a deployment parameter resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/client/#list_tags_for_resource)
        """

    async def put_deployment_parameter(
        self,
        *,
        agreementId: str,
        catalog: str,
        deploymentParameter: DeploymentParameterInputTypeDef,
        productId: str,
        clientToken: str = ...,
        expirationDate: TimestampTypeDef = ...,
        tags: Mapping[str, str] = ...,
    ) -> PutDeploymentParameterResponseTypeDef:
        """
        Creates or updates a deployment parameter and is targeted by `catalog` and
        `agreementId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.put_deployment_parameter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/client/#put_deployment_parameter)
        """

    async def tag_resource(
        self, *, resourceArn: str, tags: Mapping[str, str] = ...
    ) -> Dict[str, Any]:
        """
        Tags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes a tag or list of tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/client/#untag_resource)
        """

    async def __aenter__(self) -> "MarketplaceDeploymentServiceClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-deployment.html#MarketplaceDeploymentService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/client/)
        """
