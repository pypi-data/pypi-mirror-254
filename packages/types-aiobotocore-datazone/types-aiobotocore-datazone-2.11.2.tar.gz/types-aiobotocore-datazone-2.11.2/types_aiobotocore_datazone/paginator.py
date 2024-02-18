"""
Type annotations for datazone service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_datazone.client import DataZoneClient
    from types_aiobotocore_datazone.paginator import (
        ListAssetRevisionsPaginator,
        ListDataSourceRunActivitiesPaginator,
        ListDataSourceRunsPaginator,
        ListDataSourcesPaginator,
        ListDomainsPaginator,
        ListEnvironmentBlueprintConfigurationsPaginator,
        ListEnvironmentBlueprintsPaginator,
        ListEnvironmentProfilesPaginator,
        ListEnvironmentsPaginator,
        ListNotificationsPaginator,
        ListProjectMembershipsPaginator,
        ListProjectsPaginator,
        ListSubscriptionGrantsPaginator,
        ListSubscriptionRequestsPaginator,
        ListSubscriptionTargetsPaginator,
        ListSubscriptionsPaginator,
        SearchPaginator,
        SearchGroupProfilesPaginator,
        SearchListingsPaginator,
        SearchTypesPaginator,
        SearchUserProfilesPaginator,
    )

    session = get_session()
    with session.create_client("datazone") as client:
        client: DataZoneClient

        list_asset_revisions_paginator: ListAssetRevisionsPaginator = client.get_paginator("list_asset_revisions")
        list_data_source_run_activities_paginator: ListDataSourceRunActivitiesPaginator = client.get_paginator("list_data_source_run_activities")
        list_data_source_runs_paginator: ListDataSourceRunsPaginator = client.get_paginator("list_data_source_runs")
        list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
        list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
        list_environment_blueprint_configurations_paginator: ListEnvironmentBlueprintConfigurationsPaginator = client.get_paginator("list_environment_blueprint_configurations")
        list_environment_blueprints_paginator: ListEnvironmentBlueprintsPaginator = client.get_paginator("list_environment_blueprints")
        list_environment_profiles_paginator: ListEnvironmentProfilesPaginator = client.get_paginator("list_environment_profiles")
        list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
        list_notifications_paginator: ListNotificationsPaginator = client.get_paginator("list_notifications")
        list_project_memberships_paginator: ListProjectMembershipsPaginator = client.get_paginator("list_project_memberships")
        list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
        list_subscription_grants_paginator: ListSubscriptionGrantsPaginator = client.get_paginator("list_subscription_grants")
        list_subscription_requests_paginator: ListSubscriptionRequestsPaginator = client.get_paginator("list_subscription_requests")
        list_subscription_targets_paginator: ListSubscriptionTargetsPaginator = client.get_paginator("list_subscription_targets")
        list_subscriptions_paginator: ListSubscriptionsPaginator = client.get_paginator("list_subscriptions")
        search_paginator: SearchPaginator = client.get_paginator("search")
        search_group_profiles_paginator: SearchGroupProfilesPaginator = client.get_paginator("search_group_profiles")
        search_listings_paginator: SearchListingsPaginator = client.get_paginator("search_listings")
        search_types_paginator: SearchTypesPaginator = client.get_paginator("search_types")
        search_user_profiles_paginator: SearchUserProfilesPaginator = client.get_paginator("search_user_profiles")
    ```
"""

import sys
from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import (
    DataAssetActivityStatusType,
    DataSourceRunStatusType,
    DataSourceStatusType,
    DomainStatusType,
    EnvironmentStatusType,
    GroupSearchTypeType,
    InventorySearchScopeType,
    NotificationTypeType,
    SortKeyType,
    SortOrderType,
    SubscriptionRequestStatusType,
    SubscriptionStatusType,
    TaskStatusType,
    TypesSearchScopeType,
    UserSearchTypeType,
)
from .type_defs import (
    FilterClauseTypeDef,
    ListAssetRevisionsOutputTypeDef,
    ListDataSourceRunActivitiesOutputTypeDef,
    ListDataSourceRunsOutputTypeDef,
    ListDataSourcesOutputTypeDef,
    ListDomainsOutputTypeDef,
    ListEnvironmentBlueprintConfigurationsOutputTypeDef,
    ListEnvironmentBlueprintsOutputTypeDef,
    ListEnvironmentProfilesOutputTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListNotificationsOutputTypeDef,
    ListProjectMembershipsOutputTypeDef,
    ListProjectsOutputTypeDef,
    ListSubscriptionGrantsOutputTypeDef,
    ListSubscriptionRequestsOutputTypeDef,
    ListSubscriptionsOutputTypeDef,
    ListSubscriptionTargetsOutputTypeDef,
    PaginatorConfigTypeDef,
    SearchGroupProfilesOutputTypeDef,
    SearchInItemTypeDef,
    SearchListingsOutputTypeDef,
    SearchOutputPaginatorTypeDef,
    SearchSortTypeDef,
    SearchTypesOutputTypeDef,
    SearchUserProfilesOutputTypeDef,
    TimestampTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListAssetRevisionsPaginator",
    "ListDataSourceRunActivitiesPaginator",
    "ListDataSourceRunsPaginator",
    "ListDataSourcesPaginator",
    "ListDomainsPaginator",
    "ListEnvironmentBlueprintConfigurationsPaginator",
    "ListEnvironmentBlueprintsPaginator",
    "ListEnvironmentProfilesPaginator",
    "ListEnvironmentsPaginator",
    "ListNotificationsPaginator",
    "ListProjectMembershipsPaginator",
    "ListProjectsPaginator",
    "ListSubscriptionGrantsPaginator",
    "ListSubscriptionRequestsPaginator",
    "ListSubscriptionTargetsPaginator",
    "ListSubscriptionsPaginator",
    "SearchPaginator",
    "SearchGroupProfilesPaginator",
    "SearchListingsPaginator",
    "SearchTypesPaginator",
    "SearchUserProfilesPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListAssetRevisionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListAssetRevisions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listassetrevisionspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAssetRevisionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListAssetRevisions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listassetrevisionspaginator)
        """


class ListDataSourceRunActivitiesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListDataSourceRunActivities)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listdatasourcerunactivitiespaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        status: DataAssetActivityStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListDataSourceRunActivitiesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListDataSourceRunActivities.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listdatasourcerunactivitiespaginator)
        """


class ListDataSourceRunsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListDataSourceRuns)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listdatasourcerunspaginator)
    """

    def paginate(
        self,
        *,
        dataSourceIdentifier: str,
        domainIdentifier: str,
        status: DataSourceRunStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListDataSourceRunsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListDataSourceRuns.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listdatasourcerunspaginator)
        """


class ListDataSourcesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListDataSources)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listdatasourcespaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        environmentIdentifier: str = ...,
        name: str = ...,
        status: DataSourceStatusType = ...,
        type: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListDataSourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListDataSources.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listdatasourcespaginator)
        """


class ListDomainsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListDomains)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listdomainspaginator)
    """

    def paginate(
        self, *, status: DomainStatusType = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListDomainsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListDomains.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listdomainspaginator)
        """


class ListEnvironmentBlueprintConfigurationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentBlueprintConfigurations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listenvironmentblueprintconfigurationspaginator)
    """

    def paginate(
        self, *, domainIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListEnvironmentBlueprintConfigurationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentBlueprintConfigurations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listenvironmentblueprintconfigurationspaginator)
        """


class ListEnvironmentBlueprintsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentBlueprints)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listenvironmentblueprintspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        managed: bool = ...,
        name: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListEnvironmentBlueprintsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentBlueprints.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listenvironmentblueprintspaginator)
        """


class ListEnvironmentProfilesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentProfiles)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listenvironmentprofilespaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        awsAccountId: str = ...,
        awsAccountRegion: str = ...,
        environmentBlueprintIdentifier: str = ...,
        name: str = ...,
        projectIdentifier: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListEnvironmentProfilesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListEnvironmentProfiles.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listenvironmentprofilespaginator)
        """


class ListEnvironmentsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListEnvironments)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listenvironmentspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        awsAccountId: str = ...,
        awsAccountRegion: str = ...,
        environmentBlueprintIdentifier: str = ...,
        environmentProfileIdentifier: str = ...,
        name: str = ...,
        provider: str = ...,
        status: EnvironmentStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListEnvironmentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListEnvironments.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listenvironmentspaginator)
        """


class ListNotificationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListNotifications)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listnotificationspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        type: NotificationTypeType,
        afterTimestamp: TimestampTypeDef = ...,
        beforeTimestamp: TimestampTypeDef = ...,
        subjects: Sequence[str] = ...,
        taskStatus: TaskStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListNotificationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListNotifications.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listnotificationspaginator)
        """


class ListProjectMembershipsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListProjectMemberships)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listprojectmembershipspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        sortBy: Literal["NAME"] = ...,
        sortOrder: SortOrderType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListProjectMembershipsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListProjectMemberships.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listprojectmembershipspaginator)
        """


class ListProjectsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListProjects)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listprojectspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        groupIdentifier: str = ...,
        name: str = ...,
        userIdentifier: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListProjectsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListProjects.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listprojectspaginator)
        """


class ListSubscriptionGrantsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionGrants)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listsubscriptiongrantspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        environmentId: str = ...,
        sortBy: SortKeyType = ...,
        sortOrder: SortOrderType = ...,
        subscribedListingId: str = ...,
        subscriptionId: str = ...,
        subscriptionTargetId: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListSubscriptionGrantsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionGrants.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listsubscriptiongrantspaginator)
        """


class ListSubscriptionRequestsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionRequests)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listsubscriptionrequestspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        approverProjectId: str = ...,
        owningProjectId: str = ...,
        sortBy: SortKeyType = ...,
        sortOrder: SortOrderType = ...,
        status: SubscriptionRequestStatusType = ...,
        subscribedListingId: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListSubscriptionRequestsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionRequests.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listsubscriptionrequestspaginator)
        """


class ListSubscriptionTargetsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionTargets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listsubscriptiontargetspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        sortBy: SortKeyType = ...,
        sortOrder: SortOrderType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListSubscriptionTargetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListSubscriptionTargets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listsubscriptiontargetspaginator)
        """


class ListSubscriptionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListSubscriptions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listsubscriptionspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        approverProjectId: str = ...,
        owningProjectId: str = ...,
        sortBy: SortKeyType = ...,
        sortOrder: SortOrderType = ...,
        status: SubscriptionStatusType = ...,
        subscribedListingId: str = ...,
        subscriptionRequestIdentifier: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListSubscriptionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.ListSubscriptions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#listsubscriptionspaginator)
        """


class SearchPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.Search)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#searchpaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        searchScope: InventorySearchScopeType,
        additionalAttributes: Sequence[Literal["FORMS"]] = ...,
        filters: FilterClauseTypeDef = ...,
        owningProjectIdentifier: str = ...,
        searchIn: Sequence[SearchInItemTypeDef] = ...,
        searchText: str = ...,
        sort: SearchSortTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchOutputPaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.Search.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#searchpaginator)
        """


class SearchGroupProfilesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.SearchGroupProfiles)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#searchgroupprofilespaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        groupType: GroupSearchTypeType,
        searchText: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchGroupProfilesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.SearchGroupProfiles.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#searchgroupprofilespaginator)
        """


class SearchListingsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.SearchListings)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#searchlistingspaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        additionalAttributes: Sequence[Literal["FORMS"]] = ...,
        filters: FilterClauseTypeDef = ...,
        searchIn: Sequence[SearchInItemTypeDef] = ...,
        searchText: str = ...,
        sort: SearchSortTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchListingsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.SearchListings.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#searchlistingspaginator)
        """


class SearchTypesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.SearchTypes)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#searchtypespaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        managed: bool,
        searchScope: TypesSearchScopeType,
        filters: FilterClauseTypeDef = ...,
        searchIn: Sequence[SearchInItemTypeDef] = ...,
        searchText: str = ...,
        sort: SearchSortTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.SearchTypes.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#searchtypespaginator)
        """


class SearchUserProfilesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.SearchUserProfiles)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#searchuserprofilespaginator)
    """

    def paginate(
        self,
        *,
        domainIdentifier: str,
        userType: UserSearchTypeType,
        searchText: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchUserProfilesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Paginator.SearchUserProfiles.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/paginators/#searchuserprofilespaginator)
        """
