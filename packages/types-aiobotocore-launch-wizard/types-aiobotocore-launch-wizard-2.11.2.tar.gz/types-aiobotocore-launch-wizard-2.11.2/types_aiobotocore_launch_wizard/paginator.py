"""
Type annotations for launch-wizard service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_launch_wizard.client import LaunchWizardClient
    from types_aiobotocore_launch_wizard.paginator import (
        ListDeploymentEventsPaginator,
        ListDeploymentsPaginator,
        ListWorkloadDeploymentPatternsPaginator,
        ListWorkloadsPaginator,
    )

    session = get_session()
    with session.create_client("launch-wizard") as client:
        client: LaunchWizardClient

        list_deployment_events_paginator: ListDeploymentEventsPaginator = client.get_paginator("list_deployment_events")
        list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
        list_workload_deployment_patterns_paginator: ListWorkloadDeploymentPatternsPaginator = client.get_paginator("list_workload_deployment_patterns")
        list_workloads_paginator: ListWorkloadsPaginator = client.get_paginator("list_workloads")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    DeploymentFilterTypeDef,
    ListDeploymentEventsOutputTypeDef,
    ListDeploymentsOutputTypeDef,
    ListWorkloadDeploymentPatternsOutputTypeDef,
    ListWorkloadsOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListDeploymentEventsPaginator",
    "ListDeploymentsPaginator",
    "ListWorkloadDeploymentPatternsPaginator",
    "ListWorkloadsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListDeploymentEventsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListDeploymentEvents)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/paginators/#listdeploymenteventspaginator)
    """

    def paginate(
        self, *, deploymentId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListDeploymentEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListDeploymentEvents.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/paginators/#listdeploymenteventspaginator)
        """


class ListDeploymentsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListDeployments)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/paginators/#listdeploymentspaginator)
    """

    def paginate(
        self,
        *,
        filters: Sequence[DeploymentFilterTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListDeploymentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListDeployments.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/paginators/#listdeploymentspaginator)
        """


class ListWorkloadDeploymentPatternsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListWorkloadDeploymentPatterns)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/paginators/#listworkloaddeploymentpatternspaginator)
    """

    def paginate(
        self, *, workloadName: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListWorkloadDeploymentPatternsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListWorkloadDeploymentPatterns.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/paginators/#listworkloaddeploymentpatternspaginator)
        """


class ListWorkloadsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListWorkloads)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/paginators/#listworkloadspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListWorkloadsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListWorkloads.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/paginators/#listworkloadspaginator)
        """
