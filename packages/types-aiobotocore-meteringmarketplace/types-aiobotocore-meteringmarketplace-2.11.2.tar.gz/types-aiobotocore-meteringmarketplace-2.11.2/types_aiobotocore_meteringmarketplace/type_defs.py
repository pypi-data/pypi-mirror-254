"""
Type annotations for meteringmarketplace service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_meteringmarketplace/type_defs/)

Usage::

    ```python
    from types_aiobotocore_meteringmarketplace.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import UsageRecordResultStatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
    "RegisterUsageRequestRequestTypeDef",
    "ResolveCustomerRequestRequestTypeDef",
    "TagTypeDef",
    "MeterUsageResultTypeDef",
    "RegisterUsageResultTypeDef",
    "ResolveCustomerResultTypeDef",
    "UsageAllocationTypeDef",
    "MeterUsageRequestRequestTypeDef",
    "UsageRecordTypeDef",
    "BatchMeterUsageRequestRequestTypeDef",
    "UsageRecordResultTypeDef",
    "BatchMeterUsageResultTypeDef",
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
TimestampTypeDef = Union[datetime, str]
RegisterUsageRequestRequestTypeDef = TypedDict(
    "RegisterUsageRequestRequestTypeDef",
    {
        "ProductCode": str,
        "PublicKeyVersion": int,
        "Nonce": NotRequired[str],
    },
)
ResolveCustomerRequestRequestTypeDef = TypedDict(
    "ResolveCustomerRequestRequestTypeDef",
    {
        "RegistrationToken": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
MeterUsageResultTypeDef = TypedDict(
    "MeterUsageResultTypeDef",
    {
        "MeteringRecordId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterUsageResultTypeDef = TypedDict(
    "RegisterUsageResultTypeDef",
    {
        "PublicKeyRotationTimestamp": datetime,
        "Signature": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResolveCustomerResultTypeDef = TypedDict(
    "ResolveCustomerResultTypeDef",
    {
        "CustomerIdentifier": str,
        "ProductCode": str,
        "CustomerAWSAccountId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UsageAllocationTypeDef = TypedDict(
    "UsageAllocationTypeDef",
    {
        "AllocatedUsageQuantity": int,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
MeterUsageRequestRequestTypeDef = TypedDict(
    "MeterUsageRequestRequestTypeDef",
    {
        "ProductCode": str,
        "Timestamp": TimestampTypeDef,
        "UsageDimension": str,
        "UsageQuantity": NotRequired[int],
        "DryRun": NotRequired[bool],
        "UsageAllocations": NotRequired[Sequence[UsageAllocationTypeDef]],
    },
)
UsageRecordTypeDef = TypedDict(
    "UsageRecordTypeDef",
    {
        "Timestamp": TimestampTypeDef,
        "CustomerIdentifier": str,
        "Dimension": str,
        "Quantity": NotRequired[int],
        "UsageAllocations": NotRequired[Sequence[UsageAllocationTypeDef]],
    },
)
BatchMeterUsageRequestRequestTypeDef = TypedDict(
    "BatchMeterUsageRequestRequestTypeDef",
    {
        "UsageRecords": Sequence[UsageRecordTypeDef],
        "ProductCode": str,
    },
)
UsageRecordResultTypeDef = TypedDict(
    "UsageRecordResultTypeDef",
    {
        "UsageRecord": NotRequired[UsageRecordTypeDef],
        "MeteringRecordId": NotRequired[str],
        "Status": NotRequired[UsageRecordResultStatusType],
    },
)
BatchMeterUsageResultTypeDef = TypedDict(
    "BatchMeterUsageResultTypeDef",
    {
        "Results": List[UsageRecordResultTypeDef],
        "UnprocessedRecords": List[UsageRecordTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
