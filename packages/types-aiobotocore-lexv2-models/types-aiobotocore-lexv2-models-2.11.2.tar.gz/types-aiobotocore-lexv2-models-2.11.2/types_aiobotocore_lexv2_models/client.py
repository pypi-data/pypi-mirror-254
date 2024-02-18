"""
Type annotations for lexv2-models service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_lexv2_models.client import LexModelsV2Client

    session = get_session()
    async with session.create_client("lexv2-models") as client:
        client: LexModelsV2Client
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    BotTypeType,
    EffectType,
    ImportExportFileFormatType,
    MergeStrategyType,
    SearchOrderType,
    TestExecutionApiModeType,
    TestExecutionModalityType,
)
from .type_defs import (
    AggregatedUtterancesFilterTypeDef,
    AggregatedUtterancesSortByTypeDef,
    AnalyticsBinBySpecificationTypeDef,
    AnalyticsIntentFilterTypeDef,
    AnalyticsIntentGroupBySpecificationTypeDef,
    AnalyticsIntentMetricTypeDef,
    AnalyticsIntentStageFilterTypeDef,
    AnalyticsIntentStageGroupBySpecificationTypeDef,
    AnalyticsIntentStageMetricTypeDef,
    AnalyticsPathFilterTypeDef,
    AnalyticsSessionFilterTypeDef,
    AnalyticsSessionGroupBySpecificationTypeDef,
    AnalyticsSessionMetricTypeDef,
    AnalyticsUtteranceAttributeTypeDef,
    AnalyticsUtteranceFilterTypeDef,
    AnalyticsUtteranceGroupBySpecificationTypeDef,
    AnalyticsUtteranceMetricTypeDef,
    AssociatedTranscriptFilterTypeDef,
    BatchCreateCustomVocabularyItemResponseTypeDef,
    BatchDeleteCustomVocabularyItemResponseTypeDef,
    BatchUpdateCustomVocabularyItemResponseTypeDef,
    BotAliasLocaleSettingsTypeDef,
    BotFilterTypeDef,
    BotLocaleFilterTypeDef,
    BotLocaleSortByTypeDef,
    BotMemberTypeDef,
    BotSortByTypeDef,
    BotVersionLocaleDetailsTypeDef,
    BotVersionSortByTypeDef,
    BuildBotLocaleResponseTypeDef,
    BuiltInIntentSortByTypeDef,
    BuiltInSlotTypeSortByTypeDef,
    CompositeSlotTypeSettingTypeDef,
    ConversationLogSettingsTypeDef,
    CreateBotAliasResponseTypeDef,
    CreateBotLocaleResponseTypeDef,
    CreateBotResponseTypeDef,
    CreateBotVersionResponseTypeDef,
    CreateExportResponseTypeDef,
    CreateIntentResponseTypeDef,
    CreateResourcePolicyResponseTypeDef,
    CreateResourcePolicyStatementResponseTypeDef,
    CreateSlotResponseTypeDef,
    CreateSlotTypeResponseTypeDef,
    CreateTestSetDiscrepancyReportResponseTypeDef,
    CreateUploadUrlResponseTypeDef,
    CustomVocabularyEntryIdTypeDef,
    CustomVocabularyItemTypeDef,
    DataPrivacyTypeDef,
    DeleteBotAliasResponseTypeDef,
    DeleteBotLocaleResponseTypeDef,
    DeleteBotResponseTypeDef,
    DeleteBotVersionResponseTypeDef,
    DeleteCustomVocabularyResponseTypeDef,
    DeleteExportResponseTypeDef,
    DeleteImportResponseTypeDef,
    DeleteResourcePolicyResponseTypeDef,
    DeleteResourcePolicyStatementResponseTypeDef,
    DescribeBotAliasResponseTypeDef,
    DescribeBotLocaleResponseTypeDef,
    DescribeBotRecommendationResponseTypeDef,
    DescribeBotResourceGenerationResponseTypeDef,
    DescribeBotResponseTypeDef,
    DescribeBotVersionResponseTypeDef,
    DescribeCustomVocabularyMetadataResponseTypeDef,
    DescribeExportResponseTypeDef,
    DescribeImportResponseTypeDef,
    DescribeIntentResponseTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DescribeSlotResponseTypeDef,
    DescribeSlotTypeResponseTypeDef,
    DescribeTestExecutionResponseTypeDef,
    DescribeTestSetDiscrepancyReportResponseTypeDef,
    DescribeTestSetGenerationResponseTypeDef,
    DescribeTestSetResponseTypeDef,
    DialogCodeHookSettingsTypeDef,
    EmptyResponseMetadataTypeDef,
    EncryptionSettingTypeDef,
    ExportFilterTypeDef,
    ExportResourceSpecificationTypeDef,
    ExportSortByTypeDef,
    ExternalSourceSettingTypeDef,
    FulfillmentCodeHookSettingsTypeDef,
    GenerateBotElementResponseTypeDef,
    GenerationSortByTypeDef,
    GenerativeAISettingsTypeDef,
    GetTestExecutionArtifactsUrlResponseTypeDef,
    ImportFilterTypeDef,
    ImportResourceSpecificationTypeDef,
    ImportSortByTypeDef,
    InitialResponseSettingTypeDef,
    InputContextTypeDef,
    IntentClosingSettingTypeDef,
    IntentConfirmationSettingTypeDef,
    IntentFilterTypeDef,
    IntentSortByTypeDef,
    KendraConfigurationTypeDef,
    ListAggregatedUtterancesResponseTypeDef,
    ListBotAliasesResponseTypeDef,
    ListBotLocalesResponseTypeDef,
    ListBotRecommendationsResponseTypeDef,
    ListBotResourceGenerationsResponseTypeDef,
    ListBotsResponseTypeDef,
    ListBotVersionsResponseTypeDef,
    ListBuiltInIntentsResponseTypeDef,
    ListBuiltInSlotTypesResponseTypeDef,
    ListCustomVocabularyItemsResponseTypeDef,
    ListExportsResponseTypeDef,
    ListImportsResponseTypeDef,
    ListIntentMetricsResponseTypeDef,
    ListIntentPathsResponseTypeDef,
    ListIntentsResponseTypeDef,
    ListIntentStageMetricsResponseTypeDef,
    ListRecommendedIntentsResponseTypeDef,
    ListSessionAnalyticsDataResponseTypeDef,
    ListSessionMetricsResponseTypeDef,
    ListSlotsResponseTypeDef,
    ListSlotTypesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTestExecutionResultItemsResponseTypeDef,
    ListTestExecutionsResponseTypeDef,
    ListTestSetRecordsResponseTypeDef,
    ListTestSetsResponseTypeDef,
    ListUtteranceAnalyticsDataResponseTypeDef,
    ListUtteranceMetricsResponseTypeDef,
    MultipleValuesSettingTypeDef,
    NewCustomVocabularyItemTypeDef,
    ObfuscationSettingTypeDef,
    OutputContextTypeDef,
    PrincipalTypeDef,
    SampleUtteranceTypeDef,
    SearchAssociatedTranscriptsResponseTypeDef,
    SentimentAnalysisSettingsTypeDef,
    SessionDataSortByTypeDef,
    SlotFilterTypeDef,
    SlotPriorityTypeDef,
    SlotSortByTypeDef,
    SlotTypeFilterTypeDef,
    SlotTypeSortByTypeDef,
    SlotTypeValueTypeDef,
    SlotValueElicitationSettingTypeDef,
    SlotValueSelectionSettingTypeDef,
    StartBotRecommendationResponseTypeDef,
    StartBotResourceGenerationResponseTypeDef,
    StartImportResponseTypeDef,
    StartTestExecutionResponseTypeDef,
    StartTestSetGenerationResponseTypeDef,
    StopBotRecommendationResponseTypeDef,
    SubSlotSettingTypeDef,
    TestExecutionResultFilterByTypeDef,
    TestExecutionSortByTypeDef,
    TestExecutionTargetTypeDef,
    TestSetDiscrepancyReportResourceTargetTypeDef,
    TestSetGenerationDataSourceTypeDef,
    TestSetSortByTypeDef,
    TestSetStorageLocationTypeDef,
    TimestampTypeDef,
    TranscriptSourceSettingTypeDef,
    UpdateBotAliasResponseTypeDef,
    UpdateBotLocaleResponseTypeDef,
    UpdateBotRecommendationResponseTypeDef,
    UpdateBotResponseTypeDef,
    UpdateExportResponseTypeDef,
    UpdateIntentResponseTypeDef,
    UpdateResourcePolicyResponseTypeDef,
    UpdateSlotResponseTypeDef,
    UpdateSlotTypeResponseTypeDef,
    UpdateTestSetResponseTypeDef,
    UtteranceAggregationDurationTypeDef,
    UtteranceDataSortByTypeDef,
    VoiceSettingsTypeDef,
)
from .waiter import (
    BotAliasAvailableWaiter,
    BotAvailableWaiter,
    BotExportCompletedWaiter,
    BotImportCompletedWaiter,
    BotLocaleBuiltWaiter,
    BotLocaleCreatedWaiter,
    BotLocaleExpressTestingAvailableWaiter,
    BotVersionAvailableWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("LexModelsV2Client",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LexModelsV2Client(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LexModelsV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#exceptions)
        """

    async def batch_create_custom_vocabulary_item(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        customVocabularyItemList: Sequence[NewCustomVocabularyItemTypeDef],
    ) -> BatchCreateCustomVocabularyItemResponseTypeDef:
        """
        Create a batch of custom vocabulary items for a given bot locale's custom
        vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.batch_create_custom_vocabulary_item)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#batch_create_custom_vocabulary_item)
        """

    async def batch_delete_custom_vocabulary_item(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        customVocabularyItemList: Sequence[CustomVocabularyEntryIdTypeDef],
    ) -> BatchDeleteCustomVocabularyItemResponseTypeDef:
        """
        Delete a batch of custom vocabulary items for a given bot locale's custom
        vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.batch_delete_custom_vocabulary_item)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#batch_delete_custom_vocabulary_item)
        """

    async def batch_update_custom_vocabulary_item(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        customVocabularyItemList: Sequence[CustomVocabularyItemTypeDef],
    ) -> BatchUpdateCustomVocabularyItemResponseTypeDef:
        """
        Update a batch of custom vocabulary items for a given bot locale's custom
        vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.batch_update_custom_vocabulary_item)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#batch_update_custom_vocabulary_item)
        """

    async def build_bot_locale(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> BuildBotLocaleResponseTypeDef:
        """
        Builds a bot, its intents, and its slot types into a specific locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.build_bot_locale)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#build_bot_locale)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#close)
        """

    async def create_bot(
        self,
        *,
        botName: str,
        roleArn: str,
        dataPrivacy: DataPrivacyTypeDef,
        idleSessionTTLInSeconds: int,
        description: str = ...,
        botTags: Mapping[str, str] = ...,
        testBotAliasTags: Mapping[str, str] = ...,
        botType: BotTypeType = ...,
        botMembers: Sequence[BotMemberTypeDef] = ...,
    ) -> CreateBotResponseTypeDef:
        """
        Creates an Amazon Lex conversational bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#create_bot)
        """

    async def create_bot_alias(
        self,
        *,
        botAliasName: str,
        botId: str,
        description: str = ...,
        botVersion: str = ...,
        botAliasLocaleSettings: Mapping[str, BotAliasLocaleSettingsTypeDef] = ...,
        conversationLogSettings: ConversationLogSettingsTypeDef = ...,
        sentimentAnalysisSettings: SentimentAnalysisSettingsTypeDef = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateBotAliasResponseTypeDef:
        """
        Creates an alias for the specified version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_alias)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#create_bot_alias)
        """

    async def create_bot_locale(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        nluIntentConfidenceThreshold: float,
        description: str = ...,
        voiceSettings: VoiceSettingsTypeDef = ...,
        generativeAISettings: GenerativeAISettingsTypeDef = ...,
    ) -> CreateBotLocaleResponseTypeDef:
        """
        Creates a locale in the bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_locale)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#create_bot_locale)
        """

    async def create_bot_version(
        self,
        *,
        botId: str,
        botVersionLocaleSpecification: Mapping[str, BotVersionLocaleDetailsTypeDef],
        description: str = ...,
    ) -> CreateBotVersionResponseTypeDef:
        """
        Creates an immutable version of the bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#create_bot_version)
        """

    async def create_export(
        self,
        *,
        resourceSpecification: ExportResourceSpecificationTypeDef,
        fileFormat: ImportExportFileFormatType,
        filePassword: str = ...,
    ) -> CreateExportResponseTypeDef:
        """
        Creates a zip archive containing the contents of a bot or a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#create_export)
        """

    async def create_intent(
        self,
        *,
        intentName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = ...,
        parentIntentSignature: str = ...,
        sampleUtterances: Sequence[SampleUtteranceTypeDef] = ...,
        dialogCodeHook: DialogCodeHookSettingsTypeDef = ...,
        fulfillmentCodeHook: FulfillmentCodeHookSettingsTypeDef = ...,
        intentConfirmationSetting: IntentConfirmationSettingTypeDef = ...,
        intentClosingSetting: IntentClosingSettingTypeDef = ...,
        inputContexts: Sequence[InputContextTypeDef] = ...,
        outputContexts: Sequence[OutputContextTypeDef] = ...,
        kendraConfiguration: KendraConfigurationTypeDef = ...,
        initialResponseSetting: InitialResponseSettingTypeDef = ...,
    ) -> CreateIntentResponseTypeDef:
        """
        Creates an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_intent)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#create_intent)
        """

    async def create_resource_policy(
        self, *, resourceArn: str, policy: str
    ) -> CreateResourcePolicyResponseTypeDef:
        """
        Creates a new resource policy with the specified policy statements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_resource_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#create_resource_policy)
        """

    async def create_resource_policy_statement(
        self,
        *,
        resourceArn: str,
        statementId: str,
        effect: EffectType,
        principal: Sequence[PrincipalTypeDef],
        action: Sequence[str],
        condition: Mapping[str, Mapping[str, str]] = ...,
        expectedRevisionId: str = ...,
    ) -> CreateResourcePolicyStatementResponseTypeDef:
        """
        Adds a new resource policy statement to a bot or bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_resource_policy_statement)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#create_resource_policy_statement)
        """

    async def create_slot(
        self,
        *,
        slotName: str,
        valueElicitationSetting: SlotValueElicitationSettingTypeDef,
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        description: str = ...,
        slotTypeId: str = ...,
        obfuscationSetting: ObfuscationSettingTypeDef = ...,
        multipleValuesSetting: MultipleValuesSettingTypeDef = ...,
        subSlotSetting: SubSlotSettingTypeDef = ...,
    ) -> CreateSlotResponseTypeDef:
        """
        Creates a slot in an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#create_slot)
        """

    async def create_slot_type(
        self,
        *,
        slotTypeName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = ...,
        slotTypeValues: Sequence[SlotTypeValueTypeDef] = ...,
        valueSelectionSetting: SlotValueSelectionSettingTypeDef = ...,
        parentSlotTypeSignature: str = ...,
        externalSourceSetting: ExternalSourceSettingTypeDef = ...,
        compositeSlotTypeSetting: CompositeSlotTypeSettingTypeDef = ...,
    ) -> CreateSlotTypeResponseTypeDef:
        """
        Creates a custom slot type To create a custom slot type, specify a name for the
        slot type and a set of enumeration values, the values that a slot of this type
        can
        assume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#create_slot_type)
        """

    async def create_test_set_discrepancy_report(
        self, *, testSetId: str, target: TestSetDiscrepancyReportResourceTargetTypeDef
    ) -> CreateTestSetDiscrepancyReportResponseTypeDef:
        """
        Create a report that describes the differences between the bot and the test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_test_set_discrepancy_report)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#create_test_set_discrepancy_report)
        """

    async def create_upload_url(self) -> CreateUploadUrlResponseTypeDef:
        """
        Gets a pre-signed S3 write URL that you use to upload the zip archive when
        importing a bot or a bot
        locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_upload_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#create_upload_url)
        """

    async def delete_bot(
        self, *, botId: str, skipResourceInUseCheck: bool = ...
    ) -> DeleteBotResponseTypeDef:
        """
        Deletes all versions of a bot, including the `Draft` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_bot)
        """

    async def delete_bot_alias(
        self, *, botAliasId: str, botId: str, skipResourceInUseCheck: bool = ...
    ) -> DeleteBotAliasResponseTypeDef:
        """
        Deletes the specified bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_alias)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_bot_alias)
        """

    async def delete_bot_locale(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> DeleteBotLocaleResponseTypeDef:
        """
        Removes a locale from a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_locale)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_bot_locale)
        """

    async def delete_bot_version(
        self, *, botId: str, botVersion: str, skipResourceInUseCheck: bool = ...
    ) -> DeleteBotVersionResponseTypeDef:
        """
        Deletes a specific version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_bot_version)
        """

    async def delete_custom_vocabulary(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> DeleteCustomVocabularyResponseTypeDef:
        """
        Removes a custom vocabulary from the specified locale in the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_custom_vocabulary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_custom_vocabulary)
        """

    async def delete_export(self, *, exportId: str) -> DeleteExportResponseTypeDef:
        """
        Removes a previous export and the associated files stored in an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_export)
        """

    async def delete_import(self, *, importId: str) -> DeleteImportResponseTypeDef:
        """
        Removes a previous import and the associated file stored in an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_import)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_import)
        """

    async def delete_intent(
        self, *, intentId: str, botId: str, botVersion: str, localeId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_intent)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_intent)
        """

    async def delete_resource_policy(
        self, *, resourceArn: str, expectedRevisionId: str = ...
    ) -> DeleteResourcePolicyResponseTypeDef:
        """
        Removes an existing policy from a bot or bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_resource_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_resource_policy)
        """

    async def delete_resource_policy_statement(
        self, *, resourceArn: str, statementId: str, expectedRevisionId: str = ...
    ) -> DeleteResourcePolicyStatementResponseTypeDef:
        """
        Deletes a policy statement from a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_resource_policy_statement)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_resource_policy_statement)
        """

    async def delete_slot(
        self, *, slotId: str, botId: str, botVersion: str, localeId: str, intentId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified slot from an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_slot)
        """

    async def delete_slot_type(
        self,
        *,
        slotTypeId: str,
        botId: str,
        botVersion: str,
        localeId: str,
        skipResourceInUseCheck: bool = ...,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a slot type from a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_slot_type)
        """

    async def delete_test_set(self, *, testSetId: str) -> EmptyResponseMetadataTypeDef:
        """
        The action to delete the selected test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_test_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_test_set)
        """

    async def delete_utterances(
        self, *, botId: str, localeId: str = ..., sessionId: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes stored utterances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_utterances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#delete_utterances)
        """

    async def describe_bot(self, *, botId: str) -> DescribeBotResponseTypeDef:
        """
        Provides metadata information about a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_bot)
        """

    async def describe_bot_alias(
        self, *, botAliasId: str, botId: str
    ) -> DescribeBotAliasResponseTypeDef:
        """
        Get information about a specific bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_alias)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_bot_alias)
        """

    async def describe_bot_locale(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> DescribeBotLocaleResponseTypeDef:
        """
        Describes the settings that a bot has for a specific locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_locale)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_bot_locale)
        """

    async def describe_bot_recommendation(
        self, *, botId: str, botVersion: str, localeId: str, botRecommendationId: str
    ) -> DescribeBotRecommendationResponseTypeDef:
        """
        Provides metadata information about a bot recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_recommendation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_bot_recommendation)
        """

    async def describe_bot_resource_generation(
        self, *, botId: str, botVersion: str, localeId: str, generationId: str
    ) -> DescribeBotResourceGenerationResponseTypeDef:
        """
        Returns information about a request to generate a bot through natural language
        description, made through the `StartBotResource`
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_resource_generation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_bot_resource_generation)
        """

    async def describe_bot_version(
        self, *, botId: str, botVersion: str
    ) -> DescribeBotVersionResponseTypeDef:
        """
        Provides metadata about a version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_bot_version)
        """

    async def describe_custom_vocabulary_metadata(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> DescribeCustomVocabularyMetadataResponseTypeDef:
        """
        Provides metadata information about a custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_custom_vocabulary_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_custom_vocabulary_metadata)
        """

    async def describe_export(self, *, exportId: str) -> DescribeExportResponseTypeDef:
        """
        Gets information about a specific export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_export)
        """

    async def describe_import(self, *, importId: str) -> DescribeImportResponseTypeDef:
        """
        Gets information about a specific import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_import)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_import)
        """

    async def describe_intent(
        self, *, intentId: str, botId: str, botVersion: str, localeId: str
    ) -> DescribeIntentResponseTypeDef:
        """
        Returns metadata about an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_intent)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_intent)
        """

    async def describe_resource_policy(
        self, *, resourceArn: str
    ) -> DescribeResourcePolicyResponseTypeDef:
        """
        Gets the resource policy and policy revision for a bot or bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_resource_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_resource_policy)
        """

    async def describe_slot(
        self, *, slotId: str, botId: str, botVersion: str, localeId: str, intentId: str
    ) -> DescribeSlotResponseTypeDef:
        """
        Gets metadata information about a slot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_slot)
        """

    async def describe_slot_type(
        self, *, slotTypeId: str, botId: str, botVersion: str, localeId: str
    ) -> DescribeSlotTypeResponseTypeDef:
        """
        Gets metadata information about a slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_slot_type)
        """

    async def describe_test_execution(
        self, *, testExecutionId: str
    ) -> DescribeTestExecutionResponseTypeDef:
        """
        Gets metadata information about the test execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_test_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_test_execution)
        """

    async def describe_test_set(self, *, testSetId: str) -> DescribeTestSetResponseTypeDef:
        """
        Gets metadata information about the test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_test_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_test_set)
        """

    async def describe_test_set_discrepancy_report(
        self, *, testSetDiscrepancyReportId: str
    ) -> DescribeTestSetDiscrepancyReportResponseTypeDef:
        """
        Gets metadata information about the test set discrepancy report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_test_set_discrepancy_report)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_test_set_discrepancy_report)
        """

    async def describe_test_set_generation(
        self, *, testSetGenerationId: str
    ) -> DescribeTestSetGenerationResponseTypeDef:
        """
        Gets metadata information about the test set generation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_test_set_generation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#describe_test_set_generation)
        """

    async def generate_bot_element(
        self, *, intentId: str, botId: str, botVersion: str, localeId: str
    ) -> GenerateBotElementResponseTypeDef:
        """
        Generates sample utterances for an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.generate_bot_element)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#generate_bot_element)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#generate_presigned_url)
        """

    async def get_test_execution_artifacts_url(
        self, *, testExecutionId: str
    ) -> GetTestExecutionArtifactsUrlResponseTypeDef:
        """
        The pre-signed Amazon S3 URL to download the test execution result artifacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_test_execution_artifacts_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#get_test_execution_artifacts_url)
        """

    async def list_aggregated_utterances(
        self,
        *,
        botId: str,
        localeId: str,
        aggregationDuration: UtteranceAggregationDurationTypeDef,
        botAliasId: str = ...,
        botVersion: str = ...,
        sortBy: AggregatedUtterancesSortByTypeDef = ...,
        filters: Sequence[AggregatedUtterancesFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListAggregatedUtterancesResponseTypeDef:
        """
        Provides a list of utterances that users have sent to the bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_aggregated_utterances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_aggregated_utterances)
        """

    async def list_bot_aliases(
        self, *, botId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListBotAliasesResponseTypeDef:
        """
        Gets a list of aliases for the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_aliases)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_bot_aliases)
        """

    async def list_bot_locales(
        self,
        *,
        botId: str,
        botVersion: str,
        sortBy: BotLocaleSortByTypeDef = ...,
        filters: Sequence[BotLocaleFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListBotLocalesResponseTypeDef:
        """
        Gets a list of locales for the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_locales)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_bot_locales)
        """

    async def list_bot_recommendations(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListBotRecommendationsResponseTypeDef:
        """
        Get a list of bot recommendations that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_recommendations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_bot_recommendations)
        """

    async def list_bot_resource_generations(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: GenerationSortByTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListBotResourceGenerationsResponseTypeDef:
        """
        Lists the generation requests made for a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_resource_generations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_bot_resource_generations)
        """

    async def list_bot_versions(
        self,
        *,
        botId: str,
        sortBy: BotVersionSortByTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListBotVersionsResponseTypeDef:
        """
        Gets information about all of the versions of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_bot_versions)
        """

    async def list_bots(
        self,
        *,
        sortBy: BotSortByTypeDef = ...,
        filters: Sequence[BotFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListBotsResponseTypeDef:
        """
        Gets a list of available bots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bots)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_bots)
        """

    async def list_built_in_intents(
        self,
        *,
        localeId: str,
        sortBy: BuiltInIntentSortByTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListBuiltInIntentsResponseTypeDef:
        """
        Gets a list of built-in intents provided by Amazon Lex that you can use in your
        bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_intents)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_built_in_intents)
        """

    async def list_built_in_slot_types(
        self,
        *,
        localeId: str,
        sortBy: BuiltInSlotTypeSortByTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListBuiltInSlotTypesResponseTypeDef:
        """
        Gets a list of built-in slot types that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_slot_types)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_built_in_slot_types)
        """

    async def list_custom_vocabulary_items(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListCustomVocabularyItemsResponseTypeDef:
        """
        Paginated list of custom vocabulary items for a given bot locale's custom
        vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_custom_vocabulary_items)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_custom_vocabulary_items)
        """

    async def list_exports(
        self,
        *,
        botId: str = ...,
        botVersion: str = ...,
        sortBy: ExportSortByTypeDef = ...,
        filters: Sequence[ExportFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        localeId: str = ...,
    ) -> ListExportsResponseTypeDef:
        """
        Lists the exports for a bot, bot locale, or custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_exports)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_exports)
        """

    async def list_imports(
        self,
        *,
        botId: str = ...,
        botVersion: str = ...,
        sortBy: ImportSortByTypeDef = ...,
        filters: Sequence[ImportFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        localeId: str = ...,
    ) -> ListImportsResponseTypeDef:
        """
        Lists the imports for a bot, bot locale, or custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_imports)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_imports)
        """

    async def list_intent_metrics(
        self,
        *,
        botId: str,
        startDateTime: TimestampTypeDef,
        endDateTime: TimestampTypeDef,
        metrics: Sequence[AnalyticsIntentMetricTypeDef],
        binBy: Sequence[AnalyticsBinBySpecificationTypeDef] = ...,
        groupBy: Sequence[AnalyticsIntentGroupBySpecificationTypeDef] = ...,
        filters: Sequence[AnalyticsIntentFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListIntentMetricsResponseTypeDef:
        """
        Retrieves summary metrics for the intents in your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_intent_metrics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_intent_metrics)
        """

    async def list_intent_paths(
        self,
        *,
        botId: str,
        startDateTime: TimestampTypeDef,
        endDateTime: TimestampTypeDef,
        intentPath: str,
        filters: Sequence[AnalyticsPathFilterTypeDef] = ...,
    ) -> ListIntentPathsResponseTypeDef:
        """
        Retrieves summary statistics for a path of intents that users take over
        sessions with your
        bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_intent_paths)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_intent_paths)
        """

    async def list_intent_stage_metrics(
        self,
        *,
        botId: str,
        startDateTime: TimestampTypeDef,
        endDateTime: TimestampTypeDef,
        metrics: Sequence[AnalyticsIntentStageMetricTypeDef],
        binBy: Sequence[AnalyticsBinBySpecificationTypeDef] = ...,
        groupBy: Sequence[AnalyticsIntentStageGroupBySpecificationTypeDef] = ...,
        filters: Sequence[AnalyticsIntentStageFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListIntentStageMetricsResponseTypeDef:
        """
        Retrieves summary metrics for the stages within intents in your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_intent_stage_metrics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_intent_stage_metrics)
        """

    async def list_intents(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: IntentSortByTypeDef = ...,
        filters: Sequence[IntentFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListIntentsResponseTypeDef:
        """
        Get a list of intents that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_intents)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_intents)
        """

    async def list_recommended_intents(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        botRecommendationId: str,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> ListRecommendedIntentsResponseTypeDef:
        """
        Gets a list of recommended intents provided by the bot recommendation that you
        can use in your
        bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_recommended_intents)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_recommended_intents)
        """

    async def list_session_analytics_data(
        self,
        *,
        botId: str,
        startDateTime: TimestampTypeDef,
        endDateTime: TimestampTypeDef,
        sortBy: SessionDataSortByTypeDef = ...,
        filters: Sequence[AnalyticsSessionFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListSessionAnalyticsDataResponseTypeDef:
        """
        Retrieves a list of metadata for individual user sessions with your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_session_analytics_data)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_session_analytics_data)
        """

    async def list_session_metrics(
        self,
        *,
        botId: str,
        startDateTime: TimestampTypeDef,
        endDateTime: TimestampTypeDef,
        metrics: Sequence[AnalyticsSessionMetricTypeDef],
        binBy: Sequence[AnalyticsBinBySpecificationTypeDef] = ...,
        groupBy: Sequence[AnalyticsSessionGroupBySpecificationTypeDef] = ...,
        filters: Sequence[AnalyticsSessionFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListSessionMetricsResponseTypeDef:
        """
        Retrieves summary metrics for the user sessions with your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_session_metrics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_session_metrics)
        """

    async def list_slot_types(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: SlotTypeSortByTypeDef = ...,
        filters: Sequence[SlotTypeFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListSlotTypesResponseTypeDef:
        """
        Gets a list of slot types that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_slot_types)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_slot_types)
        """

    async def list_slots(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        sortBy: SlotSortByTypeDef = ...,
        filters: Sequence[SlotFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListSlotsResponseTypeDef:
        """
        Gets a list of slots that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_slots)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_slots)
        """

    async def list_tags_for_resource(
        self, *, resourceARN: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_tags_for_resource)
        """

    async def list_test_execution_result_items(
        self,
        *,
        testExecutionId: str,
        resultFilterBy: TestExecutionResultFilterByTypeDef,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListTestExecutionResultItemsResponseTypeDef:
        """
        Gets a list of test execution result items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_test_execution_result_items)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_test_execution_result_items)
        """

    async def list_test_executions(
        self,
        *,
        sortBy: TestExecutionSortByTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListTestExecutionsResponseTypeDef:
        """
        The list of test set executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_test_executions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_test_executions)
        """

    async def list_test_set_records(
        self, *, testSetId: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListTestSetRecordsResponseTypeDef:
        """
        The list of test set records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_test_set_records)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_test_set_records)
        """

    async def list_test_sets(
        self, *, sortBy: TestSetSortByTypeDef = ..., maxResults: int = ..., nextToken: str = ...
    ) -> ListTestSetsResponseTypeDef:
        """
        The list of the test sets See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListTestSets).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_test_sets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_test_sets)
        """

    async def list_utterance_analytics_data(
        self,
        *,
        botId: str,
        startDateTime: TimestampTypeDef,
        endDateTime: TimestampTypeDef,
        sortBy: UtteranceDataSortByTypeDef = ...,
        filters: Sequence[AnalyticsUtteranceFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListUtteranceAnalyticsDataResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_utterance_analytics_data)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_utterance_analytics_data)
        """

    async def list_utterance_metrics(
        self,
        *,
        botId: str,
        startDateTime: TimestampTypeDef,
        endDateTime: TimestampTypeDef,
        metrics: Sequence[AnalyticsUtteranceMetricTypeDef],
        binBy: Sequence[AnalyticsBinBySpecificationTypeDef] = ...,
        groupBy: Sequence[AnalyticsUtteranceGroupBySpecificationTypeDef] = ...,
        attributes: Sequence[AnalyticsUtteranceAttributeTypeDef] = ...,
        filters: Sequence[AnalyticsUtteranceFilterTypeDef] = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> ListUtteranceMetricsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_utterance_metrics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#list_utterance_metrics)
        """

    async def search_associated_transcripts(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        botRecommendationId: str,
        filters: Sequence[AssociatedTranscriptFilterTypeDef],
        searchOrder: SearchOrderType = ...,
        maxResults: int = ...,
        nextIndex: int = ...,
    ) -> SearchAssociatedTranscriptsResponseTypeDef:
        """
        Search for associated transcripts that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.search_associated_transcripts)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#search_associated_transcripts)
        """

    async def start_bot_recommendation(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        transcriptSourceSetting: TranscriptSourceSettingTypeDef,
        encryptionSetting: EncryptionSettingTypeDef = ...,
    ) -> StartBotRecommendationResponseTypeDef:
        """
        Use this to provide your transcript data, and to start the bot recommendation
        process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.start_bot_recommendation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#start_bot_recommendation)
        """

    async def start_bot_resource_generation(
        self, *, generationInputPrompt: str, botId: str, botVersion: str, localeId: str
    ) -> StartBotResourceGenerationResponseTypeDef:
        """
        Starts a request for the descriptive bot builder to generate a bot locale
        configuration based on the prompt you provide
        it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.start_bot_resource_generation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#start_bot_resource_generation)
        """

    async def start_import(
        self,
        *,
        importId: str,
        resourceSpecification: ImportResourceSpecificationTypeDef,
        mergeStrategy: MergeStrategyType,
        filePassword: str = ...,
    ) -> StartImportResponseTypeDef:
        """
        Starts importing a bot, bot locale, or custom vocabulary from a zip archive
        that you uploaded to an S3
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.start_import)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#start_import)
        """

    async def start_test_execution(
        self,
        *,
        testSetId: str,
        target: TestExecutionTargetTypeDef,
        apiMode: TestExecutionApiModeType,
        testExecutionModality: TestExecutionModalityType = ...,
    ) -> StartTestExecutionResponseTypeDef:
        """
        The action to start test set execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.start_test_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#start_test_execution)
        """

    async def start_test_set_generation(
        self,
        *,
        testSetName: str,
        storageLocation: TestSetStorageLocationTypeDef,
        generationDataSource: TestSetGenerationDataSourceTypeDef,
        roleArn: str,
        description: str = ...,
        testSetTags: Mapping[str, str] = ...,
    ) -> StartTestSetGenerationResponseTypeDef:
        """
        The action to start the generation of test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.start_test_set_generation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#start_test_set_generation)
        """

    async def stop_bot_recommendation(
        self, *, botId: str, botVersion: str, localeId: str, botRecommendationId: str
    ) -> StopBotRecommendationResponseTypeDef:
        """
        Stop an already running Bot Recommendation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.stop_bot_recommendation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#stop_bot_recommendation)
        """

    async def tag_resource(self, *, resourceARN: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceARN: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes tags from a bot, bot alias, or bot channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#untag_resource)
        """

    async def update_bot(
        self,
        *,
        botId: str,
        botName: str,
        roleArn: str,
        dataPrivacy: DataPrivacyTypeDef,
        idleSessionTTLInSeconds: int,
        description: str = ...,
        botType: BotTypeType = ...,
        botMembers: Sequence[BotMemberTypeDef] = ...,
    ) -> UpdateBotResponseTypeDef:
        """
        Updates the configuration of an existing bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#update_bot)
        """

    async def update_bot_alias(
        self,
        *,
        botAliasId: str,
        botAliasName: str,
        botId: str,
        description: str = ...,
        botVersion: str = ...,
        botAliasLocaleSettings: Mapping[str, BotAliasLocaleSettingsTypeDef] = ...,
        conversationLogSettings: ConversationLogSettingsTypeDef = ...,
        sentimentAnalysisSettings: SentimentAnalysisSettingsTypeDef = ...,
    ) -> UpdateBotAliasResponseTypeDef:
        """
        Updates the configuration of an existing bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_alias)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#update_bot_alias)
        """

    async def update_bot_locale(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        nluIntentConfidenceThreshold: float,
        description: str = ...,
        voiceSettings: VoiceSettingsTypeDef = ...,
        generativeAISettings: GenerativeAISettingsTypeDef = ...,
    ) -> UpdateBotLocaleResponseTypeDef:
        """
        Updates the settings that a bot has for a specific locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_locale)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#update_bot_locale)
        """

    async def update_bot_recommendation(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        botRecommendationId: str,
        encryptionSetting: EncryptionSettingTypeDef,
    ) -> UpdateBotRecommendationResponseTypeDef:
        """
        Updates an existing bot recommendation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_recommendation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#update_bot_recommendation)
        """

    async def update_export(
        self, *, exportId: str, filePassword: str = ...
    ) -> UpdateExportResponseTypeDef:
        """
        Updates the password used to protect an export zip archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_export)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#update_export)
        """

    async def update_intent(
        self,
        *,
        intentId: str,
        intentName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = ...,
        parentIntentSignature: str = ...,
        sampleUtterances: Sequence[SampleUtteranceTypeDef] = ...,
        dialogCodeHook: DialogCodeHookSettingsTypeDef = ...,
        fulfillmentCodeHook: FulfillmentCodeHookSettingsTypeDef = ...,
        slotPriorities: Sequence[SlotPriorityTypeDef] = ...,
        intentConfirmationSetting: IntentConfirmationSettingTypeDef = ...,
        intentClosingSetting: IntentClosingSettingTypeDef = ...,
        inputContexts: Sequence[InputContextTypeDef] = ...,
        outputContexts: Sequence[OutputContextTypeDef] = ...,
        kendraConfiguration: KendraConfigurationTypeDef = ...,
        initialResponseSetting: InitialResponseSettingTypeDef = ...,
    ) -> UpdateIntentResponseTypeDef:
        """
        Updates the settings for an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_intent)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#update_intent)
        """

    async def update_resource_policy(
        self, *, resourceArn: str, policy: str, expectedRevisionId: str = ...
    ) -> UpdateResourcePolicyResponseTypeDef:
        """
        Replaces the existing resource policy for a bot or bot alias with a new one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_resource_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#update_resource_policy)
        """

    async def update_slot(
        self,
        *,
        slotId: str,
        slotName: str,
        valueElicitationSetting: SlotValueElicitationSettingTypeDef,
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        description: str = ...,
        slotTypeId: str = ...,
        obfuscationSetting: ObfuscationSettingTypeDef = ...,
        multipleValuesSetting: MultipleValuesSettingTypeDef = ...,
        subSlotSetting: SubSlotSettingTypeDef = ...,
    ) -> UpdateSlotResponseTypeDef:
        """
        Updates the settings for a slot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#update_slot)
        """

    async def update_slot_type(
        self,
        *,
        slotTypeId: str,
        slotTypeName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = ...,
        slotTypeValues: Sequence[SlotTypeValueTypeDef] = ...,
        valueSelectionSetting: SlotValueSelectionSettingTypeDef = ...,
        parentSlotTypeSignature: str = ...,
        externalSourceSetting: ExternalSourceSettingTypeDef = ...,
        compositeSlotTypeSetting: CompositeSlotTypeSettingTypeDef = ...,
    ) -> UpdateSlotTypeResponseTypeDef:
        """
        Updates the configuration of an existing slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#update_slot_type)
        """

    async def update_test_set(
        self, *, testSetId: str, testSetName: str, description: str = ...
    ) -> UpdateTestSetResponseTypeDef:
        """
        The action to update the test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_test_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#update_test_set)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bot_alias_available"]) -> BotAliasAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bot_available"]) -> BotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bot_export_completed"]) -> BotExportCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bot_import_completed"]) -> BotImportCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bot_locale_built"]) -> BotLocaleBuiltWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bot_locale_created"]) -> BotLocaleCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["bot_locale_express_testing_available"]
    ) -> BotLocaleExpressTestingAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["bot_version_available"]
    ) -> BotVersionAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/#get_waiter)
        """

    async def __aenter__(self) -> "LexModelsV2Client":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/client/)
        """
