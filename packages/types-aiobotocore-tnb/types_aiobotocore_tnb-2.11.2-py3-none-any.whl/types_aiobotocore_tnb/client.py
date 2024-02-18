"""
Type annotations for tnb service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_tnb.client import TelcoNetworkBuilderClient

    session = get_session()
    async with session.create_client("tnb") as client:
        client: TelcoNetworkBuilderClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import NsdOperationalStateType, OperationalStateType
from .paginator import (
    ListSolFunctionInstancesPaginator,
    ListSolFunctionPackagesPaginator,
    ListSolNetworkInstancesPaginator,
    ListSolNetworkOperationsPaginator,
    ListSolNetworkPackagesPaginator,
)
from .type_defs import (
    BlobTypeDef,
    CreateSolFunctionPackageOutputTypeDef,
    CreateSolNetworkInstanceOutputTypeDef,
    CreateSolNetworkPackageOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    GetSolFunctionInstanceOutputTypeDef,
    GetSolFunctionPackageContentOutputTypeDef,
    GetSolFunctionPackageDescriptorOutputTypeDef,
    GetSolFunctionPackageOutputTypeDef,
    GetSolNetworkInstanceOutputTypeDef,
    GetSolNetworkOperationOutputTypeDef,
    GetSolNetworkPackageContentOutputTypeDef,
    GetSolNetworkPackageDescriptorOutputTypeDef,
    GetSolNetworkPackageOutputTypeDef,
    InstantiateSolNetworkInstanceOutputTypeDef,
    ListSolFunctionInstancesOutputTypeDef,
    ListSolFunctionPackagesOutputTypeDef,
    ListSolNetworkInstancesOutputTypeDef,
    ListSolNetworkOperationsOutputTypeDef,
    ListSolNetworkPackagesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PutSolFunctionPackageContentOutputTypeDef,
    PutSolNetworkPackageContentOutputTypeDef,
    TerminateSolNetworkInstanceOutputTypeDef,
    UpdateSolFunctionPackageOutputTypeDef,
    UpdateSolNetworkInstanceOutputTypeDef,
    UpdateSolNetworkModifyTypeDef,
    UpdateSolNetworkPackageOutputTypeDef,
    ValidateSolFunctionPackageContentOutputTypeDef,
    ValidateSolNetworkPackageContentOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("TelcoNetworkBuilderClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class TelcoNetworkBuilderClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TelcoNetworkBuilderClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#can_paginate)
        """

    async def cancel_sol_network_operation(
        self, *, nsLcmOpOccId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Cancels a network operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.cancel_sol_network_operation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#cancel_sol_network_operation)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#close)
        """

    async def create_sol_function_package(
        self, *, tags: Mapping[str, str] = ...
    ) -> CreateSolFunctionPackageOutputTypeDef:
        """
        Creates a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.create_sol_function_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#create_sol_function_package)
        """

    async def create_sol_network_instance(
        self,
        *,
        nsName: str,
        nsdInfoId: str,
        nsDescription: str = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateSolNetworkInstanceOutputTypeDef:
        """
        Creates a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.create_sol_network_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#create_sol_network_instance)
        """

    async def create_sol_network_package(
        self, *, tags: Mapping[str, str] = ...
    ) -> CreateSolNetworkPackageOutputTypeDef:
        """
        Creates a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.create_sol_network_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#create_sol_network_package)
        """

    async def delete_sol_function_package(self, *, vnfPkgId: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.delete_sol_function_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#delete_sol_function_package)
        """

    async def delete_sol_network_instance(
        self, *, nsInstanceId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.delete_sol_network_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#delete_sol_network_instance)
        """

    async def delete_sol_network_package(self, *, nsdInfoId: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.delete_sol_network_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#delete_sol_network_package)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#generate_presigned_url)
        """

    async def get_sol_function_instance(
        self, *, vnfInstanceId: str
    ) -> GetSolFunctionInstanceOutputTypeDef:
        """
        Gets the details of a network function instance, including the instantation
        state and metadata from the function package descriptor in the network function
        package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_function_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_sol_function_instance)
        """

    async def get_sol_function_package(
        self, *, vnfPkgId: str
    ) -> GetSolFunctionPackageOutputTypeDef:
        """
        Gets the details of an individual function package, such as the operational
        state and whether the package is in
        use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_function_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_sol_function_package)
        """

    async def get_sol_function_package_content(
        self, *, accept: Literal["application/zip"], vnfPkgId: str
    ) -> GetSolFunctionPackageContentOutputTypeDef:
        """
        Gets the contents of a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_function_package_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_sol_function_package_content)
        """

    async def get_sol_function_package_descriptor(
        self, *, accept: Literal["text/plain"], vnfPkgId: str
    ) -> GetSolFunctionPackageDescriptorOutputTypeDef:
        """
        Gets a function package descriptor in a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_function_package_descriptor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_sol_function_package_descriptor)
        """

    async def get_sol_network_instance(
        self, *, nsInstanceId: str
    ) -> GetSolNetworkInstanceOutputTypeDef:
        """
        Gets the details of the network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_network_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_sol_network_instance)
        """

    async def get_sol_network_operation(
        self, *, nsLcmOpOccId: str
    ) -> GetSolNetworkOperationOutputTypeDef:
        """
        Gets the details of a network operation, including the tasks involved in the
        network operation and the status of the
        tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_network_operation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_sol_network_operation)
        """

    async def get_sol_network_package(self, *, nsdInfoId: str) -> GetSolNetworkPackageOutputTypeDef:
        """
        Gets the details of a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_network_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_sol_network_package)
        """

    async def get_sol_network_package_content(
        self, *, accept: Literal["application/zip"], nsdInfoId: str
    ) -> GetSolNetworkPackageContentOutputTypeDef:
        """
        Gets the contents of a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_network_package_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_sol_network_package_content)
        """

    async def get_sol_network_package_descriptor(
        self, *, nsdInfoId: str
    ) -> GetSolNetworkPackageDescriptorOutputTypeDef:
        """
        Gets the content of the network service descriptor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_network_package_descriptor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_sol_network_package_descriptor)
        """

    async def instantiate_sol_network_instance(
        self,
        *,
        nsInstanceId: str,
        additionalParamsForNs: Mapping[str, Any] = ...,
        dryRun: bool = ...,
        tags: Mapping[str, str] = ...,
    ) -> InstantiateSolNetworkInstanceOutputTypeDef:
        """
        Instantiates a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.instantiate_sol_network_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#instantiate_sol_network_instance)
        """

    async def list_sol_function_instances(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListSolFunctionInstancesOutputTypeDef:
        """
        Lists network function instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.list_sol_function_instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#list_sol_function_instances)
        """

    async def list_sol_function_packages(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListSolFunctionPackagesOutputTypeDef:
        """
        Lists information about function packages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.list_sol_function_packages)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#list_sol_function_packages)
        """

    async def list_sol_network_instances(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListSolNetworkInstancesOutputTypeDef:
        """
        Lists your network instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.list_sol_network_instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#list_sol_network_instances)
        """

    async def list_sol_network_operations(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListSolNetworkOperationsOutputTypeDef:
        """
        Lists details for a network operation, including when the operation started and
        the status of the
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.list_sol_network_operations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#list_sol_network_operations)
        """

    async def list_sol_network_packages(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListSolNetworkPackagesOutputTypeDef:
        """
        Lists network packages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.list_sol_network_packages)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#list_sol_network_packages)
        """

    async def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Lists tags for AWS TNB resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#list_tags_for_resource)
        """

    async def put_sol_function_package_content(
        self, *, file: BlobTypeDef, vnfPkgId: str, contentType: Literal["application/zip"] = ...
    ) -> PutSolFunctionPackageContentOutputTypeDef:
        """
        Uploads the contents of a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.put_sol_function_package_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#put_sol_function_package_content)
        """

    async def put_sol_network_package_content(
        self, *, file: BlobTypeDef, nsdInfoId: str, contentType: Literal["application/zip"] = ...
    ) -> PutSolNetworkPackageContentOutputTypeDef:
        """
        Uploads the contents of a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.put_sol_network_package_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#put_sol_network_package_content)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Tags an AWS TNB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#tag_resource)
        """

    async def terminate_sol_network_instance(
        self, *, nsInstanceId: str, tags: Mapping[str, str] = ...
    ) -> TerminateSolNetworkInstanceOutputTypeDef:
        """
        Terminates a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.terminate_sol_network_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#terminate_sol_network_instance)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Untags an AWS TNB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#untag_resource)
        """

    async def update_sol_function_package(
        self, *, operationalState: OperationalStateType, vnfPkgId: str
    ) -> UpdateSolFunctionPackageOutputTypeDef:
        """
        Updates the operational state of function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.update_sol_function_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#update_sol_function_package)
        """

    async def update_sol_network_instance(
        self,
        *,
        nsInstanceId: str,
        updateType: Literal["MODIFY_VNF_INFORMATION"],
        modifyVnfInfoData: UpdateSolNetworkModifyTypeDef = ...,
        tags: Mapping[str, str] = ...,
    ) -> UpdateSolNetworkInstanceOutputTypeDef:
        """
        Update a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.update_sol_network_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#update_sol_network_instance)
        """

    async def update_sol_network_package(
        self, *, nsdInfoId: str, nsdOperationalState: NsdOperationalStateType
    ) -> UpdateSolNetworkPackageOutputTypeDef:
        """
        Updates the operational state of a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.update_sol_network_package)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#update_sol_network_package)
        """

    async def validate_sol_function_package_content(
        self, *, file: BlobTypeDef, vnfPkgId: str, contentType: Literal["application/zip"] = ...
    ) -> ValidateSolFunctionPackageContentOutputTypeDef:
        """
        Validates function package content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.validate_sol_function_package_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#validate_sol_function_package_content)
        """

    async def validate_sol_network_package_content(
        self, *, file: BlobTypeDef, nsdInfoId: str, contentType: Literal["application/zip"] = ...
    ) -> ValidateSolNetworkPackageContentOutputTypeDef:
        """
        Validates network package content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.validate_sol_network_package_content)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#validate_sol_network_package_content)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_sol_function_instances"]
    ) -> ListSolFunctionInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_sol_function_packages"]
    ) -> ListSolFunctionPackagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_sol_network_instances"]
    ) -> ListSolNetworkInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_sol_network_operations"]
    ) -> ListSolNetworkOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_sol_network_packages"]
    ) -> ListSolNetworkPackagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/#get_paginator)
        """

    async def __aenter__(self) -> "TelcoNetworkBuilderClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/client/)
        """
