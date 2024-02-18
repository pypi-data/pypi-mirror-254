"""
Type annotations for kafka service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_kafka.client import KafkaClient
    from types_aiobotocore_kafka.paginator import (
        ListClientVpcConnectionsPaginator,
        ListClusterOperationsPaginator,
        ListClusterOperationsV2Paginator,
        ListClustersPaginator,
        ListClustersV2Paginator,
        ListConfigurationRevisionsPaginator,
        ListConfigurationsPaginator,
        ListKafkaVersionsPaginator,
        ListNodesPaginator,
        ListReplicatorsPaginator,
        ListScramSecretsPaginator,
        ListVpcConnectionsPaginator,
    )

    session = get_session()
    with session.create_client("kafka") as client:
        client: KafkaClient

        list_client_vpc_connections_paginator: ListClientVpcConnectionsPaginator = client.get_paginator("list_client_vpc_connections")
        list_cluster_operations_paginator: ListClusterOperationsPaginator = client.get_paginator("list_cluster_operations")
        list_cluster_operations_v2_paginator: ListClusterOperationsV2Paginator = client.get_paginator("list_cluster_operations_v2")
        list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
        list_clusters_v2_paginator: ListClustersV2Paginator = client.get_paginator("list_clusters_v2")
        list_configuration_revisions_paginator: ListConfigurationRevisionsPaginator = client.get_paginator("list_configuration_revisions")
        list_configurations_paginator: ListConfigurationsPaginator = client.get_paginator("list_configurations")
        list_kafka_versions_paginator: ListKafkaVersionsPaginator = client.get_paginator("list_kafka_versions")
        list_nodes_paginator: ListNodesPaginator = client.get_paginator("list_nodes")
        list_replicators_paginator: ListReplicatorsPaginator = client.get_paginator("list_replicators")
        list_scram_secrets_paginator: ListScramSecretsPaginator = client.get_paginator("list_scram_secrets")
        list_vpc_connections_paginator: ListVpcConnectionsPaginator = client.get_paginator("list_vpc_connections")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    ListClientVpcConnectionsResponseTypeDef,
    ListClusterOperationsResponsePaginatorTypeDef,
    ListClusterOperationsV2ResponseTypeDef,
    ListClustersResponsePaginatorTypeDef,
    ListClustersV2ResponsePaginatorTypeDef,
    ListConfigurationRevisionsResponseTypeDef,
    ListConfigurationsResponseTypeDef,
    ListKafkaVersionsResponseTypeDef,
    ListNodesResponseTypeDef,
    ListReplicatorsResponseTypeDef,
    ListScramSecretsResponseTypeDef,
    ListVpcConnectionsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListClientVpcConnectionsPaginator",
    "ListClusterOperationsPaginator",
    "ListClusterOperationsV2Paginator",
    "ListClustersPaginator",
    "ListClustersV2Paginator",
    "ListConfigurationRevisionsPaginator",
    "ListConfigurationsPaginator",
    "ListKafkaVersionsPaginator",
    "ListNodesPaginator",
    "ListReplicatorsPaginator",
    "ListScramSecretsPaginator",
    "ListVpcConnectionsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListClientVpcConnectionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListClientVpcConnections)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listclientvpcconnectionspaginator)
    """

    def paginate(
        self, *, ClusterArn: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListClientVpcConnectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListClientVpcConnections.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listclientvpcconnectionspaginator)
        """

class ListClusterOperationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListClusterOperations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listclusteroperationspaginator)
    """

    def paginate(
        self, *, ClusterArn: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListClusterOperationsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListClusterOperations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listclusteroperationspaginator)
        """

class ListClusterOperationsV2Paginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListClusterOperationsV2)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listclusteroperationsv2paginator)
    """

    def paginate(
        self, *, ClusterArn: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListClusterOperationsV2ResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListClusterOperationsV2.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listclusteroperationsv2paginator)
        """

class ListClustersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListClusters)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listclusterspaginator)
    """

    def paginate(
        self, *, ClusterNameFilter: str = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListClustersResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListClusters.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listclusterspaginator)
        """

class ListClustersV2Paginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListClustersV2)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listclustersv2paginator)
    """

    def paginate(
        self,
        *,
        ClusterNameFilter: str = ...,
        ClusterTypeFilter: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListClustersV2ResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListClustersV2.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listclustersv2paginator)
        """

class ListConfigurationRevisionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListConfigurationRevisions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listconfigurationrevisionspaginator)
    """

    def paginate(
        self, *, Arn: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListConfigurationRevisionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListConfigurationRevisions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listconfigurationrevisionspaginator)
        """

class ListConfigurationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListConfigurations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listconfigurationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListConfigurations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listconfigurationspaginator)
        """

class ListKafkaVersionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListKafkaVersions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listkafkaversionspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListKafkaVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListKafkaVersions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listkafkaversionspaginator)
        """

class ListNodesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListNodes)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listnodespaginator)
    """

    def paginate(
        self, *, ClusterArn: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListNodesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListNodes.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listnodespaginator)
        """

class ListReplicatorsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListReplicators)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listreplicatorspaginator)
    """

    def paginate(
        self, *, ReplicatorNameFilter: str = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListReplicatorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListReplicators.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listreplicatorspaginator)
        """

class ListScramSecretsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListScramSecrets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listscramsecretspaginator)
    """

    def paginate(
        self, *, ClusterArn: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListScramSecretsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListScramSecrets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listscramsecretspaginator)
        """

class ListVpcConnectionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListVpcConnections)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listvpcconnectionspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListVpcConnectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListVpcConnections.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/paginators/#listvpcconnectionspaginator)
        """
