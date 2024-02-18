"""
Type annotations for launch-wizard service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_launch_wizard.client import LaunchWizardClient

    session = get_session()
    async with session.create_client("launch-wizard") as client:
        client: LaunchWizardClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .paginator import (
    ListDeploymentEventsPaginator,
    ListDeploymentsPaginator,
    ListWorkloadDeploymentPatternsPaginator,
    ListWorkloadsPaginator,
)
from .type_defs import (
    CreateDeploymentOutputTypeDef,
    DeleteDeploymentOutputTypeDef,
    DeploymentFilterTypeDef,
    GetDeploymentOutputTypeDef,
    GetWorkloadOutputTypeDef,
    ListDeploymentEventsOutputTypeDef,
    ListDeploymentsOutputTypeDef,
    ListWorkloadDeploymentPatternsOutputTypeDef,
    ListWorkloadsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("LaunchWizardClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceLimitException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class LaunchWizardClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LaunchWizardClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#close)
        """

    async def create_deployment(
        self,
        *,
        deploymentPatternName: str,
        name: str,
        specifications: Mapping[str, str],
        workloadName: str,
        dryRun: bool = ...,
    ) -> CreateDeploymentOutputTypeDef:
        """
        Creates a deployment for the given workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.create_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#create_deployment)
        """

    async def delete_deployment(self, *, deploymentId: str) -> DeleteDeploymentOutputTypeDef:
        """
        Deletes a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.delete_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#delete_deployment)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#generate_presigned_url)
        """

    async def get_deployment(self, *, deploymentId: str) -> GetDeploymentOutputTypeDef:
        """
        Returns information about the deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.get_deployment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#get_deployment)
        """

    async def get_workload(self, *, workloadName: str) -> GetWorkloadOutputTypeDef:
        """
        Returns information about a workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.get_workload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#get_workload)
        """

    async def list_deployment_events(
        self, *, deploymentId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListDeploymentEventsOutputTypeDef:
        """
        Lists the events of a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.list_deployment_events)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#list_deployment_events)
        """

    async def list_deployments(
        self,
        *,
        filters: Sequence[DeploymentFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListDeploymentsOutputTypeDef:
        """
        Lists the deployments that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.list_deployments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#list_deployments)
        """

    async def list_workload_deployment_patterns(
        self, *, workloadName: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListWorkloadDeploymentPatternsOutputTypeDef:
        """
        Lists the workload deployment patterns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.list_workload_deployment_patterns)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#list_workload_deployment_patterns)
        """

    async def list_workloads(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListWorkloadsOutputTypeDef:
        """
        Lists the workloads.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.list_workloads)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#list_workloads)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_events"]
    ) -> ListDeploymentEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workload_deployment_patterns"]
    ) -> ListWorkloadDeploymentPatternsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workloads"]) -> ListWorkloadsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/#get_paginator)
        """

    async def __aenter__(self) -> "LaunchWizardClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_launch_wizard/client/)
        """
