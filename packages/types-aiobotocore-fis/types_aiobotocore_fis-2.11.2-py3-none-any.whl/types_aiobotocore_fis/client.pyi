"""
Type annotations for fis service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_fis.client import FISClient

    session = get_session()
    async with session.create_client("fis") as client:
        client: FISClient
    ```
"""

from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .type_defs import (
    CreateExperimentTemplateActionInputTypeDef,
    CreateExperimentTemplateExperimentOptionsInputTypeDef,
    CreateExperimentTemplateLogConfigurationInputTypeDef,
    CreateExperimentTemplateResponseTypeDef,
    CreateExperimentTemplateStopConditionInputTypeDef,
    CreateExperimentTemplateTargetInputTypeDef,
    CreateTargetAccountConfigurationResponseTypeDef,
    DeleteExperimentTemplateResponseTypeDef,
    DeleteTargetAccountConfigurationResponseTypeDef,
    GetActionResponseTypeDef,
    GetExperimentResponseTypeDef,
    GetExperimentTargetAccountConfigurationResponseTypeDef,
    GetExperimentTemplateResponseTypeDef,
    GetTargetAccountConfigurationResponseTypeDef,
    GetTargetResourceTypeResponseTypeDef,
    ListActionsResponseTypeDef,
    ListExperimentResolvedTargetsResponseTypeDef,
    ListExperimentsResponseTypeDef,
    ListExperimentTargetAccountConfigurationsResponseTypeDef,
    ListExperimentTemplatesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetAccountConfigurationsResponseTypeDef,
    ListTargetResourceTypesResponseTypeDef,
    StartExperimentResponseTypeDef,
    StopExperimentResponseTypeDef,
    UpdateExperimentTemplateActionInputItemTypeDef,
    UpdateExperimentTemplateExperimentOptionsInputTypeDef,
    UpdateExperimentTemplateLogConfigurationInputTypeDef,
    UpdateExperimentTemplateResponseTypeDef,
    UpdateExperimentTemplateStopConditionInputTypeDef,
    UpdateExperimentTemplateTargetInputTypeDef,
    UpdateTargetAccountConfigurationResponseTypeDef,
)

__all__ = ("FISClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class FISClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        FISClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#close)
        """

    async def create_experiment_template(
        self,
        *,
        clientToken: str,
        description: str,
        stopConditions: Sequence[CreateExperimentTemplateStopConditionInputTypeDef],
        actions: Mapping[str, CreateExperimentTemplateActionInputTypeDef],
        roleArn: str,
        targets: Mapping[str, CreateExperimentTemplateTargetInputTypeDef] = ...,
        tags: Mapping[str, str] = ...,
        logConfiguration: CreateExperimentTemplateLogConfigurationInputTypeDef = ...,
        experimentOptions: CreateExperimentTemplateExperimentOptionsInputTypeDef = ...,
    ) -> CreateExperimentTemplateResponseTypeDef:
        """
        Creates an experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.create_experiment_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#create_experiment_template)
        """

    async def create_target_account_configuration(
        self,
        *,
        experimentTemplateId: str,
        accountId: str,
        roleArn: str,
        clientToken: str = ...,
        description: str = ...,
    ) -> CreateTargetAccountConfigurationResponseTypeDef:
        """
        Creates a target account configuration for the experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.create_target_account_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#create_target_account_configuration)
        """

    async def delete_experiment_template(
        self, *, id: str
    ) -> DeleteExperimentTemplateResponseTypeDef:
        """
        Deletes the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.delete_experiment_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#delete_experiment_template)
        """

    async def delete_target_account_configuration(
        self, *, experimentTemplateId: str, accountId: str
    ) -> DeleteTargetAccountConfigurationResponseTypeDef:
        """
        Deletes the specified target account configuration of the experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.delete_target_account_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#delete_target_account_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#generate_presigned_url)
        """

    async def get_action(self, *, id: str) -> GetActionResponseTypeDef:
        """
        Gets information about the specified FIS action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.get_action)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#get_action)
        """

    async def get_experiment(self, *, id: str) -> GetExperimentResponseTypeDef:
        """
        Gets information about the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.get_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#get_experiment)
        """

    async def get_experiment_target_account_configuration(
        self, *, experimentId: str, accountId: str
    ) -> GetExperimentTargetAccountConfigurationResponseTypeDef:
        """
        Gets information about the specified target account configuration of the
        experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.get_experiment_target_account_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#get_experiment_target_account_configuration)
        """

    async def get_experiment_template(self, *, id: str) -> GetExperimentTemplateResponseTypeDef:
        """
        Gets information about the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.get_experiment_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#get_experiment_template)
        """

    async def get_target_account_configuration(
        self, *, experimentTemplateId: str, accountId: str
    ) -> GetTargetAccountConfigurationResponseTypeDef:
        """
        Gets information about the specified target account configuration of the
        experiment
        template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.get_target_account_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#get_target_account_configuration)
        """

    async def get_target_resource_type(
        self, *, resourceType: str
    ) -> GetTargetResourceTypeResponseTypeDef:
        """
        Gets information about the specified resource type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.get_target_resource_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#get_target_resource_type)
        """

    async def list_actions(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListActionsResponseTypeDef:
        """
        Lists the available FIS actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.list_actions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#list_actions)
        """

    async def list_experiment_resolved_targets(
        self,
        *,
        experimentId: str,
        maxResults: int = ...,
        nextToken: str = ...,
        targetName: str = ...,
    ) -> ListExperimentResolvedTargetsResponseTypeDef:
        """
        Lists the resolved targets information of the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.list_experiment_resolved_targets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#list_experiment_resolved_targets)
        """

    async def list_experiment_target_account_configurations(
        self, *, experimentId: str, nextToken: str = ...
    ) -> ListExperimentTargetAccountConfigurationsResponseTypeDef:
        """
        Lists the target account configurations of the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.list_experiment_target_account_configurations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#list_experiment_target_account_configurations)
        """

    async def list_experiment_templates(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListExperimentTemplatesResponseTypeDef:
        """
        Lists your experiment templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.list_experiment_templates)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#list_experiment_templates)
        """

    async def list_experiments(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListExperimentsResponseTypeDef:
        """
        Lists your experiments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.list_experiments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#list_experiments)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#list_tags_for_resource)
        """

    async def list_target_account_configurations(
        self, *, experimentTemplateId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListTargetAccountConfigurationsResponseTypeDef:
        """
        Lists the target account configurations of the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.list_target_account_configurations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#list_target_account_configurations)
        """

    async def list_target_resource_types(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListTargetResourceTypesResponseTypeDef:
        """
        Lists the target resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.list_target_resource_types)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#list_target_resource_types)
        """

    async def start_experiment(
        self, *, clientToken: str, experimentTemplateId: str, tags: Mapping[str, str] = ...
    ) -> StartExperimentResponseTypeDef:
        """
        Starts running an experiment from the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.start_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#start_experiment)
        """

    async def stop_experiment(self, *, id: str) -> StopExperimentResponseTypeDef:
        """
        Stops the specified experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.stop_experiment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#stop_experiment)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Applies the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#tag_resource)
        """

    async def untag_resource(
        self, *, resourceArn: str, tagKeys: Sequence[str] = ...
    ) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#untag_resource)
        """

    async def update_experiment_template(
        self,
        *,
        id: str,
        description: str = ...,
        stopConditions: Sequence[UpdateExperimentTemplateStopConditionInputTypeDef] = ...,
        targets: Mapping[str, UpdateExperimentTemplateTargetInputTypeDef] = ...,
        actions: Mapping[str, UpdateExperimentTemplateActionInputItemTypeDef] = ...,
        roleArn: str = ...,
        logConfiguration: UpdateExperimentTemplateLogConfigurationInputTypeDef = ...,
        experimentOptions: UpdateExperimentTemplateExperimentOptionsInputTypeDef = ...,
    ) -> UpdateExperimentTemplateResponseTypeDef:
        """
        Updates the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.update_experiment_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#update_experiment_template)
        """

    async def update_target_account_configuration(
        self,
        *,
        experimentTemplateId: str,
        accountId: str,
        roleArn: str = ...,
        description: str = ...,
    ) -> UpdateTargetAccountConfigurationResponseTypeDef:
        """
        Updates the target account configuration for the specified experiment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client.update_target_account_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/#update_target_account_configuration)
        """

    async def __aenter__(self) -> "FISClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html#FIS.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/client/)
        """
