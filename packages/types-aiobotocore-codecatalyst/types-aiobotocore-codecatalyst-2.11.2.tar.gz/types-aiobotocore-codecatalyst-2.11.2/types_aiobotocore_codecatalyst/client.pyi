"""
Type annotations for codecatalyst service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_codecatalyst.client import CodeCatalystClient

    session = get_session()
    async with session.create_client("codecatalyst") as client:
        client: CodeCatalystClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import InstanceTypeType
from .paginator import (
    ListAccessTokensPaginator,
    ListDevEnvironmentSessionsPaginator,
    ListDevEnvironmentsPaginator,
    ListEventLogsPaginator,
    ListProjectsPaginator,
    ListSourceRepositoriesPaginator,
    ListSourceRepositoryBranchesPaginator,
    ListSpacesPaginator,
    ListWorkflowRunsPaginator,
    ListWorkflowsPaginator,
)
from .type_defs import (
    CreateAccessTokenResponseTypeDef,
    CreateDevEnvironmentResponseTypeDef,
    CreateProjectResponseTypeDef,
    CreateSourceRepositoryBranchResponseTypeDef,
    CreateSourceRepositoryResponseTypeDef,
    DeleteDevEnvironmentResponseTypeDef,
    DeleteProjectResponseTypeDef,
    DeleteSourceRepositoryResponseTypeDef,
    DeleteSpaceResponseTypeDef,
    DevEnvironmentSessionConfigurationTypeDef,
    FilterTypeDef,
    GetDevEnvironmentResponseTypeDef,
    GetProjectResponseTypeDef,
    GetSourceRepositoryCloneUrlsResponseTypeDef,
    GetSourceRepositoryResponseTypeDef,
    GetSpaceResponseTypeDef,
    GetSubscriptionResponseTypeDef,
    GetUserDetailsResponseTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowRunResponseTypeDef,
    IdeConfigurationTypeDef,
    ListAccessTokensResponseTypeDef,
    ListDevEnvironmentSessionsResponseTypeDef,
    ListDevEnvironmentsResponseTypeDef,
    ListEventLogsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListSourceRepositoriesResponseTypeDef,
    ListSourceRepositoryBranchesResponseTypeDef,
    ListSpacesResponseTypeDef,
    ListWorkflowRunsResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    PersistentStorageConfigurationTypeDef,
    ProjectListFilterTypeDef,
    RepositoryInputTypeDef,
    StartDevEnvironmentResponseTypeDef,
    StartDevEnvironmentSessionResponseTypeDef,
    StartWorkflowRunResponseTypeDef,
    StopDevEnvironmentResponseTypeDef,
    StopDevEnvironmentSessionResponseTypeDef,
    TimestampTypeDef,
    UpdateDevEnvironmentResponseTypeDef,
    UpdateProjectResponseTypeDef,
    UpdateSpaceResponseTypeDef,
    VerifySessionResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CodeCatalystClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CodeCatalystClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeCatalystClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#close)
        """

    async def create_access_token(
        self, *, name: str, expiresTime: TimestampTypeDef = ...
    ) -> CreateAccessTokenResponseTypeDef:
        """
        Creates a personal access token (PAT) for the current user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.create_access_token)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#create_access_token)
        """

    async def create_dev_environment(
        self,
        *,
        spaceName: str,
        projectName: str,
        instanceType: InstanceTypeType,
        persistentStorage: PersistentStorageConfigurationTypeDef,
        repositories: Sequence[RepositoryInputTypeDef] = ...,
        clientToken: str = ...,
        alias: str = ...,
        ides: Sequence[IdeConfigurationTypeDef] = ...,
        inactivityTimeoutMinutes: int = ...,
        vpcConnectionName: str = ...,
    ) -> CreateDevEnvironmentResponseTypeDef:
        """
        Creates a Dev Environment in Amazon CodeCatalyst, a cloud-based development
        environment that you can use to quickly work on the code stored in the source
        repositories of your
        project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.create_dev_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#create_dev_environment)
        """

    async def create_project(
        self, *, spaceName: str, displayName: str, description: str = ...
    ) -> CreateProjectResponseTypeDef:
        """
        Creates a project in a specified space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.create_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#create_project)
        """

    async def create_source_repository(
        self, *, spaceName: str, projectName: str, name: str, description: str = ...
    ) -> CreateSourceRepositoryResponseTypeDef:
        """
        Creates an empty Git-based source repository in a specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.create_source_repository)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#create_source_repository)
        """

    async def create_source_repository_branch(
        self,
        *,
        spaceName: str,
        projectName: str,
        sourceRepositoryName: str,
        name: str,
        headCommitId: str = ...,
    ) -> CreateSourceRepositoryBranchResponseTypeDef:
        """
        Creates a branch in a specified source repository in Amazon CodeCatalyst.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.create_source_repository_branch)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#create_source_repository_branch)
        """

    async def delete_access_token(self, *, id: str) -> Dict[str, Any]:
        """
        Deletes a specified personal access token (PAT).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.delete_access_token)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#delete_access_token)
        """

    async def delete_dev_environment(
        self, *, spaceName: str, projectName: str, id: str
    ) -> DeleteDevEnvironmentResponseTypeDef:
        """
        Deletes a Dev Environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.delete_dev_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#delete_dev_environment)
        """

    async def delete_project(self, *, spaceName: str, name: str) -> DeleteProjectResponseTypeDef:
        """
        Deletes a project in a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.delete_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#delete_project)
        """

    async def delete_source_repository(
        self, *, spaceName: str, projectName: str, name: str
    ) -> DeleteSourceRepositoryResponseTypeDef:
        """
        Deletes a source repository in Amazon CodeCatalyst.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.delete_source_repository)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#delete_source_repository)
        """

    async def delete_space(self, *, name: str) -> DeleteSpaceResponseTypeDef:
        """
        Deletes a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.delete_space)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#delete_space)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#generate_presigned_url)
        """

    async def get_dev_environment(
        self, *, spaceName: str, projectName: str, id: str
    ) -> GetDevEnvironmentResponseTypeDef:
        """
        Returns information about a Dev Environment for a source repository in a
        project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_dev_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_dev_environment)
        """

    async def get_project(self, *, spaceName: str, name: str) -> GetProjectResponseTypeDef:
        """
        Returns information about a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_project)
        """

    async def get_source_repository(
        self, *, spaceName: str, projectName: str, name: str
    ) -> GetSourceRepositoryResponseTypeDef:
        """
        Returns information about a source repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_source_repository)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_source_repository)
        """

    async def get_source_repository_clone_urls(
        self, *, spaceName: str, projectName: str, sourceRepositoryName: str
    ) -> GetSourceRepositoryCloneUrlsResponseTypeDef:
        """
        Returns information about the URLs that can be used with a Git client to clone
        a source
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_source_repository_clone_urls)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_source_repository_clone_urls)
        """

    async def get_space(self, *, name: str) -> GetSpaceResponseTypeDef:
        """
        Returns information about an space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_space)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_space)
        """

    async def get_subscription(self, *, spaceName: str) -> GetSubscriptionResponseTypeDef:
        """
        Returns information about the Amazon Web Services account used for billing
        purposes and the billing plan for the
        space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_subscription)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_subscription)
        """

    async def get_user_details(
        self, *, id: str = ..., userName: str = ...
    ) -> GetUserDetailsResponseTypeDef:
        """
        Returns information about a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_user_details)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_user_details)
        """

    async def get_workflow(
        self, *, spaceName: str, id: str, projectName: str
    ) -> GetWorkflowResponseTypeDef:
        """
        Returns information about a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_workflow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_workflow)
        """

    async def get_workflow_run(
        self, *, spaceName: str, id: str, projectName: str
    ) -> GetWorkflowRunResponseTypeDef:
        """
        Returns information about a specified run of a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_workflow_run)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_workflow_run)
        """

    async def list_access_tokens(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListAccessTokensResponseTypeDef:
        """
        Lists all personal access tokens (PATs) associated with the user who calls the
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.list_access_tokens)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#list_access_tokens)
        """

    async def list_dev_environment_sessions(
        self,
        *,
        spaceName: str,
        projectName: str,
        devEnvironmentId: str,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> ListDevEnvironmentSessionsResponseTypeDef:
        """
        Retrieves a list of active sessions for a Dev Environment in a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.list_dev_environment_sessions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#list_dev_environment_sessions)
        """

    async def list_dev_environments(
        self,
        *,
        spaceName: str,
        projectName: str = ...,
        filters: Sequence[FilterTypeDef] = ...,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> ListDevEnvironmentsResponseTypeDef:
        """
        Retrieves a list of Dev Environments in a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.list_dev_environments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#list_dev_environments)
        """

    async def list_event_logs(
        self,
        *,
        spaceName: str,
        startTime: TimestampTypeDef,
        endTime: TimestampTypeDef,
        eventName: str = ...,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> ListEventLogsResponseTypeDef:
        """
        Retrieves a list of events that occurred during a specific time in a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.list_event_logs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#list_event_logs)
        """

    async def list_projects(
        self,
        *,
        spaceName: str,
        nextToken: str = ...,
        maxResults: int = ...,
        filters: Sequence[ProjectListFilterTypeDef] = ...,
    ) -> ListProjectsResponseTypeDef:
        """
        Retrieves a list of projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.list_projects)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#list_projects)
        """

    async def list_source_repositories(
        self, *, spaceName: str, projectName: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListSourceRepositoriesResponseTypeDef:
        """
        Retrieves a list of source repositories in a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.list_source_repositories)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#list_source_repositories)
        """

    async def list_source_repository_branches(
        self,
        *,
        spaceName: str,
        projectName: str,
        sourceRepositoryName: str,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> ListSourceRepositoryBranchesResponseTypeDef:
        """
        Retrieves a list of branches in a specified source repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.list_source_repository_branches)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#list_source_repository_branches)
        """

    async def list_spaces(self, *, nextToken: str = ...) -> ListSpacesResponseTypeDef:
        """
        Retrieves a list of spaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.list_spaces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#list_spaces)
        """

    async def list_workflow_runs(
        self,
        *,
        spaceName: str,
        projectName: str,
        workflowId: str = ...,
        nextToken: str = ...,
        maxResults: int = ...,
        sortBy: Sequence[Mapping[str, Any]] = ...,
    ) -> ListWorkflowRunsResponseTypeDef:
        """
        Retrieves a list of workflow runs of a specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.list_workflow_runs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#list_workflow_runs)
        """

    async def list_workflows(
        self,
        *,
        spaceName: str,
        projectName: str,
        nextToken: str = ...,
        maxResults: int = ...,
        sortBy: Sequence[Mapping[str, Any]] = ...,
    ) -> ListWorkflowsResponseTypeDef:
        """
        Retrieves a list of workflows in a specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.list_workflows)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#list_workflows)
        """

    async def start_dev_environment(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
        ides: Sequence[IdeConfigurationTypeDef] = ...,
        instanceType: InstanceTypeType = ...,
        inactivityTimeoutMinutes: int = ...,
    ) -> StartDevEnvironmentResponseTypeDef:
        """
        Starts a specified Dev Environment and puts it into an active state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.start_dev_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#start_dev_environment)
        """

    async def start_dev_environment_session(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
        sessionConfiguration: DevEnvironmentSessionConfigurationTypeDef,
    ) -> StartDevEnvironmentSessionResponseTypeDef:
        """
        Starts a session for a specified Dev Environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.start_dev_environment_session)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#start_dev_environment_session)
        """

    async def start_workflow_run(
        self, *, spaceName: str, projectName: str, workflowId: str, clientToken: str = ...
    ) -> StartWorkflowRunResponseTypeDef:
        """
        Begins a run of a specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.start_workflow_run)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#start_workflow_run)
        """

    async def stop_dev_environment(
        self, *, spaceName: str, projectName: str, id: str
    ) -> StopDevEnvironmentResponseTypeDef:
        """
        Pauses a specified Dev Environment and places it in a non-running state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.stop_dev_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#stop_dev_environment)
        """

    async def stop_dev_environment_session(
        self, *, spaceName: str, projectName: str, id: str, sessionId: str
    ) -> StopDevEnvironmentSessionResponseTypeDef:
        """
        Stops a session for a specified Dev Environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.stop_dev_environment_session)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#stop_dev_environment_session)
        """

    async def update_dev_environment(
        self,
        *,
        spaceName: str,
        projectName: str,
        id: str,
        alias: str = ...,
        ides: Sequence[IdeConfigurationTypeDef] = ...,
        instanceType: InstanceTypeType = ...,
        inactivityTimeoutMinutes: int = ...,
        clientToken: str = ...,
    ) -> UpdateDevEnvironmentResponseTypeDef:
        """
        Changes one or more values for a Dev Environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.update_dev_environment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#update_dev_environment)
        """

    async def update_project(
        self, *, spaceName: str, name: str, description: str = ...
    ) -> UpdateProjectResponseTypeDef:
        """
        Changes one or more values for a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.update_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#update_project)
        """

    async def update_space(
        self, *, name: str, description: str = ...
    ) -> UpdateSpaceResponseTypeDef:
        """
        Changes one or more values for a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.update_space)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#update_space)
        """

    async def verify_session(self) -> VerifySessionResponseTypeDef:
        """
        Verifies whether the calling user has a valid Amazon CodeCatalyst login and
        session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.verify_session)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#verify_session)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_tokens"]
    ) -> ListAccessTokensPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dev_environment_sessions"]
    ) -> ListDevEnvironmentSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dev_environments"]
    ) -> ListDevEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_event_logs"]) -> ListEventLogsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_source_repositories"]
    ) -> ListSourceRepositoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_source_repository_branches"]
    ) -> ListSourceRepositoryBranchesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_spaces"]) -> ListSpacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workflow_runs"]
    ) -> ListWorkflowRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workflows"]) -> ListWorkflowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/#get_paginator)
        """

    async def __aenter__(self) -> "CodeCatalystClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html#CodeCatalyst.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecatalyst/client/)
        """
