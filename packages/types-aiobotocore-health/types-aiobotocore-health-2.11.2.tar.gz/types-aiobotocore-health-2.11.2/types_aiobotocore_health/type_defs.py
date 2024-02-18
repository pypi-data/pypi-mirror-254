"""
Type annotations for health service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_health/type_defs/)

Usage::

    ```python
    from types_aiobotocore_health.type_defs import AccountEntityAggregateTypeDef

    data: AccountEntityAggregateTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    entityStatusCodeType,
    eventScopeCodeType,
    eventStatusCodeType,
    eventTypeCategoryType,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountEntityAggregateTypeDef",
    "AffectedEntityTypeDef",
    "TimestampTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAffectedAccountsForOrganizationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "EntityAccountFilterTypeDef",
    "EventAccountFilterTypeDef",
    "OrganizationAffectedEntitiesErrorItemTypeDef",
    "DescribeEntityAggregatesForOrganizationRequestRequestTypeDef",
    "DescribeEntityAggregatesRequestRequestTypeDef",
    "EntityAggregateTypeDef",
    "EventAggregateTypeDef",
    "OrganizationEventDetailsErrorItemTypeDef",
    "DescribeEventDetailsRequestRequestTypeDef",
    "EventDetailsErrorItemTypeDef",
    "EventTypeFilterTypeDef",
    "EventTypeTypeDef",
    "OrganizationEventTypeDef",
    "EventTypeDef",
    "EventDescriptionTypeDef",
    "OrganizationEntityAggregateTypeDef",
    "DateTimeRangeTypeDef",
    "DescribeAffectedAccountsForOrganizationRequestDescribeAffectedAccountsForOrganizationPaginateTypeDef",
    "DescribeAffectedAccountsForOrganizationResponseTypeDef",
    "DescribeAffectedEntitiesResponseTypeDef",
    "DescribeHealthServiceStatusForOrganizationResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "DescribeAffectedEntitiesForOrganizationRequestDescribeAffectedEntitiesForOrganizationPaginateTypeDef",
    "DescribeAffectedEntitiesForOrganizationRequestRequestTypeDef",
    "DescribeEventDetailsForOrganizationRequestRequestTypeDef",
    "DescribeAffectedEntitiesForOrganizationResponseTypeDef",
    "DescribeEntityAggregatesResponseTypeDef",
    "DescribeEventAggregatesResponseTypeDef",
    "DescribeEventTypesRequestDescribeEventTypesPaginateTypeDef",
    "DescribeEventTypesRequestRequestTypeDef",
    "DescribeEventTypesResponseTypeDef",
    "DescribeEventsForOrganizationResponseTypeDef",
    "DescribeEventsResponseTypeDef",
    "EventDetailsTypeDef",
    "OrganizationEventDetailsTypeDef",
    "DescribeEntityAggregatesForOrganizationResponseTypeDef",
    "EntityFilterTypeDef",
    "EventFilterTypeDef",
    "OrganizationEventFilterTypeDef",
    "DescribeEventDetailsResponseTypeDef",
    "DescribeEventDetailsForOrganizationResponseTypeDef",
    "DescribeAffectedEntitiesRequestDescribeAffectedEntitiesPaginateTypeDef",
    "DescribeAffectedEntitiesRequestRequestTypeDef",
    "DescribeEventAggregatesRequestDescribeEventAggregatesPaginateTypeDef",
    "DescribeEventAggregatesRequestRequestTypeDef",
    "DescribeEventsRequestDescribeEventsPaginateTypeDef",
    "DescribeEventsRequestRequestTypeDef",
    "DescribeEventsForOrganizationRequestDescribeEventsForOrganizationPaginateTypeDef",
    "DescribeEventsForOrganizationRequestRequestTypeDef",
)

AccountEntityAggregateTypeDef = TypedDict(
    "AccountEntityAggregateTypeDef",
    {
        "accountId": NotRequired[str],
        "count": NotRequired[int],
        "statuses": NotRequired[Dict[entityStatusCodeType, int]],
    },
)
AffectedEntityTypeDef = TypedDict(
    "AffectedEntityTypeDef",
    {
        "entityArn": NotRequired[str],
        "eventArn": NotRequired[str],
        "entityValue": NotRequired[str],
        "entityUrl": NotRequired[str],
        "awsAccountId": NotRequired[str],
        "lastUpdatedTime": NotRequired[datetime],
        "statusCode": NotRequired[entityStatusCodeType],
        "tags": NotRequired[Dict[str, str]],
    },
)
TimestampTypeDef = Union[datetime, str]
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
DescribeAffectedAccountsForOrganizationRequestRequestTypeDef = TypedDict(
    "DescribeAffectedAccountsForOrganizationRequestRequestTypeDef",
    {
        "eventArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
EntityAccountFilterTypeDef = TypedDict(
    "EntityAccountFilterTypeDef",
    {
        "eventArn": str,
        "awsAccountId": NotRequired[str],
        "statusCodes": NotRequired[Sequence[entityStatusCodeType]],
    },
)
EventAccountFilterTypeDef = TypedDict(
    "EventAccountFilterTypeDef",
    {
        "eventArn": str,
        "awsAccountId": NotRequired[str],
    },
)
OrganizationAffectedEntitiesErrorItemTypeDef = TypedDict(
    "OrganizationAffectedEntitiesErrorItemTypeDef",
    {
        "awsAccountId": NotRequired[str],
        "eventArn": NotRequired[str],
        "errorName": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)
DescribeEntityAggregatesForOrganizationRequestRequestTypeDef = TypedDict(
    "DescribeEntityAggregatesForOrganizationRequestRequestTypeDef",
    {
        "eventArns": Sequence[str],
        "awsAccountIds": NotRequired[Sequence[str]],
    },
)
DescribeEntityAggregatesRequestRequestTypeDef = TypedDict(
    "DescribeEntityAggregatesRequestRequestTypeDef",
    {
        "eventArns": NotRequired[Sequence[str]],
    },
)
EntityAggregateTypeDef = TypedDict(
    "EntityAggregateTypeDef",
    {
        "eventArn": NotRequired[str],
        "count": NotRequired[int],
        "statuses": NotRequired[Dict[entityStatusCodeType, int]],
    },
)
EventAggregateTypeDef = TypedDict(
    "EventAggregateTypeDef",
    {
        "aggregateValue": NotRequired[str],
        "count": NotRequired[int],
    },
)
OrganizationEventDetailsErrorItemTypeDef = TypedDict(
    "OrganizationEventDetailsErrorItemTypeDef",
    {
        "awsAccountId": NotRequired[str],
        "eventArn": NotRequired[str],
        "errorName": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)
DescribeEventDetailsRequestRequestTypeDef = TypedDict(
    "DescribeEventDetailsRequestRequestTypeDef",
    {
        "eventArns": Sequence[str],
        "locale": NotRequired[str],
    },
)
EventDetailsErrorItemTypeDef = TypedDict(
    "EventDetailsErrorItemTypeDef",
    {
        "eventArn": NotRequired[str],
        "errorName": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)
EventTypeFilterTypeDef = TypedDict(
    "EventTypeFilterTypeDef",
    {
        "eventTypeCodes": NotRequired[Sequence[str]],
        "services": NotRequired[Sequence[str]],
        "eventTypeCategories": NotRequired[Sequence[eventTypeCategoryType]],
    },
)
EventTypeTypeDef = TypedDict(
    "EventTypeTypeDef",
    {
        "service": NotRequired[str],
        "code": NotRequired[str],
        "category": NotRequired[eventTypeCategoryType],
    },
)
OrganizationEventTypeDef = TypedDict(
    "OrganizationEventTypeDef",
    {
        "arn": NotRequired[str],
        "service": NotRequired[str],
        "eventTypeCode": NotRequired[str],
        "eventTypeCategory": NotRequired[eventTypeCategoryType],
        "eventScopeCode": NotRequired[eventScopeCodeType],
        "region": NotRequired[str],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "statusCode": NotRequired[eventStatusCodeType],
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "arn": NotRequired[str],
        "service": NotRequired[str],
        "eventTypeCode": NotRequired[str],
        "eventTypeCategory": NotRequired[eventTypeCategoryType],
        "region": NotRequired[str],
        "availabilityZone": NotRequired[str],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "statusCode": NotRequired[eventStatusCodeType],
        "eventScopeCode": NotRequired[eventScopeCodeType],
    },
)
EventDescriptionTypeDef = TypedDict(
    "EventDescriptionTypeDef",
    {
        "latestDescription": NotRequired[str],
    },
)
OrganizationEntityAggregateTypeDef = TypedDict(
    "OrganizationEntityAggregateTypeDef",
    {
        "eventArn": NotRequired[str],
        "count": NotRequired[int],
        "statuses": NotRequired[Dict[entityStatusCodeType, int]],
        "accounts": NotRequired[List[AccountEntityAggregateTypeDef]],
    },
)
DateTimeRangeTypeDef = TypedDict(
    "DateTimeRangeTypeDef",
    {
        "from": NotRequired[TimestampTypeDef],
        "to": NotRequired[TimestampTypeDef],
    },
)
DescribeAffectedAccountsForOrganizationRequestDescribeAffectedAccountsForOrganizationPaginateTypeDef = TypedDict(
    "DescribeAffectedAccountsForOrganizationRequestDescribeAffectedAccountsForOrganizationPaginateTypeDef",
    {
        "eventArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAffectedAccountsForOrganizationResponseTypeDef = TypedDict(
    "DescribeAffectedAccountsForOrganizationResponseTypeDef",
    {
        "affectedAccounts": List[str],
        "eventScopeCode": eventScopeCodeType,
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAffectedEntitiesResponseTypeDef = TypedDict(
    "DescribeAffectedEntitiesResponseTypeDef",
    {
        "entities": List[AffectedEntityTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeHealthServiceStatusForOrganizationResponseTypeDef = TypedDict(
    "DescribeHealthServiceStatusForOrganizationResponseTypeDef",
    {
        "healthServiceAccessStatusForOrganization": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAffectedEntitiesForOrganizationRequestDescribeAffectedEntitiesForOrganizationPaginateTypeDef = TypedDict(
    "DescribeAffectedEntitiesForOrganizationRequestDescribeAffectedEntitiesForOrganizationPaginateTypeDef",
    {
        "organizationEntityFilters": NotRequired[Sequence[EventAccountFilterTypeDef]],
        "locale": NotRequired[str],
        "organizationEntityAccountFilters": NotRequired[Sequence[EntityAccountFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAffectedEntitiesForOrganizationRequestRequestTypeDef = TypedDict(
    "DescribeAffectedEntitiesForOrganizationRequestRequestTypeDef",
    {
        "organizationEntityFilters": NotRequired[Sequence[EventAccountFilterTypeDef]],
        "locale": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "organizationEntityAccountFilters": NotRequired[Sequence[EntityAccountFilterTypeDef]],
    },
)
DescribeEventDetailsForOrganizationRequestRequestTypeDef = TypedDict(
    "DescribeEventDetailsForOrganizationRequestRequestTypeDef",
    {
        "organizationEventDetailFilters": Sequence[EventAccountFilterTypeDef],
        "locale": NotRequired[str],
    },
)
DescribeAffectedEntitiesForOrganizationResponseTypeDef = TypedDict(
    "DescribeAffectedEntitiesForOrganizationResponseTypeDef",
    {
        "entities": List[AffectedEntityTypeDef],
        "failedSet": List[OrganizationAffectedEntitiesErrorItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEntityAggregatesResponseTypeDef = TypedDict(
    "DescribeEntityAggregatesResponseTypeDef",
    {
        "entityAggregates": List[EntityAggregateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEventAggregatesResponseTypeDef = TypedDict(
    "DescribeEventAggregatesResponseTypeDef",
    {
        "eventAggregates": List[EventAggregateTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEventTypesRequestDescribeEventTypesPaginateTypeDef = TypedDict(
    "DescribeEventTypesRequestDescribeEventTypesPaginateTypeDef",
    {
        "filter": NotRequired[EventTypeFilterTypeDef],
        "locale": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventTypesRequestRequestTypeDef = TypedDict(
    "DescribeEventTypesRequestRequestTypeDef",
    {
        "filter": NotRequired[EventTypeFilterTypeDef],
        "locale": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeEventTypesResponseTypeDef = TypedDict(
    "DescribeEventTypesResponseTypeDef",
    {
        "eventTypes": List[EventTypeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEventsForOrganizationResponseTypeDef = TypedDict(
    "DescribeEventsForOrganizationResponseTypeDef",
    {
        "events": List[OrganizationEventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "events": List[EventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventDetailsTypeDef = TypedDict(
    "EventDetailsTypeDef",
    {
        "event": NotRequired[EventTypeDef],
        "eventDescription": NotRequired[EventDescriptionTypeDef],
        "eventMetadata": NotRequired[Dict[str, str]],
    },
)
OrganizationEventDetailsTypeDef = TypedDict(
    "OrganizationEventDetailsTypeDef",
    {
        "awsAccountId": NotRequired[str],
        "event": NotRequired[EventTypeDef],
        "eventDescription": NotRequired[EventDescriptionTypeDef],
        "eventMetadata": NotRequired[Dict[str, str]],
    },
)
DescribeEntityAggregatesForOrganizationResponseTypeDef = TypedDict(
    "DescribeEntityAggregatesForOrganizationResponseTypeDef",
    {
        "organizationEntityAggregates": List[OrganizationEntityAggregateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EntityFilterTypeDef = TypedDict(
    "EntityFilterTypeDef",
    {
        "eventArns": Sequence[str],
        "entityArns": NotRequired[Sequence[str]],
        "entityValues": NotRequired[Sequence[str]],
        "lastUpdatedTimes": NotRequired[Sequence[DateTimeRangeTypeDef]],
        "tags": NotRequired[Sequence[Mapping[str, str]]],
        "statusCodes": NotRequired[Sequence[entityStatusCodeType]],
    },
)
EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "eventArns": NotRequired[Sequence[str]],
        "eventTypeCodes": NotRequired[Sequence[str]],
        "services": NotRequired[Sequence[str]],
        "regions": NotRequired[Sequence[str]],
        "availabilityZones": NotRequired[Sequence[str]],
        "startTimes": NotRequired[Sequence[DateTimeRangeTypeDef]],
        "endTimes": NotRequired[Sequence[DateTimeRangeTypeDef]],
        "lastUpdatedTimes": NotRequired[Sequence[DateTimeRangeTypeDef]],
        "entityArns": NotRequired[Sequence[str]],
        "entityValues": NotRequired[Sequence[str]],
        "eventTypeCategories": NotRequired[Sequence[eventTypeCategoryType]],
        "tags": NotRequired[Sequence[Mapping[str, str]]],
        "eventStatusCodes": NotRequired[Sequence[eventStatusCodeType]],
    },
)
OrganizationEventFilterTypeDef = TypedDict(
    "OrganizationEventFilterTypeDef",
    {
        "eventTypeCodes": NotRequired[Sequence[str]],
        "awsAccountIds": NotRequired[Sequence[str]],
        "services": NotRequired[Sequence[str]],
        "regions": NotRequired[Sequence[str]],
        "startTime": NotRequired[DateTimeRangeTypeDef],
        "endTime": NotRequired[DateTimeRangeTypeDef],
        "lastUpdatedTime": NotRequired[DateTimeRangeTypeDef],
        "entityArns": NotRequired[Sequence[str]],
        "entityValues": NotRequired[Sequence[str]],
        "eventTypeCategories": NotRequired[Sequence[eventTypeCategoryType]],
        "eventStatusCodes": NotRequired[Sequence[eventStatusCodeType]],
    },
)
DescribeEventDetailsResponseTypeDef = TypedDict(
    "DescribeEventDetailsResponseTypeDef",
    {
        "successfulSet": List[EventDetailsTypeDef],
        "failedSet": List[EventDetailsErrorItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEventDetailsForOrganizationResponseTypeDef = TypedDict(
    "DescribeEventDetailsForOrganizationResponseTypeDef",
    {
        "successfulSet": List[OrganizationEventDetailsTypeDef],
        "failedSet": List[OrganizationEventDetailsErrorItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAffectedEntitiesRequestDescribeAffectedEntitiesPaginateTypeDef = TypedDict(
    "DescribeAffectedEntitiesRequestDescribeAffectedEntitiesPaginateTypeDef",
    {
        "filter": EntityFilterTypeDef,
        "locale": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAffectedEntitiesRequestRequestTypeDef = TypedDict(
    "DescribeAffectedEntitiesRequestRequestTypeDef",
    {
        "filter": EntityFilterTypeDef,
        "locale": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeEventAggregatesRequestDescribeEventAggregatesPaginateTypeDef = TypedDict(
    "DescribeEventAggregatesRequestDescribeEventAggregatesPaginateTypeDef",
    {
        "aggregateField": Literal["eventTypeCategory"],
        "filter": NotRequired[EventFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventAggregatesRequestRequestTypeDef = TypedDict(
    "DescribeEventAggregatesRequestRequestTypeDef",
    {
        "aggregateField": Literal["eventTypeCategory"],
        "filter": NotRequired[EventFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
DescribeEventsRequestDescribeEventsPaginateTypeDef = TypedDict(
    "DescribeEventsRequestDescribeEventsPaginateTypeDef",
    {
        "filter": NotRequired[EventFilterTypeDef],
        "locale": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsRequestRequestTypeDef = TypedDict(
    "DescribeEventsRequestRequestTypeDef",
    {
        "filter": NotRequired[EventFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "locale": NotRequired[str],
    },
)
DescribeEventsForOrganizationRequestDescribeEventsForOrganizationPaginateTypeDef = TypedDict(
    "DescribeEventsForOrganizationRequestDescribeEventsForOrganizationPaginateTypeDef",
    {
        "filter": NotRequired[OrganizationEventFilterTypeDef],
        "locale": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsForOrganizationRequestRequestTypeDef = TypedDict(
    "DescribeEventsForOrganizationRequestRequestTypeDef",
    {
        "filter": NotRequired[OrganizationEventFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "locale": NotRequired[str],
    },
)
