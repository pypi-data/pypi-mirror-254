"""
Type annotations for iotsitewise service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_iotsitewise.client import IoTSiteWiseClient
    from types_aiobotocore_iotsitewise.paginator import (
        ExecuteQueryPaginator,
        GetAssetPropertyAggregatesPaginator,
        GetAssetPropertyValueHistoryPaginator,
        GetInterpolatedAssetPropertyValuesPaginator,
        ListAccessPoliciesPaginator,
        ListActionsPaginator,
        ListAssetModelCompositeModelsPaginator,
        ListAssetModelPropertiesPaginator,
        ListAssetModelsPaginator,
        ListAssetPropertiesPaginator,
        ListAssetRelationshipsPaginator,
        ListAssetsPaginator,
        ListAssociatedAssetsPaginator,
        ListBulkImportJobsPaginator,
        ListCompositionRelationshipsPaginator,
        ListDashboardsPaginator,
        ListGatewaysPaginator,
        ListPortalsPaginator,
        ListProjectAssetsPaginator,
        ListProjectsPaginator,
        ListTimeSeriesPaginator,
    )

    session = get_session()
    with session.create_client("iotsitewise") as client:
        client: IoTSiteWiseClient

        execute_query_paginator: ExecuteQueryPaginator = client.get_paginator("execute_query")
        get_asset_property_aggregates_paginator: GetAssetPropertyAggregatesPaginator = client.get_paginator("get_asset_property_aggregates")
        get_asset_property_value_history_paginator: GetAssetPropertyValueHistoryPaginator = client.get_paginator("get_asset_property_value_history")
        get_interpolated_asset_property_values_paginator: GetInterpolatedAssetPropertyValuesPaginator = client.get_paginator("get_interpolated_asset_property_values")
        list_access_policies_paginator: ListAccessPoliciesPaginator = client.get_paginator("list_access_policies")
        list_actions_paginator: ListActionsPaginator = client.get_paginator("list_actions")
        list_asset_model_composite_models_paginator: ListAssetModelCompositeModelsPaginator = client.get_paginator("list_asset_model_composite_models")
        list_asset_model_properties_paginator: ListAssetModelPropertiesPaginator = client.get_paginator("list_asset_model_properties")
        list_asset_models_paginator: ListAssetModelsPaginator = client.get_paginator("list_asset_models")
        list_asset_properties_paginator: ListAssetPropertiesPaginator = client.get_paginator("list_asset_properties")
        list_asset_relationships_paginator: ListAssetRelationshipsPaginator = client.get_paginator("list_asset_relationships")
        list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
        list_associated_assets_paginator: ListAssociatedAssetsPaginator = client.get_paginator("list_associated_assets")
        list_bulk_import_jobs_paginator: ListBulkImportJobsPaginator = client.get_paginator("list_bulk_import_jobs")
        list_composition_relationships_paginator: ListCompositionRelationshipsPaginator = client.get_paginator("list_composition_relationships")
        list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
        list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
        list_portals_paginator: ListPortalsPaginator = client.get_paginator("list_portals")
        list_project_assets_paginator: ListProjectAssetsPaginator = client.get_paginator("list_project_assets")
        list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
        list_time_series_paginator: ListTimeSeriesPaginator = client.get_paginator("list_time_series")
    ```
"""

import sys
from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import (
    AggregateTypeType,
    AssetModelTypeType,
    IdentityTypeType,
    ListAssetModelPropertiesFilterType,
    ListAssetPropertiesFilterType,
    ListAssetsFilterType,
    ListBulkImportJobsFilterType,
    ListTimeSeriesTypeType,
    QualityType,
    ResourceTypeType,
    TimeOrderingType,
    TraversalDirectionType,
)
from .type_defs import (
    ExecuteQueryResponseTypeDef,
    GetAssetPropertyAggregatesResponseTypeDef,
    GetAssetPropertyValueHistoryResponseTypeDef,
    GetInterpolatedAssetPropertyValuesResponseTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListActionsResponseTypeDef,
    ListAssetModelCompositeModelsResponseTypeDef,
    ListAssetModelPropertiesResponsePaginatorTypeDef,
    ListAssetModelsResponseTypeDef,
    ListAssetPropertiesResponseTypeDef,
    ListAssetRelationshipsResponseTypeDef,
    ListAssetsResponseTypeDef,
    ListAssociatedAssetsResponseTypeDef,
    ListBulkImportJobsResponseTypeDef,
    ListCompositionRelationshipsResponseTypeDef,
    ListDashboardsResponseTypeDef,
    ListGatewaysResponseTypeDef,
    ListPortalsResponseTypeDef,
    ListProjectAssetsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListTimeSeriesResponseTypeDef,
    PaginatorConfigTypeDef,
    TimestampTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ExecuteQueryPaginator",
    "GetAssetPropertyAggregatesPaginator",
    "GetAssetPropertyValueHistoryPaginator",
    "GetInterpolatedAssetPropertyValuesPaginator",
    "ListAccessPoliciesPaginator",
    "ListActionsPaginator",
    "ListAssetModelCompositeModelsPaginator",
    "ListAssetModelPropertiesPaginator",
    "ListAssetModelsPaginator",
    "ListAssetPropertiesPaginator",
    "ListAssetRelationshipsPaginator",
    "ListAssetsPaginator",
    "ListAssociatedAssetsPaginator",
    "ListBulkImportJobsPaginator",
    "ListCompositionRelationshipsPaginator",
    "ListDashboardsPaginator",
    "ListGatewaysPaginator",
    "ListPortalsPaginator",
    "ListProjectAssetsPaginator",
    "ListProjectsPaginator",
    "ListTimeSeriesPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ExecuteQueryPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ExecuteQuery)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#executequerypaginator)
    """

    def paginate(
        self, *, queryStatement: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ExecuteQueryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ExecuteQuery.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#executequerypaginator)
        """

class GetAssetPropertyAggregatesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyAggregates)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#getassetpropertyaggregatespaginator)
    """

    def paginate(
        self,
        *,
        aggregateTypes: Sequence[AggregateTypeType],
        resolution: str,
        startDate: TimestampTypeDef,
        endDate: TimestampTypeDef,
        assetId: str = ...,
        propertyId: str = ...,
        propertyAlias: str = ...,
        qualities: Sequence[QualityType] = ...,
        timeOrdering: TimeOrderingType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[GetAssetPropertyAggregatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyAggregates.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#getassetpropertyaggregatespaginator)
        """

class GetAssetPropertyValueHistoryPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyValueHistory)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#getassetpropertyvaluehistorypaginator)
    """

    def paginate(
        self,
        *,
        assetId: str = ...,
        propertyId: str = ...,
        propertyAlias: str = ...,
        startDate: TimestampTypeDef = ...,
        endDate: TimestampTypeDef = ...,
        qualities: Sequence[QualityType] = ...,
        timeOrdering: TimeOrderingType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[GetAssetPropertyValueHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyValueHistory.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#getassetpropertyvaluehistorypaginator)
        """

class GetInterpolatedAssetPropertyValuesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetInterpolatedAssetPropertyValues)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#getinterpolatedassetpropertyvaluespaginator)
    """

    def paginate(
        self,
        *,
        startTimeInSeconds: int,
        endTimeInSeconds: int,
        quality: QualityType,
        intervalInSeconds: int,
        type: str,
        assetId: str = ...,
        propertyId: str = ...,
        propertyAlias: str = ...,
        startTimeOffsetInNanos: int = ...,
        endTimeOffsetInNanos: int = ...,
        intervalWindowInSeconds: int = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[GetInterpolatedAssetPropertyValuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetInterpolatedAssetPropertyValues.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#getinterpolatedassetpropertyvaluespaginator)
        """

class ListAccessPoliciesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAccessPolicies)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listaccesspoliciespaginator)
    """

    def paginate(
        self,
        *,
        identityType: IdentityTypeType = ...,
        identityId: str = ...,
        resourceType: ResourceTypeType = ...,
        resourceId: str = ...,
        iamArn: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAccessPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAccessPolicies.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listaccesspoliciespaginator)
        """

class ListActionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListActions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listactionspaginator)
    """

    def paginate(
        self,
        *,
        targetResourceType: Literal["ASSET"],
        targetResourceId: str,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListActions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listactionspaginator)
        """

class ListAssetModelCompositeModelsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetModelCompositeModels)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassetmodelcompositemodelspaginator)
    """

    def paginate(
        self, *, assetModelId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListAssetModelCompositeModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetModelCompositeModels.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassetmodelcompositemodelspaginator)
        """

class ListAssetModelPropertiesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetModelProperties)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassetmodelpropertiespaginator)
    """

    def paginate(
        self,
        *,
        assetModelId: str,
        filter: ListAssetModelPropertiesFilterType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAssetModelPropertiesResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetModelProperties.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassetmodelpropertiespaginator)
        """

class ListAssetModelsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetModels)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassetmodelspaginator)
    """

    def paginate(
        self,
        *,
        assetModelTypes: Sequence[AssetModelTypeType] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAssetModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetModels.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassetmodelspaginator)
        """

class ListAssetPropertiesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetProperties)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassetpropertiespaginator)
    """

    def paginate(
        self,
        *,
        assetId: str,
        filter: ListAssetPropertiesFilterType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAssetPropertiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetProperties.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassetpropertiespaginator)
        """

class ListAssetRelationshipsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetRelationships)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassetrelationshipspaginator)
    """

    def paginate(
        self,
        *,
        assetId: str,
        traversalType: Literal["PATH_TO_ROOT"],
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAssetRelationshipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetRelationships.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassetrelationshipspaginator)
        """

class ListAssetsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassetspaginator)
    """

    def paginate(
        self,
        *,
        assetModelId: str = ...,
        filter: ListAssetsFilterType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAssetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassetspaginator)
        """

class ListAssociatedAssetsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssociatedAssets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassociatedassetspaginator)
    """

    def paginate(
        self,
        *,
        assetId: str,
        hierarchyId: str = ...,
        traversalDirection: TraversalDirectionType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAssociatedAssetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssociatedAssets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listassociatedassetspaginator)
        """

class ListBulkImportJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListBulkImportJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listbulkimportjobspaginator)
    """

    def paginate(
        self,
        *,
        filter: ListBulkImportJobsFilterType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListBulkImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListBulkImportJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listbulkimportjobspaginator)
        """

class ListCompositionRelationshipsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListCompositionRelationships)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listcompositionrelationshipspaginator)
    """

    def paginate(
        self, *, assetModelId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListCompositionRelationshipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListCompositionRelationships.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listcompositionrelationshipspaginator)
        """

class ListDashboardsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListDashboards)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listdashboardspaginator)
    """

    def paginate(
        self, *, projectId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListDashboardsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListDashboards.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listdashboardspaginator)
        """

class ListGatewaysPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListGateways)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listgatewayspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListGatewaysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListGateways.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listgatewayspaginator)
        """

class ListPortalsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListPortals)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listportalspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListPortalsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListPortals.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listportalspaginator)
        """

class ListProjectAssetsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjectAssets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listprojectassetspaginator)
    """

    def paginate(
        self, *, projectId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListProjectAssetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjectAssets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listprojectassetspaginator)
        """

class ListProjectsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjects)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listprojectspaginator)
    """

    def paginate(
        self, *, portalId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjects.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listprojectspaginator)
        """

class ListTimeSeriesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListTimeSeries)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listtimeseriespaginator)
    """

    def paginate(
        self,
        *,
        assetId: str = ...,
        aliasPrefix: str = ...,
        timeSeriesType: ListTimeSeriesTypeType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListTimeSeriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListTimeSeries.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotsitewise/paginators/#listtimeseriespaginator)
        """
