"""
Type annotations for ssm-contacts service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_ssm_contacts.client import SSMContactsClient
    from types_aiobotocore_ssm_contacts.paginator import (
        ListContactChannelsPaginator,
        ListContactsPaginator,
        ListEngagementsPaginator,
        ListPageReceiptsPaginator,
        ListPageResolutionsPaginator,
        ListPagesByContactPaginator,
        ListPagesByEngagementPaginator,
        ListPreviewRotationShiftsPaginator,
        ListRotationOverridesPaginator,
        ListRotationShiftsPaginator,
        ListRotationsPaginator,
    )

    session = get_session()
    with session.create_client("ssm-contacts") as client:
        client: SSMContactsClient

        list_contact_channels_paginator: ListContactChannelsPaginator = client.get_paginator("list_contact_channels")
        list_contacts_paginator: ListContactsPaginator = client.get_paginator("list_contacts")
        list_engagements_paginator: ListEngagementsPaginator = client.get_paginator("list_engagements")
        list_page_receipts_paginator: ListPageReceiptsPaginator = client.get_paginator("list_page_receipts")
        list_page_resolutions_paginator: ListPageResolutionsPaginator = client.get_paginator("list_page_resolutions")
        list_pages_by_contact_paginator: ListPagesByContactPaginator = client.get_paginator("list_pages_by_contact")
        list_pages_by_engagement_paginator: ListPagesByEngagementPaginator = client.get_paginator("list_pages_by_engagement")
        list_preview_rotation_shifts_paginator: ListPreviewRotationShiftsPaginator = client.get_paginator("list_preview_rotation_shifts")
        list_rotation_overrides_paginator: ListRotationOverridesPaginator = client.get_paginator("list_rotation_overrides")
        list_rotation_shifts_paginator: ListRotationShiftsPaginator = client.get_paginator("list_rotation_shifts")
        list_rotations_paginator: ListRotationsPaginator = client.get_paginator("list_rotations")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import ContactTypeType
from .type_defs import (
    ListContactChannelsResultTypeDef,
    ListContactsResultTypeDef,
    ListEngagementsResultTypeDef,
    ListPageReceiptsResultTypeDef,
    ListPageResolutionsResultTypeDef,
    ListPagesByContactResultTypeDef,
    ListPagesByEngagementResultTypeDef,
    ListPreviewRotationShiftsResultTypeDef,
    ListRotationOverridesResultTypeDef,
    ListRotationShiftsResultTypeDef,
    ListRotationsResultTypeDef,
    PaginatorConfigTypeDef,
    PreviewOverrideTypeDef,
    RecurrenceSettingsTypeDef,
    TimeRangeTypeDef,
    TimestampTypeDef,
)

__all__ = (
    "ListContactChannelsPaginator",
    "ListContactsPaginator",
    "ListEngagementsPaginator",
    "ListPageReceiptsPaginator",
    "ListPageResolutionsPaginator",
    "ListPagesByContactPaginator",
    "ListPagesByEngagementPaginator",
    "ListPreviewRotationShiftsPaginator",
    "ListRotationOverridesPaginator",
    "ListRotationShiftsPaginator",
    "ListRotationsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListContactChannelsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContactChannels)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listcontactchannelspaginator)
    """

    def paginate(
        self, *, ContactId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListContactChannelsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContactChannels.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listcontactchannelspaginator)
        """

class ListContactsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContacts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listcontactspaginator)
    """

    def paginate(
        self,
        *,
        AliasPrefix: str = ...,
        Type: ContactTypeType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListContactsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListContacts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listcontactspaginator)
        """

class ListEngagementsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListEngagements)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listengagementspaginator)
    """

    def paginate(
        self,
        *,
        IncidentId: str = ...,
        TimeRangeValue: TimeRangeTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListEngagementsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListEngagements.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listengagementspaginator)
        """

class ListPageReceiptsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPageReceipts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listpagereceiptspaginator)
    """

    def paginate(
        self, *, PageId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListPageReceiptsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPageReceipts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listpagereceiptspaginator)
        """

class ListPageResolutionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPageResolutions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listpageresolutionspaginator)
    """

    def paginate(
        self, *, PageId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListPageResolutionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPageResolutions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listpageresolutionspaginator)
        """

class ListPagesByContactPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByContact)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listpagesbycontactpaginator)
    """

    def paginate(
        self, *, ContactId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListPagesByContactResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByContact.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listpagesbycontactpaginator)
        """

class ListPagesByEngagementPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByEngagement)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listpagesbyengagementpaginator)
    """

    def paginate(
        self, *, EngagementId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListPagesByEngagementResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPagesByEngagement.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listpagesbyengagementpaginator)
        """

class ListPreviewRotationShiftsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPreviewRotationShifts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listpreviewrotationshiftspaginator)
    """

    def paginate(
        self,
        *,
        EndTime: TimestampTypeDef,
        Members: Sequence[str],
        TimeZoneId: str,
        Recurrence: RecurrenceSettingsTypeDef,
        RotationStartTime: TimestampTypeDef = ...,
        StartTime: TimestampTypeDef = ...,
        Overrides: Sequence[PreviewOverrideTypeDef] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListPreviewRotationShiftsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListPreviewRotationShifts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listpreviewrotationshiftspaginator)
        """

class ListRotationOverridesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListRotationOverrides)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listrotationoverridespaginator)
    """

    def paginate(
        self,
        *,
        RotationId: str,
        StartTime: TimestampTypeDef,
        EndTime: TimestampTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRotationOverridesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListRotationOverrides.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listrotationoverridespaginator)
        """

class ListRotationShiftsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListRotationShifts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listrotationshiftspaginator)
    """

    def paginate(
        self,
        *,
        RotationId: str,
        EndTime: TimestampTypeDef,
        StartTime: TimestampTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRotationShiftsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListRotationShifts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listrotationshiftspaginator)
        """

class ListRotationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListRotations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listrotationspaginator)
    """

    def paginate(
        self, *, RotationNamePrefix: str = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListRotationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html#SSMContacts.Paginator.ListRotations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/paginators/#listrotationspaginator)
        """
