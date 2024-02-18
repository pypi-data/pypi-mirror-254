"""
Type annotations for elasticbeanstalk service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticbeanstalk/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_elasticbeanstalk.client import ElasticBeanstalkClient
    from types_aiobotocore_elasticbeanstalk.paginator import (
        DescribeApplicationVersionsPaginator,
        DescribeEnvironmentManagedActionHistoryPaginator,
        DescribeEnvironmentsPaginator,
        DescribeEventsPaginator,
        ListPlatformVersionsPaginator,
    )

    session = get_session()
    with session.create_client("elasticbeanstalk") as client:
        client: ElasticBeanstalkClient

        describe_application_versions_paginator: DescribeApplicationVersionsPaginator = client.get_paginator("describe_application_versions")
        describe_environment_managed_action_history_paginator: DescribeEnvironmentManagedActionHistoryPaginator = client.get_paginator("describe_environment_managed_action_history")
        describe_environments_paginator: DescribeEnvironmentsPaginator = client.get_paginator("describe_environments")
        describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
        list_platform_versions_paginator: ListPlatformVersionsPaginator = client.get_paginator("list_platform_versions")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import EventSeverityType
from .type_defs import (
    ApplicationVersionDescriptionsMessageTypeDef,
    DescribeEnvironmentManagedActionHistoryResultTypeDef,
    EnvironmentDescriptionsMessageTypeDef,
    EventDescriptionsMessageTypeDef,
    ListPlatformVersionsResultTypeDef,
    PaginatorConfigTypeDef,
    PlatformFilterTypeDef,
    TimestampTypeDef,
)

__all__ = (
    "DescribeApplicationVersionsPaginator",
    "DescribeEnvironmentManagedActionHistoryPaginator",
    "DescribeEnvironmentsPaginator",
    "DescribeEventsPaginator",
    "ListPlatformVersionsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class DescribeApplicationVersionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticbeanstalk/paginators/#describeapplicationversionspaginator)
    """

    def paginate(
        self,
        *,
        ApplicationName: str = ...,
        VersionLabels: Sequence[str] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ApplicationVersionDescriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticbeanstalk/paginators/#describeapplicationversionspaginator)
        """

class DescribeEnvironmentManagedActionHistoryPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticbeanstalk/paginators/#describeenvironmentmanagedactionhistorypaginator)
    """

    def paginate(
        self,
        *,
        EnvironmentId: str = ...,
        EnvironmentName: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[DescribeEnvironmentManagedActionHistoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticbeanstalk/paginators/#describeenvironmentmanagedactionhistorypaginator)
        """

class DescribeEnvironmentsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironments)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticbeanstalk/paginators/#describeenvironmentspaginator)
    """

    def paginate(
        self,
        *,
        ApplicationName: str = ...,
        VersionLabel: str = ...,
        EnvironmentIds: Sequence[str] = ...,
        EnvironmentNames: Sequence[str] = ...,
        IncludeDeleted: bool = ...,
        IncludedDeletedBackTo: TimestampTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[EnvironmentDescriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironments.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticbeanstalk/paginators/#describeenvironmentspaginator)
        """

class DescribeEventsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEvents)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticbeanstalk/paginators/#describeeventspaginator)
    """

    def paginate(
        self,
        *,
        ApplicationName: str = ...,
        VersionLabel: str = ...,
        TemplateName: str = ...,
        EnvironmentId: str = ...,
        EnvironmentName: str = ...,
        PlatformArn: str = ...,
        RequestId: str = ...,
        Severity: EventSeverityType = ...,
        StartTime: TimestampTypeDef = ...,
        EndTime: TimestampTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[EventDescriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEvents.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticbeanstalk/paginators/#describeeventspaginator)
        """

class ListPlatformVersionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.ListPlatformVersions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticbeanstalk/paginators/#listplatformversionspaginator)
    """

    def paginate(
        self,
        *,
        Filters: Sequence[PlatformFilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListPlatformVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.ListPlatformVersions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticbeanstalk/paginators/#listplatformversionspaginator)
        """
