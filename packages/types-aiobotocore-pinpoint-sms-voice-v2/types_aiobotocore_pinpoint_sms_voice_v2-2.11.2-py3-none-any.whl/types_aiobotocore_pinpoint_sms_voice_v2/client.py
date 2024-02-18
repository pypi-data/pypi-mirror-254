"""
Type annotations for pinpoint-sms-voice-v2 service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_pinpoint_sms_voice_v2.client import PinpointSMSVoiceV2Client

    session = get_session()
    async with session.create_client("pinpoint-sms-voice-v2") as client:
        client: PinpointSMSVoiceV2Client
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    DestinationCountryParameterKeyType,
    EventTypeType,
    KeywordActionType,
    LanguageCodeType,
    MessageTypeType,
    NumberCapabilityType,
    RequestableNumberTypeType,
    VerificationChannelType,
    VoiceIdType,
    VoiceMessageBodyTextTypeType,
)
from .paginator import (
    DescribeAccountAttributesPaginator,
    DescribeAccountLimitsPaginator,
    DescribeConfigurationSetsPaginator,
    DescribeKeywordsPaginator,
    DescribeOptedOutNumbersPaginator,
    DescribeOptOutListsPaginator,
    DescribePhoneNumbersPaginator,
    DescribePoolsPaginator,
    DescribeRegistrationAttachmentsPaginator,
    DescribeRegistrationFieldDefinitionsPaginator,
    DescribeRegistrationFieldValuesPaginator,
    DescribeRegistrationSectionDefinitionsPaginator,
    DescribeRegistrationsPaginator,
    DescribeRegistrationTypeDefinitionsPaginator,
    DescribeRegistrationVersionsPaginator,
    DescribeSenderIdsPaginator,
    DescribeSpendLimitsPaginator,
    DescribeVerifiedDestinationNumbersPaginator,
    ListPoolOriginationIdentitiesPaginator,
    ListRegistrationAssociationsPaginator,
)
from .type_defs import (
    AssociateOriginationIdentityResultTypeDef,
    BlobTypeDef,
    CloudWatchLogsDestinationTypeDef,
    ConfigurationSetFilterTypeDef,
    CreateConfigurationSetResultTypeDef,
    CreateEventDestinationResultTypeDef,
    CreateOptOutListResultTypeDef,
    CreatePoolResultTypeDef,
    CreateRegistrationAssociationResultTypeDef,
    CreateRegistrationAttachmentResultTypeDef,
    CreateRegistrationResultTypeDef,
    CreateRegistrationVersionResultTypeDef,
    CreateVerifiedDestinationNumberResultTypeDef,
    DeleteConfigurationSetResultTypeDef,
    DeleteDefaultMessageTypeResultTypeDef,
    DeleteDefaultSenderIdResultTypeDef,
    DeleteEventDestinationResultTypeDef,
    DeleteKeywordResultTypeDef,
    DeleteOptedOutNumberResultTypeDef,
    DeleteOptOutListResultTypeDef,
    DeletePoolResultTypeDef,
    DeleteRegistrationAttachmentResultTypeDef,
    DeleteRegistrationFieldValueResultTypeDef,
    DeleteRegistrationResultTypeDef,
    DeleteTextMessageSpendLimitOverrideResultTypeDef,
    DeleteVerifiedDestinationNumberResultTypeDef,
    DeleteVoiceMessageSpendLimitOverrideResultTypeDef,
    DescribeAccountAttributesResultTypeDef,
    DescribeAccountLimitsResultTypeDef,
    DescribeConfigurationSetsResultTypeDef,
    DescribeKeywordsResultTypeDef,
    DescribeOptedOutNumbersResultTypeDef,
    DescribeOptOutListsResultTypeDef,
    DescribePhoneNumbersResultTypeDef,
    DescribePoolsResultTypeDef,
    DescribeRegistrationAttachmentsResultTypeDef,
    DescribeRegistrationFieldDefinitionsResultTypeDef,
    DescribeRegistrationFieldValuesResultTypeDef,
    DescribeRegistrationSectionDefinitionsResultTypeDef,
    DescribeRegistrationsResultTypeDef,
    DescribeRegistrationTypeDefinitionsResultTypeDef,
    DescribeRegistrationVersionsResultTypeDef,
    DescribeSenderIdsResultTypeDef,
    DescribeSpendLimitsResultTypeDef,
    DescribeVerifiedDestinationNumbersResultTypeDef,
    DisassociateOriginationIdentityResultTypeDef,
    DiscardRegistrationVersionResultTypeDef,
    KeywordFilterTypeDef,
    KinesisFirehoseDestinationTypeDef,
    ListPoolOriginationIdentitiesResultTypeDef,
    ListRegistrationAssociationsResultTypeDef,
    ListTagsForResourceResultTypeDef,
    OptedOutFilterTypeDef,
    PhoneNumberFilterTypeDef,
    PoolFilterTypeDef,
    PoolOriginationIdentitiesFilterTypeDef,
    PutKeywordResultTypeDef,
    PutOptedOutNumberResultTypeDef,
    PutRegistrationFieldValueResultTypeDef,
    RegistrationAssociationFilterTypeDef,
    RegistrationAttachmentFilterTypeDef,
    RegistrationFilterTypeDef,
    RegistrationTypeFilterTypeDef,
    RegistrationVersionFilterTypeDef,
    ReleasePhoneNumberResultTypeDef,
    ReleaseSenderIdResultTypeDef,
    RequestPhoneNumberResultTypeDef,
    RequestSenderIdResultTypeDef,
    SendDestinationNumberVerificationCodeResultTypeDef,
    SenderIdAndCountryTypeDef,
    SenderIdFilterTypeDef,
    SendTextMessageResultTypeDef,
    SendVoiceMessageResultTypeDef,
    SetDefaultMessageTypeResultTypeDef,
    SetDefaultSenderIdResultTypeDef,
    SetTextMessageSpendLimitOverrideResultTypeDef,
    SetVoiceMessageSpendLimitOverrideResultTypeDef,
    SnsDestinationTypeDef,
    SubmitRegistrationVersionResultTypeDef,
    TagTypeDef,
    UpdateEventDestinationResultTypeDef,
    UpdatePhoneNumberResultTypeDef,
    UpdatePoolResultTypeDef,
    UpdateSenderIdResultTypeDef,
    VerifiedDestinationNumberFilterTypeDef,
    VerifyDestinationNumberResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PinpointSMSVoiceV2Client",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class PinpointSMSVoiceV2Client(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PinpointSMSVoiceV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#exceptions)
        """

    async def associate_origination_identity(
        self, *, PoolId: str, OriginationIdentity: str, IsoCountryCode: str, ClientToken: str = ...
    ) -> AssociateOriginationIdentityResultTypeDef:
        """
        Associates the specified origination identity with a pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.associate_origination_identity)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#associate_origination_identity)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#close)
        """

    async def create_configuration_set(
        self, *, ConfigurationSetName: str, Tags: Sequence[TagTypeDef] = ..., ClientToken: str = ...
    ) -> CreateConfigurationSetResultTypeDef:
        """
        Creates a new configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_configuration_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_configuration_set)
        """

    async def create_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        MatchingEventTypes: Sequence[EventTypeType],
        CloudWatchLogsDestination: CloudWatchLogsDestinationTypeDef = ...,
        KinesisFirehoseDestination: KinesisFirehoseDestinationTypeDef = ...,
        SnsDestination: SnsDestinationTypeDef = ...,
        ClientToken: str = ...,
    ) -> CreateEventDestinationResultTypeDef:
        """
        Creates a new event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_event_destination)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_event_destination)
        """

    async def create_opt_out_list(
        self, *, OptOutListName: str, Tags: Sequence[TagTypeDef] = ..., ClientToken: str = ...
    ) -> CreateOptOutListResultTypeDef:
        """
        Creates a new opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_opt_out_list)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_opt_out_list)
        """

    async def create_pool(
        self,
        *,
        OriginationIdentity: str,
        IsoCountryCode: str,
        MessageType: MessageTypeType,
        DeletionProtectionEnabled: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ClientToken: str = ...,
    ) -> CreatePoolResultTypeDef:
        """
        Creates a new pool and associates the specified origination identity to the
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_pool)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_pool)
        """

    async def create_registration(
        self, *, RegistrationType: str, Tags: Sequence[TagTypeDef] = ..., ClientToken: str = ...
    ) -> CreateRegistrationResultTypeDef:
        """
        Creates a new registration based on the **RegistrationType** field.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_registration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_registration)
        """

    async def create_registration_association(
        self, *, RegistrationId: str, ResourceId: str
    ) -> CreateRegistrationAssociationResultTypeDef:
        """
        Associate the registration with an origination identity such as a phone number
        or sender
        ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_registration_association)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_registration_association)
        """

    async def create_registration_attachment(
        self,
        *,
        AttachmentBody: BlobTypeDef = ...,
        AttachmentUrl: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ClientToken: str = ...,
    ) -> CreateRegistrationAttachmentResultTypeDef:
        """
        Create a new registration attachment to use for uploading a file or a URL to a
        file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_registration_attachment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_registration_attachment)
        """

    async def create_registration_version(
        self, *, RegistrationId: str
    ) -> CreateRegistrationVersionResultTypeDef:
        """
        Create a new version of the registration and increase the **VersionNumber**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_registration_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_registration_version)
        """

    async def create_verified_destination_number(
        self,
        *,
        DestinationPhoneNumber: str,
        Tags: Sequence[TagTypeDef] = ...,
        ClientToken: str = ...,
    ) -> CreateVerifiedDestinationNumberResultTypeDef:
        """
        You can only send messages to verified destination numbers when your account is
        in the
        sandbox.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.create_verified_destination_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#create_verified_destination_number)
        """

    async def delete_configuration_set(
        self, *, ConfigurationSetName: str
    ) -> DeleteConfigurationSetResultTypeDef:
        """
        Deletes an existing configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_configuration_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_configuration_set)
        """

    async def delete_default_message_type(
        self, *, ConfigurationSetName: str
    ) -> DeleteDefaultMessageTypeResultTypeDef:
        """
        Deletes an existing default message type on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_default_message_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_default_message_type)
        """

    async def delete_default_sender_id(
        self, *, ConfigurationSetName: str
    ) -> DeleteDefaultSenderIdResultTypeDef:
        """
        Deletes an existing default sender ID on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_default_sender_id)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_default_sender_id)
        """

    async def delete_event_destination(
        self, *, ConfigurationSetName: str, EventDestinationName: str
    ) -> DeleteEventDestinationResultTypeDef:
        """
        Deletes an existing event destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_event_destination)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_event_destination)
        """

    async def delete_keyword(
        self, *, OriginationIdentity: str, Keyword: str
    ) -> DeleteKeywordResultTypeDef:
        """
        Deletes an existing keyword from an origination phone number or pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_keyword)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_keyword)
        """

    async def delete_opt_out_list(self, *, OptOutListName: str) -> DeleteOptOutListResultTypeDef:
        """
        Deletes an existing opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_opt_out_list)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_opt_out_list)
        """

    async def delete_opted_out_number(
        self, *, OptOutListName: str, OptedOutNumber: str
    ) -> DeleteOptedOutNumberResultTypeDef:
        """
        Deletes an existing opted out destination phone number from the specified
        opt-out
        list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_opted_out_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_opted_out_number)
        """

    async def delete_pool(self, *, PoolId: str) -> DeletePoolResultTypeDef:
        """
        Deletes an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_pool)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_pool)
        """

    async def delete_registration(self, *, RegistrationId: str) -> DeleteRegistrationResultTypeDef:
        """
        Permanently delete an existing registration from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_registration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_registration)
        """

    async def delete_registration_attachment(
        self, *, RegistrationAttachmentId: str
    ) -> DeleteRegistrationAttachmentResultTypeDef:
        """
        Permanently delete the specified registration attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_registration_attachment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_registration_attachment)
        """

    async def delete_registration_field_value(
        self, *, RegistrationId: str, FieldPath: str
    ) -> DeleteRegistrationFieldValueResultTypeDef:
        """
        Delete the value in a registration form field.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_registration_field_value)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_registration_field_value)
        """

    async def delete_text_message_spend_limit_override(
        self,
    ) -> DeleteTextMessageSpendLimitOverrideResultTypeDef:
        """
        Deletes an account-level monthly spending limit override for sending text
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_text_message_spend_limit_override)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_text_message_spend_limit_override)
        """

    async def delete_verified_destination_number(
        self, *, VerifiedDestinationNumberId: str
    ) -> DeleteVerifiedDestinationNumberResultTypeDef:
        """
        Delete a verified destination phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_verified_destination_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_verified_destination_number)
        """

    async def delete_voice_message_spend_limit_override(
        self,
    ) -> DeleteVoiceMessageSpendLimitOverrideResultTypeDef:
        """
        Deletes an account level monthly spend limit override for sending voice
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.delete_voice_message_spend_limit_override)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#delete_voice_message_spend_limit_override)
        """

    async def describe_account_attributes(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeAccountAttributesResultTypeDef:
        """
        Describes attributes of your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_account_attributes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_account_attributes)
        """

    async def describe_account_limits(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeAccountLimitsResultTypeDef:
        """
        Describes the current Amazon Pinpoint SMS Voice V2 resource quotas for your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_account_limits)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_account_limits)
        """

    async def describe_configuration_sets(
        self,
        *,
        ConfigurationSetNames: Sequence[str] = ...,
        Filters: Sequence[ConfigurationSetFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeConfigurationSetsResultTypeDef:
        """
        Describes the specified configuration sets or all in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_configuration_sets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_configuration_sets)
        """

    async def describe_keywords(
        self,
        *,
        OriginationIdentity: str,
        Keywords: Sequence[str] = ...,
        Filters: Sequence[KeywordFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeKeywordsResultTypeDef:
        """
        Describes the specified keywords or all keywords on your origination phone
        number or
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_keywords)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_keywords)
        """

    async def describe_opt_out_lists(
        self, *, OptOutListNames: Sequence[str] = ..., NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeOptOutListsResultTypeDef:
        """
        Describes the specified opt-out list or all opt-out lists in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_opt_out_lists)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_opt_out_lists)
        """

    async def describe_opted_out_numbers(
        self,
        *,
        OptOutListName: str,
        OptedOutNumbers: Sequence[str] = ...,
        Filters: Sequence[OptedOutFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeOptedOutNumbersResultTypeDef:
        """
        Describes the specified opted out destination numbers or all opted out
        destination numbers in an opt-out
        list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_opted_out_numbers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_opted_out_numbers)
        """

    async def describe_phone_numbers(
        self,
        *,
        PhoneNumberIds: Sequence[str] = ...,
        Filters: Sequence[PhoneNumberFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribePhoneNumbersResultTypeDef:
        """
        Describes the specified origination phone number, or all the phone numbers in
        your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_phone_numbers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_phone_numbers)
        """

    async def describe_pools(
        self,
        *,
        PoolIds: Sequence[str] = ...,
        Filters: Sequence[PoolFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribePoolsResultTypeDef:
        """
        Retrieves the specified pools or all pools associated with your Amazon Web
        Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_pools)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_pools)
        """

    async def describe_registration_attachments(
        self,
        *,
        RegistrationAttachmentIds: Sequence[str] = ...,
        Filters: Sequence[RegistrationAttachmentFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeRegistrationAttachmentsResultTypeDef:
        """
        Retrieves the specified registration attachments or all registration
        attachments associated with your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registration_attachments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_registration_attachments)
        """

    async def describe_registration_field_definitions(
        self,
        *,
        RegistrationType: str,
        SectionPath: str = ...,
        FieldPaths: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeRegistrationFieldDefinitionsResultTypeDef:
        """
        Retrieves the specified registration type field definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registration_field_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_registration_field_definitions)
        """

    async def describe_registration_field_values(
        self,
        *,
        RegistrationId: str,
        VersionNumber: int = ...,
        SectionPath: str = ...,
        FieldPaths: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeRegistrationFieldValuesResultTypeDef:
        """
        Retrieves the specified registration field values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registration_field_values)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_registration_field_values)
        """

    async def describe_registration_section_definitions(
        self,
        *,
        RegistrationType: str,
        SectionPaths: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeRegistrationSectionDefinitionsResultTypeDef:
        """
        Retrieves the specified registration section definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registration_section_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_registration_section_definitions)
        """

    async def describe_registration_type_definitions(
        self,
        *,
        RegistrationTypes: Sequence[str] = ...,
        Filters: Sequence[RegistrationTypeFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeRegistrationTypeDefinitionsResultTypeDef:
        """
        Retrieves the specified registration type definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registration_type_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_registration_type_definitions)
        """

    async def describe_registration_versions(
        self,
        *,
        RegistrationId: str,
        VersionNumbers: Sequence[int] = ...,
        Filters: Sequence[RegistrationVersionFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeRegistrationVersionsResultTypeDef:
        """
        Retrieves the specified registration version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registration_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_registration_versions)
        """

    async def describe_registrations(
        self,
        *,
        RegistrationIds: Sequence[str] = ...,
        Filters: Sequence[RegistrationFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeRegistrationsResultTypeDef:
        """
        Retrieves the specified registrations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_registrations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_registrations)
        """

    async def describe_sender_ids(
        self,
        *,
        SenderIds: Sequence[SenderIdAndCountryTypeDef] = ...,
        Filters: Sequence[SenderIdFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeSenderIdsResultTypeDef:
        """
        Describes the specified SenderIds or all SenderIds associated with your Amazon
        Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_sender_ids)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_sender_ids)
        """

    async def describe_spend_limits(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeSpendLimitsResultTypeDef:
        """
        Describes the current Amazon Pinpoint monthly spend limits for sending voice
        and text
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_spend_limits)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_spend_limits)
        """

    async def describe_verified_destination_numbers(
        self,
        *,
        VerifiedDestinationNumberIds: Sequence[str] = ...,
        DestinationPhoneNumbers: Sequence[str] = ...,
        Filters: Sequence[VerifiedDestinationNumberFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeVerifiedDestinationNumbersResultTypeDef:
        """
        Retrieves the specified verified destiona numbers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.describe_verified_destination_numbers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#describe_verified_destination_numbers)
        """

    async def disassociate_origination_identity(
        self, *, PoolId: str, OriginationIdentity: str, IsoCountryCode: str, ClientToken: str = ...
    ) -> DisassociateOriginationIdentityResultTypeDef:
        """
        Removes the specified origination identity from an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.disassociate_origination_identity)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#disassociate_origination_identity)
        """

    async def discard_registration_version(
        self, *, RegistrationId: str
    ) -> DiscardRegistrationVersionResultTypeDef:
        """
        Discard the current version of the registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.discard_registration_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#discard_registration_version)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#generate_presigned_url)
        """

    async def list_pool_origination_identities(
        self,
        *,
        PoolId: str,
        Filters: Sequence[PoolOriginationIdentitiesFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListPoolOriginationIdentitiesResultTypeDef:
        """
        Lists all associated origination identities in your pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.list_pool_origination_identities)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#list_pool_origination_identities)
        """

    async def list_registration_associations(
        self,
        *,
        RegistrationId: str,
        Filters: Sequence[RegistrationAssociationFilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListRegistrationAssociationsResultTypeDef:
        """
        Retreive all of the origination identies that are associated with a
        registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.list_registration_associations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#list_registration_associations)
        """

    async def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResultTypeDef:
        """
        List all tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#list_tags_for_resource)
        """

    async def put_keyword(
        self,
        *,
        OriginationIdentity: str,
        Keyword: str,
        KeywordMessage: str,
        KeywordAction: KeywordActionType = ...,
    ) -> PutKeywordResultTypeDef:
        """
        Creates or updates a keyword configuration on an origination phone number or
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.put_keyword)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#put_keyword)
        """

    async def put_opted_out_number(
        self, *, OptOutListName: str, OptedOutNumber: str
    ) -> PutOptedOutNumberResultTypeDef:
        """
        Creates an opted out destination phone number in the opt-out list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.put_opted_out_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#put_opted_out_number)
        """

    async def put_registration_field_value(
        self,
        *,
        RegistrationId: str,
        FieldPath: str,
        SelectChoices: Sequence[str] = ...,
        TextValue: str = ...,
        RegistrationAttachmentId: str = ...,
    ) -> PutRegistrationFieldValueResultTypeDef:
        """
        Creates or updates a field value for a registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.put_registration_field_value)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#put_registration_field_value)
        """

    async def release_phone_number(self, *, PhoneNumberId: str) -> ReleasePhoneNumberResultTypeDef:
        """
        Releases an existing origination phone number in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.release_phone_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#release_phone_number)
        """

    async def release_sender_id(
        self, *, SenderId: str, IsoCountryCode: str
    ) -> ReleaseSenderIdResultTypeDef:
        """
        Releases an existing sender ID in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.release_sender_id)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#release_sender_id)
        """

    async def request_phone_number(
        self,
        *,
        IsoCountryCode: str,
        MessageType: MessageTypeType,
        NumberCapabilities: Sequence[NumberCapabilityType],
        NumberType: RequestableNumberTypeType,
        OptOutListName: str = ...,
        PoolId: str = ...,
        RegistrationId: str = ...,
        DeletionProtectionEnabled: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ClientToken: str = ...,
    ) -> RequestPhoneNumberResultTypeDef:
        """
        Request an origination phone number for use in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.request_phone_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#request_phone_number)
        """

    async def request_sender_id(
        self,
        *,
        SenderId: str,
        IsoCountryCode: str,
        MessageTypes: Sequence[MessageTypeType] = ...,
        DeletionProtectionEnabled: bool = ...,
        Tags: Sequence[TagTypeDef] = ...,
        ClientToken: str = ...,
    ) -> RequestSenderIdResultTypeDef:
        """
        Request a new sender ID that doesn't require registration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.request_sender_id)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#request_sender_id)
        """

    async def send_destination_number_verification_code(
        self,
        *,
        VerifiedDestinationNumberId: str,
        VerificationChannel: VerificationChannelType,
        LanguageCode: LanguageCodeType = ...,
        OriginationIdentity: str = ...,
        ConfigurationSetName: str = ...,
        Context: Mapping[str, str] = ...,
        DestinationCountryParameters: Mapping[DestinationCountryParameterKeyType, str] = ...,
    ) -> SendDestinationNumberVerificationCodeResultTypeDef:
        """
        Before you can send test messages to a verified destination phone number you
        need to opt-in the verified destination phone
        number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.send_destination_number_verification_code)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#send_destination_number_verification_code)
        """

    async def send_text_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str = ...,
        MessageBody: str = ...,
        MessageType: MessageTypeType = ...,
        Keyword: str = ...,
        ConfigurationSetName: str = ...,
        MaxPrice: str = ...,
        TimeToLive: int = ...,
        Context: Mapping[str, str] = ...,
        DestinationCountryParameters: Mapping[DestinationCountryParameterKeyType, str] = ...,
        DryRun: bool = ...,
    ) -> SendTextMessageResultTypeDef:
        """
        Creates a new text message and sends it to a recipient's phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.send_text_message)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#send_text_message)
        """

    async def send_voice_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str,
        MessageBody: str = ...,
        MessageBodyTextType: VoiceMessageBodyTextTypeType = ...,
        VoiceId: VoiceIdType = ...,
        ConfigurationSetName: str = ...,
        MaxPricePerMinute: str = ...,
        TimeToLive: int = ...,
        Context: Mapping[str, str] = ...,
        DryRun: bool = ...,
    ) -> SendVoiceMessageResultTypeDef:
        """
        Allows you to send a request that sends a voice message through Amazon Pinpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.send_voice_message)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#send_voice_message)
        """

    async def set_default_message_type(
        self, *, ConfigurationSetName: str, MessageType: MessageTypeType
    ) -> SetDefaultMessageTypeResultTypeDef:
        """
        Sets the default message type on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_default_message_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#set_default_message_type)
        """

    async def set_default_sender_id(
        self, *, ConfigurationSetName: str, SenderId: str
    ) -> SetDefaultSenderIdResultTypeDef:
        """
        Sets default sender ID on a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_default_sender_id)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#set_default_sender_id)
        """

    async def set_text_message_spend_limit_override(
        self, *, MonthlyLimit: int
    ) -> SetTextMessageSpendLimitOverrideResultTypeDef:
        """
        Sets an account level monthly spend limit override for sending text messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_text_message_spend_limit_override)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#set_text_message_spend_limit_override)
        """

    async def set_voice_message_spend_limit_override(
        self, *, MonthlyLimit: int
    ) -> SetVoiceMessageSpendLimitOverrideResultTypeDef:
        """
        Sets an account level monthly spend limit override for sending voice messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.set_voice_message_spend_limit_override)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#set_voice_message_spend_limit_override)
        """

    async def submit_registration_version(
        self, *, RegistrationId: str
    ) -> SubmitRegistrationVersionResultTypeDef:
        """
        Submit the specified registration for review and approval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.submit_registration_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#submit_registration_version)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Adds or overwrites only the specified tags for the specified Amazon Pinpoint
        SMS Voice, version 2
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes the association of the specified tags from an Amazon Pinpoint SMS Voice
        V2
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#untag_resource)
        """

    async def update_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        Enabled: bool = ...,
        MatchingEventTypes: Sequence[EventTypeType] = ...,
        CloudWatchLogsDestination: CloudWatchLogsDestinationTypeDef = ...,
        KinesisFirehoseDestination: KinesisFirehoseDestinationTypeDef = ...,
        SnsDestination: SnsDestinationTypeDef = ...,
    ) -> UpdateEventDestinationResultTypeDef:
        """
        Updates an existing event destination in a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_event_destination)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#update_event_destination)
        """

    async def update_phone_number(
        self,
        *,
        PhoneNumberId: str,
        TwoWayEnabled: bool = ...,
        TwoWayChannelArn: str = ...,
        TwoWayChannelRole: str = ...,
        SelfManagedOptOutsEnabled: bool = ...,
        OptOutListName: str = ...,
        DeletionProtectionEnabled: bool = ...,
    ) -> UpdatePhoneNumberResultTypeDef:
        """
        Updates the configuration of an existing origination phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_phone_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#update_phone_number)
        """

    async def update_pool(
        self,
        *,
        PoolId: str,
        TwoWayEnabled: bool = ...,
        TwoWayChannelArn: str = ...,
        TwoWayChannelRole: str = ...,
        SelfManagedOptOutsEnabled: bool = ...,
        OptOutListName: str = ...,
        SharedRoutesEnabled: bool = ...,
        DeletionProtectionEnabled: bool = ...,
    ) -> UpdatePoolResultTypeDef:
        """
        Updates the configuration of an existing pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_pool)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#update_pool)
        """

    async def update_sender_id(
        self, *, SenderId: str, IsoCountryCode: str, DeletionProtectionEnabled: bool = ...
    ) -> UpdateSenderIdResultTypeDef:
        """
        Updates the configuration of an existing sender ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.update_sender_id)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#update_sender_id)
        """

    async def verify_destination_number(
        self, *, VerifiedDestinationNumberId: str, VerificationCode: str
    ) -> VerifyDestinationNumberResultTypeDef:
        """
        Use the verification code that was received by the verified destination phone
        number to opt-in the verified destination phone number to receive more
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.verify_destination_number)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#verify_destination_number)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_attributes"]
    ) -> DescribeAccountAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> DescribeAccountLimitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_configuration_sets"]
    ) -> DescribeConfigurationSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_keywords"]
    ) -> DescribeKeywordsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_opt_out_lists"]
    ) -> DescribeOptOutListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_opted_out_numbers"]
    ) -> DescribeOptedOutNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_phone_numbers"]
    ) -> DescribePhoneNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_pools"]) -> DescribePoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registration_attachments"]
    ) -> DescribeRegistrationAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registration_field_definitions"]
    ) -> DescribeRegistrationFieldDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registration_field_values"]
    ) -> DescribeRegistrationFieldValuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registration_section_definitions"]
    ) -> DescribeRegistrationSectionDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registration_type_definitions"]
    ) -> DescribeRegistrationTypeDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registration_versions"]
    ) -> DescribeRegistrationVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registrations"]
    ) -> DescribeRegistrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_sender_ids"]
    ) -> DescribeSenderIdsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spend_limits"]
    ) -> DescribeSpendLimitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_verified_destination_numbers"]
    ) -> DescribeVerifiedDestinationNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pool_origination_identities"]
    ) -> ListPoolOriginationIdentitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_registration_associations"]
    ) -> ListRegistrationAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/#get_paginator)
        """

    async def __aenter__(self) -> "PinpointSMSVoiceV2Client":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html#PinpointSMSVoiceV2.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pinpoint_sms_voice_v2/client/)
        """
