"""
Type annotations for neptune-graph service client waiters.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_neptune_graph.client import NeptuneGraphClient
    from types_aiobotocore_neptune_graph.waiter import (
        GraphAvailableWaiter,
        GraphDeletedWaiter,
        GraphSnapshotAvailableWaiter,
        GraphSnapshotDeletedWaiter,
        ImportTaskCancelledWaiter,
        ImportTaskSuccessfulWaiter,
        PrivateGraphEndpointAvailableWaiter,
        PrivateGraphEndpointDeletedWaiter,
    )

    session = get_session()
    async with session.create_client("neptune-graph") as client:
        client: NeptuneGraphClient

        graph_available_waiter: GraphAvailableWaiter = client.get_waiter("graph_available")
        graph_deleted_waiter: GraphDeletedWaiter = client.get_waiter("graph_deleted")
        graph_snapshot_available_waiter: GraphSnapshotAvailableWaiter = client.get_waiter("graph_snapshot_available")
        graph_snapshot_deleted_waiter: GraphSnapshotDeletedWaiter = client.get_waiter("graph_snapshot_deleted")
        import_task_cancelled_waiter: ImportTaskCancelledWaiter = client.get_waiter("import_task_cancelled")
        import_task_successful_waiter: ImportTaskSuccessfulWaiter = client.get_waiter("import_task_successful")
        private_graph_endpoint_available_waiter: PrivateGraphEndpointAvailableWaiter = client.get_waiter("private_graph_endpoint_available")
        private_graph_endpoint_deleted_waiter: PrivateGraphEndpointDeletedWaiter = client.get_waiter("private_graph_endpoint_deleted")
    ```
"""

from aiobotocore.waiter import AIOWaiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "GraphAvailableWaiter",
    "GraphDeletedWaiter",
    "GraphSnapshotAvailableWaiter",
    "GraphSnapshotDeletedWaiter",
    "ImportTaskCancelledWaiter",
    "ImportTaskSuccessfulWaiter",
    "PrivateGraphEndpointAvailableWaiter",
    "PrivateGraphEndpointDeletedWaiter",
)

class GraphAvailableWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphAvailable)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#graphavailablewaiter)
    """

    async def wait(self, *, graphIdentifier: str, WaiterConfig: WaiterConfigTypeDef = ...) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphAvailable.wait)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#graphavailablewaiter)
        """

class GraphDeletedWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphDeleted)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#graphdeletedwaiter)
    """

    async def wait(self, *, graphIdentifier: str, WaiterConfig: WaiterConfigTypeDef = ...) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphDeleted.wait)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#graphdeletedwaiter)
        """

class GraphSnapshotAvailableWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphSnapshotAvailable)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#graphsnapshotavailablewaiter)
    """

    async def wait(
        self, *, snapshotIdentifier: str, WaiterConfig: WaiterConfigTypeDef = ...
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphSnapshotAvailable.wait)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#graphsnapshotavailablewaiter)
        """

class GraphSnapshotDeletedWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphSnapshotDeleted)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#graphsnapshotdeletedwaiter)
    """

    async def wait(
        self, *, snapshotIdentifier: str, WaiterConfig: WaiterConfigTypeDef = ...
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphSnapshotDeleted.wait)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#graphsnapshotdeletedwaiter)
        """

class ImportTaskCancelledWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.ImportTaskCancelled)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#importtaskcancelledwaiter)
    """

    async def wait(self, *, taskIdentifier: str, WaiterConfig: WaiterConfigTypeDef = ...) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.ImportTaskCancelled.wait)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#importtaskcancelledwaiter)
        """

class ImportTaskSuccessfulWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.ImportTaskSuccessful)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#importtasksuccessfulwaiter)
    """

    async def wait(self, *, taskIdentifier: str, WaiterConfig: WaiterConfigTypeDef = ...) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.ImportTaskSuccessful.wait)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#importtasksuccessfulwaiter)
        """

class PrivateGraphEndpointAvailableWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.PrivateGraphEndpointAvailable)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#privategraphendpointavailablewaiter)
    """

    async def wait(
        self, *, graphIdentifier: str, vpcId: str, WaiterConfig: WaiterConfigTypeDef = ...
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.PrivateGraphEndpointAvailable.wait)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#privategraphendpointavailablewaiter)
        """

class PrivateGraphEndpointDeletedWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.PrivateGraphEndpointDeleted)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#privategraphendpointdeletedwaiter)
    """

    async def wait(
        self, *, graphIdentifier: str, vpcId: str, WaiterConfig: WaiterConfigTypeDef = ...
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Waiter.PrivateGraphEndpointDeleted.wait)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_neptune_graph/waiters/#privategraphendpointdeletedwaiter)
        """
