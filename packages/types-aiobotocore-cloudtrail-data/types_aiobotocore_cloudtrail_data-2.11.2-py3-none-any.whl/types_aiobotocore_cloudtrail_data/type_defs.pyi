"""
Type annotations for cloudtrail-data service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudtrail_data/type_defs/)

Usage::

    ```python
    from types_aiobotocore_cloudtrail_data.type_defs import AuditEventResultEntryTypeDef

    data: AuditEventResultEntryTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AuditEventResultEntryTypeDef",
    "AuditEventTypeDef",
    "ResponseMetadataTypeDef",
    "ResultErrorEntryTypeDef",
    "PutAuditEventsRequestRequestTypeDef",
    "PutAuditEventsResponseTypeDef",
)

AuditEventResultEntryTypeDef = TypedDict(
    "AuditEventResultEntryTypeDef",
    {
        "eventID": str,
        "id": str,
    },
)
AuditEventTypeDef = TypedDict(
    "AuditEventTypeDef",
    {
        "eventData": str,
        "id": str,
        "eventDataChecksum": NotRequired[str],
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
ResultErrorEntryTypeDef = TypedDict(
    "ResultErrorEntryTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "id": str,
    },
)
PutAuditEventsRequestRequestTypeDef = TypedDict(
    "PutAuditEventsRequestRequestTypeDef",
    {
        "auditEvents": Sequence[AuditEventTypeDef],
        "channelArn": str,
        "externalId": NotRequired[str],
    },
)
PutAuditEventsResponseTypeDef = TypedDict(
    "PutAuditEventsResponseTypeDef",
    {
        "failed": List[ResultErrorEntryTypeDef],
        "successful": List[AuditEventResultEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
