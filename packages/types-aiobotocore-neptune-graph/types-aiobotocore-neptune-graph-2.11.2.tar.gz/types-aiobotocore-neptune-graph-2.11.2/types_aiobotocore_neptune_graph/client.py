"""
Type annotations for neptune-graph service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_neptune_graph.client import NeptuneGraphClient

    session = get_session()
    async with session.create_client("neptune-graph") as client:
        client: NeptuneGraphClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    ExplainModeType,
    FormatType,
    GraphSummaryModeType,
    PlanCacheTypeType,
    QueryStateInputType,
)
from .paginator import (
    ListGraphSnapshotsPaginator,
    ListGraphsPaginator,
    ListImportTasksPaginator,
    ListPrivateGraphEndpointsPaginator,
)
from .type_defs import (
    CancelImportTaskOutputTypeDef,
    CreateGraphOutputTypeDef,
    CreateGraphSnapshotOutputTypeDef,
    CreateGraphUsingImportTaskOutputTypeDef,
    CreatePrivateGraphEndpointOutputTypeDef,
    DeleteGraphOutputTypeDef,
    DeleteGraphSnapshotOutputTypeDef,
    DeletePrivateGraphEndpointOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    ExecuteQueryOutputTypeDef,
    GetGraphOutputTypeDef,
    GetGraphSnapshotOutputTypeDef,
    GetGraphSummaryOutputTypeDef,
    GetImportTaskOutputTypeDef,
    GetPrivateGraphEndpointOutputTypeDef,
    GetQueryOutputTypeDef,
    ImportOptionsTypeDef,
    ListGraphSnapshotsOutputTypeDef,
    ListGraphsOutputTypeDef,
    ListImportTasksOutputTypeDef,
    ListPrivateGraphEndpointsOutputTypeDef,
    ListQueriesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ResetGraphOutputTypeDef,
    RestoreGraphFromSnapshotOutputTypeDef,
    UpdateGraphOutputTypeDef,
    VectorSearchConfigurationTypeDef,
)
from .waiter import (
    GraphAvailableWaiter,
    GraphDeletedWaiter,
    GraphSnapshotAvailableWaiter,
    GraphSnapshotDeletedWaiter,
    ImportTaskCancelledWaiter,
    ImportTaskSuccessfulWaiter,
    PrivateGraphEndpointAvailableWaiter,
    PrivateGraphEndpointDeletedWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("NeptuneGraphClient",)


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
    UnprocessableException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class NeptuneGraphClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NeptuneGraphClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#can_paginate)
        """

    async def cancel_import_task(self, *, taskIdentifier: str) -> CancelImportTaskOutputTypeDef:
        """
        Deletes the specified import task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.cancel_import_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#cancel_import_task)
        """

    async def cancel_query(
        self, *, graphIdentifier: str, queryId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Cancels a specified query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.cancel_query)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#cancel_query)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#close)
        """

    async def create_graph(
        self,
        *,
        graphName: str,
        provisionedMemory: int,
        tags: Mapping[str, str] = ...,
        publicConnectivity: bool = ...,
        kmsKeyIdentifier: str = ...,
        vectorSearchConfiguration: VectorSearchConfigurationTypeDef = ...,
        replicaCount: int = ...,
        deletionProtection: bool = ...,
    ) -> CreateGraphOutputTypeDef:
        """
        Creates a new Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.create_graph)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#create_graph)
        """

    async def create_graph_snapshot(
        self, *, graphIdentifier: str, snapshotName: str, tags: Mapping[str, str] = ...
    ) -> CreateGraphSnapshotOutputTypeDef:
        """
        Creates a snapshot of the specific graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.create_graph_snapshot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#create_graph_snapshot)
        """

    async def create_graph_using_import_task(
        self,
        *,
        graphName: str,
        source: str,
        roleArn: str,
        tags: Mapping[str, str] = ...,
        publicConnectivity: bool = ...,
        kmsKeyIdentifier: str = ...,
        vectorSearchConfiguration: VectorSearchConfigurationTypeDef = ...,
        replicaCount: int = ...,
        deletionProtection: bool = ...,
        importOptions: ImportOptionsTypeDef = ...,
        maxProvisionedMemory: int = ...,
        minProvisionedMemory: int = ...,
        failOnError: bool = ...,
        format: FormatType = ...,
    ) -> CreateGraphUsingImportTaskOutputTypeDef:
        """
        Creates a new Neptune Analytics graph and imports data into it, either from
        Amazon Simple Storage Service (S3) or from a Neptune database or a Neptune
        database
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.create_graph_using_import_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#create_graph_using_import_task)
        """

    async def create_private_graph_endpoint(
        self,
        *,
        graphIdentifier: str,
        vpcId: str = ...,
        subnetIds: Sequence[str] = ...,
        vpcSecurityGroupIds: Sequence[str] = ...,
    ) -> CreatePrivateGraphEndpointOutputTypeDef:
        """
        Create a private graph endpoint to allow private access from to the graph from
        within a
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.create_private_graph_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#create_private_graph_endpoint)
        """

    async def delete_graph(
        self, *, graphIdentifier: str, skipSnapshot: bool
    ) -> DeleteGraphOutputTypeDef:
        """
        Deletes the specified graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.delete_graph)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#delete_graph)
        """

    async def delete_graph_snapshot(
        self, *, snapshotIdentifier: str
    ) -> DeleteGraphSnapshotOutputTypeDef:
        """
        Deletes the specifed graph snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.delete_graph_snapshot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#delete_graph_snapshot)
        """

    async def delete_private_graph_endpoint(
        self, *, graphIdentifier: str, vpcId: str
    ) -> DeletePrivateGraphEndpointOutputTypeDef:
        """
        Deletes a private graph endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.delete_private_graph_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#delete_private_graph_endpoint)
        """

    async def execute_query(
        self,
        *,
        graphIdentifier: str,
        queryString: str,
        language: Literal["OPEN_CYPHER"],
        planCache: PlanCacheTypeType = ...,
        explainMode: ExplainModeType = ...,
        queryTimeoutMilliseconds: int = ...,
    ) -> ExecuteQueryOutputTypeDef:
        """
        Execute an openCypher query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.execute_query)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#execute_query)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#generate_presigned_url)
        """

    async def get_graph(self, *, graphIdentifier: str) -> GetGraphOutputTypeDef:
        """
        Gets information about a specified graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_graph)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_graph)
        """

    async def get_graph_snapshot(self, *, snapshotIdentifier: str) -> GetGraphSnapshotOutputTypeDef:
        """
        Retrieves a specified graph snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_graph_snapshot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_graph_snapshot)
        """

    async def get_graph_summary(
        self, *, graphIdentifier: str, mode: GraphSummaryModeType = ...
    ) -> GetGraphSummaryOutputTypeDef:
        """
        Gets a graph summary for a property graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_graph_summary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_graph_summary)
        """

    async def get_import_task(self, *, taskIdentifier: str) -> GetImportTaskOutputTypeDef:
        """
        Retrieves a specified import task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_import_task)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_import_task)
        """

    async def get_private_graph_endpoint(
        self, *, graphIdentifier: str, vpcId: str
    ) -> GetPrivateGraphEndpointOutputTypeDef:
        """
        Retrieves information about a specified private endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_private_graph_endpoint)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_private_graph_endpoint)
        """

    async def get_query(self, *, graphIdentifier: str, queryId: str) -> GetQueryOutputTypeDef:
        """
        Retrieves the status of a specified query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_query)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_query)
        """

    async def list_graph_snapshots(
        self, *, graphIdentifier: str = ..., nextToken: str = ..., maxResults: int = ...
    ) -> ListGraphSnapshotsOutputTypeDef:
        """
        Lists available snapshots of a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.list_graph_snapshots)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_graph_snapshots)
        """

    async def list_graphs(
        self, *, nextToken: str = ..., maxResults: int = ...
    ) -> ListGraphsOutputTypeDef:
        """
        Lists available Neptune Analytics graphs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.list_graphs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_graphs)
        """

    async def list_import_tasks(
        self, *, nextToken: str = ..., maxResults: int = ...
    ) -> ListImportTasksOutputTypeDef:
        """
        Lists import tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.list_import_tasks)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_import_tasks)
        """

    async def list_private_graph_endpoints(
        self, *, graphIdentifier: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListPrivateGraphEndpointsOutputTypeDef:
        """
        Lists private endpoints for a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.list_private_graph_endpoints)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_private_graph_endpoints)
        """

    async def list_queries(
        self, *, graphIdentifier: str, maxResults: int, state: QueryStateInputType = ...
    ) -> ListQueriesOutputTypeDef:
        """
        Lists active openCypher queries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.list_queries)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_queries)
        """

    async def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Lists tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#list_tags_for_resource)
        """

    async def reset_graph(
        self, *, graphIdentifier: str, skipSnapshot: bool
    ) -> ResetGraphOutputTypeDef:
        """
        Empties the data from a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.reset_graph)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#reset_graph)
        """

    async def restore_graph_from_snapshot(
        self,
        *,
        snapshotIdentifier: str,
        graphName: str,
        provisionedMemory: int = ...,
        deletionProtection: bool = ...,
        tags: Mapping[str, str] = ...,
        replicaCount: int = ...,
        publicConnectivity: bool = ...,
    ) -> RestoreGraphFromSnapshotOutputTypeDef:
        """
        Restores a graph from a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.restore_graph_from_snapshot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#restore_graph_from_snapshot)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#untag_resource)
        """

    async def update_graph(
        self,
        *,
        graphIdentifier: str,
        publicConnectivity: bool = ...,
        provisionedMemory: int = ...,
        deletionProtection: bool = ...,
    ) -> UpdateGraphOutputTypeDef:
        """
        Updates the configuration of a specified Neptune Analytics graph See also: [AWS
        API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-graph-2023-11-29/UpdateGraph).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.update_graph)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#update_graph)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_graph_snapshots"]
    ) -> ListGraphSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_graphs"]) -> ListGraphsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_import_tasks"]
    ) -> ListImportTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_private_graph_endpoints"]
    ) -> ListPrivateGraphEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["graph_available"]) -> GraphAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["graph_deleted"]) -> GraphDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["graph_snapshot_available"]
    ) -> GraphSnapshotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["graph_snapshot_deleted"]
    ) -> GraphSnapshotDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["import_task_cancelled"]
    ) -> ImportTaskCancelledWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["import_task_successful"]
    ) -> ImportTaskSuccessfulWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["private_graph_endpoint_available"]
    ) -> PrivateGraphEndpointAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["private_graph_endpoint_deleted"]
    ) -> PrivateGraphEndpointDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/#get_waiter)
        """

    async def __aenter__(self) -> "NeptuneGraphClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/client/)
        """
