"""
Type annotations for clouddirectory service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_clouddirectory/type_defs/)

Usage::

    ```python
    from types_aiobotocore_clouddirectory.type_defs import ObjectReferenceTypeDef

    data: ObjectReferenceTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    BatchReadExceptionTypeType,
    ConsistencyLevelType,
    DirectoryStateType,
    FacetAttributeTypeType,
    FacetStyleType,
    ObjectTypeType,
    RangeModeType,
    RequiredAttributeBehaviorType,
    RuleTypeType,
    UpdateActionTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ObjectReferenceTypeDef",
    "SchemaFacetTypeDef",
    "ApplySchemaRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TypedLinkSchemaAndFacetNameTypeDef",
    "AttributeKeyTypeDef",
    "TypedAttributeValuePaginatorTypeDef",
    "BatchAttachObjectResponseTypeDef",
    "BatchAttachToIndexResponseTypeDef",
    "BatchCreateIndexResponseTypeDef",
    "BatchCreateObjectResponseTypeDef",
    "BatchDetachFromIndexResponseTypeDef",
    "BatchDetachObjectResponseTypeDef",
    "BatchListObjectChildrenResponseTypeDef",
    "PathToObjectIdentifiersTypeDef",
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    "BatchListObjectPoliciesResponseTypeDef",
    "BatchListPolicyAttachmentsResponseTypeDef",
    "BatchReadExceptionTypeDef",
    "BatchUpdateObjectAttributesResponseTypeDef",
    "BlobTypeDef",
    "CreateDirectoryRequestRequestTypeDef",
    "CreateSchemaRequestRequestTypeDef",
    "DeleteDirectoryRequestRequestTypeDef",
    "DeleteFacetRequestRequestTypeDef",
    "DeleteSchemaRequestRequestTypeDef",
    "DeleteTypedLinkFacetRequestRequestTypeDef",
    "DirectoryTypeDef",
    "DisableDirectoryRequestRequestTypeDef",
    "EnableDirectoryRequestRequestTypeDef",
    "RulePaginatorTypeDef",
    "RuleTypeDef",
    "FacetAttributeReferenceTypeDef",
    "FacetTypeDef",
    "GetAppliedSchemaVersionRequestRequestTypeDef",
    "GetDirectoryRequestRequestTypeDef",
    "GetFacetRequestRequestTypeDef",
    "GetSchemaAsJsonRequestRequestTypeDef",
    "GetTypedLinkFacetInformationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAppliedSchemaArnsRequestRequestTypeDef",
    "ListDevelopmentSchemaArnsRequestRequestTypeDef",
    "ListDirectoriesRequestRequestTypeDef",
    "ListFacetAttributesRequestRequestTypeDef",
    "ListFacetNamesRequestRequestTypeDef",
    "ListManagedSchemaArnsRequestRequestTypeDef",
    "ListPublishedSchemaArnsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ListTypedLinkFacetAttributesRequestRequestTypeDef",
    "ListTypedLinkFacetNamesRequestRequestTypeDef",
    "PolicyAttachmentTypeDef",
    "PublishSchemaRequestRequestTypeDef",
    "PutSchemaFromJsonRequestRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateSchemaRequestRequestTypeDef",
    "UpgradeAppliedSchemaRequestRequestTypeDef",
    "UpgradePublishedSchemaRequestRequestTypeDef",
    "AttachObjectRequestRequestTypeDef",
    "AttachPolicyRequestRequestTypeDef",
    "AttachToIndexRequestRequestTypeDef",
    "BatchAttachObjectTypeDef",
    "BatchAttachPolicyTypeDef",
    "BatchAttachToIndexTypeDef",
    "BatchDeleteObjectTypeDef",
    "BatchDetachFromIndexTypeDef",
    "BatchDetachObjectTypeDef",
    "BatchDetachPolicyTypeDef",
    "BatchGetObjectInformationTypeDef",
    "BatchListAttachedIndicesTypeDef",
    "BatchListObjectChildrenTypeDef",
    "BatchListObjectParentPathsTypeDef",
    "BatchListObjectParentsTypeDef",
    "BatchListObjectPoliciesTypeDef",
    "BatchListPolicyAttachmentsTypeDef",
    "BatchLookupPolicyTypeDef",
    "DeleteObjectRequestRequestTypeDef",
    "DetachFromIndexRequestRequestTypeDef",
    "DetachObjectRequestRequestTypeDef",
    "DetachPolicyRequestRequestTypeDef",
    "GetObjectInformationRequestRequestTypeDef",
    "ListAttachedIndicesRequestRequestTypeDef",
    "ListObjectChildrenRequestRequestTypeDef",
    "ListObjectParentPathsRequestRequestTypeDef",
    "ListObjectParentsRequestRequestTypeDef",
    "ListObjectPoliciesRequestRequestTypeDef",
    "ListPolicyAttachmentsRequestRequestTypeDef",
    "LookupPolicyRequestRequestTypeDef",
    "BatchGetObjectAttributesTypeDef",
    "BatchGetObjectInformationResponseTypeDef",
    "BatchListObjectAttributesTypeDef",
    "BatchRemoveFacetFromObjectTypeDef",
    "GetObjectAttributesRequestRequestTypeDef",
    "ListObjectAttributesRequestRequestTypeDef",
    "RemoveFacetFromObjectRequestRequestTypeDef",
    "ApplySchemaResponseTypeDef",
    "AttachObjectResponseTypeDef",
    "AttachToIndexResponseTypeDef",
    "CreateDirectoryResponseTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateObjectResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "DeleteDirectoryResponseTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DetachFromIndexResponseTypeDef",
    "DetachObjectResponseTypeDef",
    "DisableDirectoryResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableDirectoryResponseTypeDef",
    "GetAppliedSchemaVersionResponseTypeDef",
    "GetObjectInformationResponseTypeDef",
    "GetSchemaAsJsonResponseTypeDef",
    "GetTypedLinkFacetInformationResponseTypeDef",
    "ListAppliedSchemaArnsResponseTypeDef",
    "ListDevelopmentSchemaArnsResponseTypeDef",
    "ListFacetNamesResponseTypeDef",
    "ListManagedSchemaArnsResponseTypeDef",
    "ListObjectChildrenResponseTypeDef",
    "ListObjectPoliciesResponseTypeDef",
    "ListPolicyAttachmentsResponseTypeDef",
    "ListPublishedSchemaArnsResponseTypeDef",
    "ListTypedLinkFacetNamesResponseTypeDef",
    "PublishSchemaResponseTypeDef",
    "PutSchemaFromJsonResponseTypeDef",
    "UpdateObjectAttributesResponseTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpgradeAppliedSchemaResponseTypeDef",
    "UpgradePublishedSchemaResponseTypeDef",
    "BatchCreateIndexTypeDef",
    "CreateIndexRequestRequestTypeDef",
    "AttributeKeyAndValuePaginatorTypeDef",
    "AttributeNameAndValuePaginatorTypeDef",
    "TypedAttributeValueRangePaginatorTypeDef",
    "BatchListObjectParentPathsResponseTypeDef",
    "ListObjectParentPathsResponseTypeDef",
    "BatchListObjectParentsResponseTypeDef",
    "ListObjectParentsResponseTypeDef",
    "GetDirectoryResponseTypeDef",
    "ListDirectoriesResponseTypeDef",
    "FacetAttributeDefinitionPaginatorTypeDef",
    "TypedLinkAttributeDefinitionPaginatorTypeDef",
    "GetFacetResponseTypeDef",
    "ListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef",
    "ListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef",
    "ListDevelopmentSchemaArnsRequestListDevelopmentSchemaArnsPaginateTypeDef",
    "ListDirectoriesRequestListDirectoriesPaginateTypeDef",
    "ListFacetAttributesRequestListFacetAttributesPaginateTypeDef",
    "ListFacetNamesRequestListFacetNamesPaginateTypeDef",
    "ListManagedSchemaArnsRequestListManagedSchemaArnsPaginateTypeDef",
    "ListObjectAttributesRequestListObjectAttributesPaginateTypeDef",
    "ListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef",
    "ListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef",
    "ListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef",
    "ListPublishedSchemaArnsRequestListPublishedSchemaArnsPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "ListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef",
    "ListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef",
    "LookupPolicyRequestLookupPolicyPaginateTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "PolicyToPathTypeDef",
    "TypedAttributeValueTypeDef",
    "IndexAttachmentPaginatorTypeDef",
    "ListObjectAttributesResponsePaginatorTypeDef",
    "TypedLinkSpecifierPaginatorTypeDef",
    "ObjectAttributeRangePaginatorTypeDef",
    "TypedLinkAttributeRangePaginatorTypeDef",
    "FacetAttributePaginatorTypeDef",
    "ListTypedLinkFacetAttributesResponsePaginatorTypeDef",
    "BatchLookupPolicyResponseTypeDef",
    "LookupPolicyResponseTypeDef",
    "AttributeKeyAndValueTypeDef",
    "AttributeNameAndValueTypeDef",
    "FacetAttributeDefinitionTypeDef",
    "LinkAttributeActionTypeDef",
    "ObjectAttributeActionTypeDef",
    "TypedAttributeValueRangeTypeDef",
    "TypedLinkAttributeDefinitionTypeDef",
    "ListAttachedIndicesResponsePaginatorTypeDef",
    "ListIndexResponsePaginatorTypeDef",
    "ListIncomingTypedLinksResponsePaginatorTypeDef",
    "ListOutgoingTypedLinksResponsePaginatorTypeDef",
    "ListIndexRequestListIndexPaginateTypeDef",
    "ListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef",
    "ListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef",
    "ListFacetAttributesResponsePaginatorTypeDef",
    "AddFacetToObjectRequestRequestTypeDef",
    "BatchAddFacetToObjectTypeDef",
    "BatchCreateObjectTypeDef",
    "BatchGetLinkAttributesResponseTypeDef",
    "BatchGetObjectAttributesResponseTypeDef",
    "BatchListObjectAttributesResponseTypeDef",
    "CreateObjectRequestRequestTypeDef",
    "GetLinkAttributesResponseTypeDef",
    "GetObjectAttributesResponseTypeDef",
    "IndexAttachmentTypeDef",
    "ListObjectAttributesResponseTypeDef",
    "AttachTypedLinkRequestRequestTypeDef",
    "BatchAttachTypedLinkTypeDef",
    "TypedLinkSpecifierTypeDef",
    "FacetAttributeTypeDef",
    "LinkAttributeUpdateTypeDef",
    "ObjectAttributeUpdateTypeDef",
    "ObjectAttributeRangeTypeDef",
    "TypedLinkAttributeRangeTypeDef",
    "ListTypedLinkFacetAttributesResponseTypeDef",
    "TypedLinkFacetAttributeUpdateTypeDef",
    "TypedLinkFacetTypeDef",
    "BatchListAttachedIndicesResponseTypeDef",
    "BatchListIndexResponseTypeDef",
    "ListAttachedIndicesResponseTypeDef",
    "ListIndexResponseTypeDef",
    "AttachTypedLinkResponseTypeDef",
    "BatchAttachTypedLinkResponseTypeDef",
    "BatchDetachTypedLinkTypeDef",
    "BatchGetLinkAttributesTypeDef",
    "BatchListIncomingTypedLinksResponseTypeDef",
    "BatchListOutgoingTypedLinksResponseTypeDef",
    "DetachTypedLinkRequestRequestTypeDef",
    "GetLinkAttributesRequestRequestTypeDef",
    "ListIncomingTypedLinksResponseTypeDef",
    "ListOutgoingTypedLinksResponseTypeDef",
    "CreateFacetRequestRequestTypeDef",
    "FacetAttributeUpdateTypeDef",
    "ListFacetAttributesResponseTypeDef",
    "BatchUpdateLinkAttributesTypeDef",
    "UpdateLinkAttributesRequestRequestTypeDef",
    "BatchUpdateObjectAttributesTypeDef",
    "UpdateObjectAttributesRequestRequestTypeDef",
    "BatchListIndexTypeDef",
    "ListIndexRequestRequestTypeDef",
    "BatchListIncomingTypedLinksTypeDef",
    "BatchListOutgoingTypedLinksTypeDef",
    "ListIncomingTypedLinksRequestRequestTypeDef",
    "ListOutgoingTypedLinksRequestRequestTypeDef",
    "UpdateTypedLinkFacetRequestRequestTypeDef",
    "CreateTypedLinkFacetRequestRequestTypeDef",
    "BatchWriteOperationResponseTypeDef",
    "BatchReadSuccessfulResponseTypeDef",
    "UpdateFacetRequestRequestTypeDef",
    "BatchWriteOperationTypeDef",
    "BatchReadOperationTypeDef",
    "BatchWriteResponseTypeDef",
    "BatchReadOperationResponseTypeDef",
    "BatchWriteRequestRequestTypeDef",
    "BatchReadRequestRequestTypeDef",
    "BatchReadResponseTypeDef",
)

ObjectReferenceTypeDef = TypedDict(
    "ObjectReferenceTypeDef",
    {
        "Selector": NotRequired[str],
    },
)
SchemaFacetTypeDef = TypedDict(
    "SchemaFacetTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "FacetName": NotRequired[str],
    },
)
ApplySchemaRequestRequestTypeDef = TypedDict(
    "ApplySchemaRequestRequestTypeDef",
    {
        "PublishedSchemaArn": str,
        "DirectoryArn": str,
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
TypedLinkSchemaAndFacetNameTypeDef = TypedDict(
    "TypedLinkSchemaAndFacetNameTypeDef",
    {
        "SchemaArn": str,
        "TypedLinkName": str,
    },
)
AttributeKeyTypeDef = TypedDict(
    "AttributeKeyTypeDef",
    {
        "SchemaArn": str,
        "FacetName": str,
        "Name": str,
    },
)
TypedAttributeValuePaginatorTypeDef = TypedDict(
    "TypedAttributeValuePaginatorTypeDef",
    {
        "StringValue": NotRequired[str],
        "BinaryValue": NotRequired[bytes],
        "BooleanValue": NotRequired[bool],
        "NumberValue": NotRequired[str],
        "DatetimeValue": NotRequired[datetime],
    },
)
BatchAttachObjectResponseTypeDef = TypedDict(
    "BatchAttachObjectResponseTypeDef",
    {
        "attachedObjectIdentifier": NotRequired[str],
    },
)
BatchAttachToIndexResponseTypeDef = TypedDict(
    "BatchAttachToIndexResponseTypeDef",
    {
        "AttachedObjectIdentifier": NotRequired[str],
    },
)
BatchCreateIndexResponseTypeDef = TypedDict(
    "BatchCreateIndexResponseTypeDef",
    {
        "ObjectIdentifier": NotRequired[str],
    },
)
BatchCreateObjectResponseTypeDef = TypedDict(
    "BatchCreateObjectResponseTypeDef",
    {
        "ObjectIdentifier": NotRequired[str],
    },
)
BatchDetachFromIndexResponseTypeDef = TypedDict(
    "BatchDetachFromIndexResponseTypeDef",
    {
        "DetachedObjectIdentifier": NotRequired[str],
    },
)
BatchDetachObjectResponseTypeDef = TypedDict(
    "BatchDetachObjectResponseTypeDef",
    {
        "detachedObjectIdentifier": NotRequired[str],
    },
)
BatchListObjectChildrenResponseTypeDef = TypedDict(
    "BatchListObjectChildrenResponseTypeDef",
    {
        "Children": NotRequired[Dict[str, str]],
        "NextToken": NotRequired[str],
    },
)
PathToObjectIdentifiersTypeDef = TypedDict(
    "PathToObjectIdentifiersTypeDef",
    {
        "Path": NotRequired[str],
        "ObjectIdentifiers": NotRequired[List[str]],
    },
)
ObjectIdentifierAndLinkNameTupleTypeDef = TypedDict(
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    {
        "ObjectIdentifier": NotRequired[str],
        "LinkName": NotRequired[str],
    },
)
BatchListObjectPoliciesResponseTypeDef = TypedDict(
    "BatchListObjectPoliciesResponseTypeDef",
    {
        "AttachedPolicyIds": NotRequired[List[str]],
        "NextToken": NotRequired[str],
    },
)
BatchListPolicyAttachmentsResponseTypeDef = TypedDict(
    "BatchListPolicyAttachmentsResponseTypeDef",
    {
        "ObjectIdentifiers": NotRequired[List[str]],
        "NextToken": NotRequired[str],
    },
)
BatchReadExceptionTypeDef = TypedDict(
    "BatchReadExceptionTypeDef",
    {
        "Type": NotRequired[BatchReadExceptionTypeType],
        "Message": NotRequired[str],
    },
)
BatchUpdateObjectAttributesResponseTypeDef = TypedDict(
    "BatchUpdateObjectAttributesResponseTypeDef",
    {
        "ObjectIdentifier": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CreateDirectoryRequestRequestTypeDef = TypedDict(
    "CreateDirectoryRequestRequestTypeDef",
    {
        "Name": str,
        "SchemaArn": str,
    },
)
CreateSchemaRequestRequestTypeDef = TypedDict(
    "CreateSchemaRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteDirectoryRequestRequestTypeDef = TypedDict(
    "DeleteDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)
DeleteFacetRequestRequestTypeDef = TypedDict(
    "DeleteFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
DeleteSchemaRequestRequestTypeDef = TypedDict(
    "DeleteSchemaRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)
DeleteTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "DeleteTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
DirectoryTypeDef = TypedDict(
    "DirectoryTypeDef",
    {
        "Name": NotRequired[str],
        "DirectoryArn": NotRequired[str],
        "State": NotRequired[DirectoryStateType],
        "CreationDateTime": NotRequired[datetime],
    },
)
DisableDirectoryRequestRequestTypeDef = TypedDict(
    "DisableDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)
EnableDirectoryRequestRequestTypeDef = TypedDict(
    "EnableDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)
RulePaginatorTypeDef = TypedDict(
    "RulePaginatorTypeDef",
    {
        "Type": NotRequired[RuleTypeType],
        "Parameters": NotRequired[Dict[str, str]],
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Type": NotRequired[RuleTypeType],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)
FacetAttributeReferenceTypeDef = TypedDict(
    "FacetAttributeReferenceTypeDef",
    {
        "TargetFacetName": str,
        "TargetAttributeName": str,
    },
)
FacetTypeDef = TypedDict(
    "FacetTypeDef",
    {
        "Name": NotRequired[str],
        "ObjectType": NotRequired[ObjectTypeType],
        "FacetStyle": NotRequired[FacetStyleType],
    },
)
GetAppliedSchemaVersionRequestRequestTypeDef = TypedDict(
    "GetAppliedSchemaVersionRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)
GetDirectoryRequestRequestTypeDef = TypedDict(
    "GetDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)
GetFacetRequestRequestTypeDef = TypedDict(
    "GetFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
GetSchemaAsJsonRequestRequestTypeDef = TypedDict(
    "GetSchemaAsJsonRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)
GetTypedLinkFacetInformationRequestRequestTypeDef = TypedDict(
    "GetTypedLinkFacetInformationRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ListAppliedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListAppliedSchemaArnsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDevelopmentSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDirectoriesRequestRequestTypeDef = TypedDict(
    "ListDirectoriesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "state": NotRequired[DirectoryStateType],
    },
)
ListFacetAttributesRequestRequestTypeDef = TypedDict(
    "ListFacetAttributesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListFacetNamesRequestRequestTypeDef = TypedDict(
    "ListFacetNamesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListManagedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListManagedSchemaArnsRequestRequestTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListPublishedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListPublishedSchemaArnsRequestRequestTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ListTypedLinkFacetAttributesRequestRequestTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTypedLinkFacetNamesRequestRequestTypeDef = TypedDict(
    "ListTypedLinkFacetNamesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PolicyAttachmentTypeDef = TypedDict(
    "PolicyAttachmentTypeDef",
    {
        "PolicyId": NotRequired[str],
        "ObjectIdentifier": NotRequired[str],
        "PolicyType": NotRequired[str],
    },
)
PublishSchemaRequestRequestTypeDef = TypedDict(
    "PublishSchemaRequestRequestTypeDef",
    {
        "DevelopmentSchemaArn": str,
        "Version": str,
        "MinorVersion": NotRequired[str],
        "Name": NotRequired[str],
    },
)
PutSchemaFromJsonRequestRequestTypeDef = TypedDict(
    "PutSchemaFromJsonRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Document": str,
    },
)
TimestampTypeDef = Union[datetime, str]
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateSchemaRequestRequestTypeDef = TypedDict(
    "UpdateSchemaRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
UpgradeAppliedSchemaRequestRequestTypeDef = TypedDict(
    "UpgradeAppliedSchemaRequestRequestTypeDef",
    {
        "PublishedSchemaArn": str,
        "DirectoryArn": str,
        "DryRun": NotRequired[bool],
    },
)
UpgradePublishedSchemaRequestRequestTypeDef = TypedDict(
    "UpgradePublishedSchemaRequestRequestTypeDef",
    {
        "DevelopmentSchemaArn": str,
        "PublishedSchemaArn": str,
        "MinorVersion": str,
        "DryRun": NotRequired[bool],
    },
)
AttachObjectRequestRequestTypeDef = TypedDict(
    "AttachObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ParentReference": ObjectReferenceTypeDef,
        "ChildReference": ObjectReferenceTypeDef,
        "LinkName": str,
    },
)
AttachPolicyRequestRequestTypeDef = TypedDict(
    "AttachPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": ObjectReferenceTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
AttachToIndexRequestRequestTypeDef = TypedDict(
    "AttachToIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": ObjectReferenceTypeDef,
        "TargetReference": ObjectReferenceTypeDef,
    },
)
BatchAttachObjectTypeDef = TypedDict(
    "BatchAttachObjectTypeDef",
    {
        "ParentReference": ObjectReferenceTypeDef,
        "ChildReference": ObjectReferenceTypeDef,
        "LinkName": str,
    },
)
BatchAttachPolicyTypeDef = TypedDict(
    "BatchAttachPolicyTypeDef",
    {
        "PolicyReference": ObjectReferenceTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
BatchAttachToIndexTypeDef = TypedDict(
    "BatchAttachToIndexTypeDef",
    {
        "IndexReference": ObjectReferenceTypeDef,
        "TargetReference": ObjectReferenceTypeDef,
    },
)
BatchDeleteObjectTypeDef = TypedDict(
    "BatchDeleteObjectTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
BatchDetachFromIndexTypeDef = TypedDict(
    "BatchDetachFromIndexTypeDef",
    {
        "IndexReference": ObjectReferenceTypeDef,
        "TargetReference": ObjectReferenceTypeDef,
    },
)
BatchDetachObjectTypeDef = TypedDict(
    "BatchDetachObjectTypeDef",
    {
        "ParentReference": ObjectReferenceTypeDef,
        "LinkName": str,
        "BatchReferenceName": NotRequired[str],
    },
)
BatchDetachPolicyTypeDef = TypedDict(
    "BatchDetachPolicyTypeDef",
    {
        "PolicyReference": ObjectReferenceTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
BatchGetObjectInformationTypeDef = TypedDict(
    "BatchGetObjectInformationTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
BatchListAttachedIndicesTypeDef = TypedDict(
    "BatchListAttachedIndicesTypeDef",
    {
        "TargetReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchListObjectChildrenTypeDef = TypedDict(
    "BatchListObjectChildrenTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchListObjectParentPathsTypeDef = TypedDict(
    "BatchListObjectParentPathsTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchListObjectParentsTypeDef = TypedDict(
    "BatchListObjectParentsTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchListObjectPoliciesTypeDef = TypedDict(
    "BatchListObjectPoliciesTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchListPolicyAttachmentsTypeDef = TypedDict(
    "BatchListPolicyAttachmentsTypeDef",
    {
        "PolicyReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchLookupPolicyTypeDef = TypedDict(
    "BatchLookupPolicyTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DeleteObjectRequestRequestTypeDef = TypedDict(
    "DeleteObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
DetachFromIndexRequestRequestTypeDef = TypedDict(
    "DetachFromIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": ObjectReferenceTypeDef,
        "TargetReference": ObjectReferenceTypeDef,
    },
)
DetachObjectRequestRequestTypeDef = TypedDict(
    "DetachObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ParentReference": ObjectReferenceTypeDef,
        "LinkName": str,
    },
)
DetachPolicyRequestRequestTypeDef = TypedDict(
    "DetachPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": ObjectReferenceTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
GetObjectInformationRequestRequestTypeDef = TypedDict(
    "GetObjectInformationRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListAttachedIndicesRequestRequestTypeDef = TypedDict(
    "ListAttachedIndicesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TargetReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListObjectChildrenRequestRequestTypeDef = TypedDict(
    "ListObjectChildrenRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListObjectParentPathsRequestRequestTypeDef = TypedDict(
    "ListObjectParentPathsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListObjectParentsRequestRequestTypeDef = TypedDict(
    "ListObjectParentsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "IncludeAllLinksToEachParent": NotRequired[bool],
    },
)
ListObjectPoliciesRequestRequestTypeDef = TypedDict(
    "ListObjectPoliciesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListPolicyAttachmentsRequestRequestTypeDef = TypedDict(
    "ListPolicyAttachmentsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
LookupPolicyRequestRequestTypeDef = TypedDict(
    "LookupPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchGetObjectAttributesTypeDef = TypedDict(
    "BatchGetObjectAttributesTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "SchemaFacet": SchemaFacetTypeDef,
        "AttributeNames": Sequence[str],
    },
)
BatchGetObjectInformationResponseTypeDef = TypedDict(
    "BatchGetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": NotRequired[List[SchemaFacetTypeDef]],
        "ObjectIdentifier": NotRequired[str],
    },
)
BatchListObjectAttributesTypeDef = TypedDict(
    "BatchListObjectAttributesTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "FacetFilter": NotRequired[SchemaFacetTypeDef],
    },
)
BatchRemoveFacetFromObjectTypeDef = TypedDict(
    "BatchRemoveFacetFromObjectTypeDef",
    {
        "SchemaFacet": SchemaFacetTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
GetObjectAttributesRequestRequestTypeDef = TypedDict(
    "GetObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "SchemaFacet": SchemaFacetTypeDef,
        "AttributeNames": Sequence[str],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListObjectAttributesRequestRequestTypeDef = TypedDict(
    "ListObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "FacetFilter": NotRequired[SchemaFacetTypeDef],
    },
)
RemoveFacetFromObjectRequestRequestTypeDef = TypedDict(
    "RemoveFacetFromObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacet": SchemaFacetTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
ApplySchemaResponseTypeDef = TypedDict(
    "ApplySchemaResponseTypeDef",
    {
        "AppliedSchemaArn": str,
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachObjectResponseTypeDef = TypedDict(
    "AttachObjectResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachToIndexResponseTypeDef = TypedDict(
    "AttachToIndexResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDirectoryResponseTypeDef = TypedDict(
    "CreateDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "Name": str,
        "ObjectIdentifier": str,
        "AppliedSchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateObjectResponseTypeDef = TypedDict(
    "CreateObjectResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDirectoryResponseTypeDef = TypedDict(
    "DeleteDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSchemaResponseTypeDef = TypedDict(
    "DeleteSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachFromIndexResponseTypeDef = TypedDict(
    "DetachFromIndexResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachObjectResponseTypeDef = TypedDict(
    "DetachObjectResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableDirectoryResponseTypeDef = TypedDict(
    "DisableDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableDirectoryResponseTypeDef = TypedDict(
    "EnableDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppliedSchemaVersionResponseTypeDef = TypedDict(
    "GetAppliedSchemaVersionResponseTypeDef",
    {
        "AppliedSchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetObjectInformationResponseTypeDef = TypedDict(
    "GetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": List[SchemaFacetTypeDef],
        "ObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSchemaAsJsonResponseTypeDef = TypedDict(
    "GetSchemaAsJsonResponseTypeDef",
    {
        "Name": str,
        "Document": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTypedLinkFacetInformationResponseTypeDef = TypedDict(
    "GetTypedLinkFacetInformationResponseTypeDef",
    {
        "IdentityAttributeOrder": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAppliedSchemaArnsResponseTypeDef = TypedDict(
    "ListAppliedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDevelopmentSchemaArnsResponseTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFacetNamesResponseTypeDef = TypedDict(
    "ListFacetNamesResponseTypeDef",
    {
        "FacetNames": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListManagedSchemaArnsResponseTypeDef = TypedDict(
    "ListManagedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListObjectChildrenResponseTypeDef = TypedDict(
    "ListObjectChildrenResponseTypeDef",
    {
        "Children": Dict[str, str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListObjectPoliciesResponseTypeDef = TypedDict(
    "ListObjectPoliciesResponseTypeDef",
    {
        "AttachedPolicyIds": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPolicyAttachmentsResponseTypeDef = TypedDict(
    "ListPolicyAttachmentsResponseTypeDef",
    {
        "ObjectIdentifiers": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPublishedSchemaArnsResponseTypeDef = TypedDict(
    "ListPublishedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTypedLinkFacetNamesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetNamesResponseTypeDef",
    {
        "FacetNames": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PublishSchemaResponseTypeDef = TypedDict(
    "PublishSchemaResponseTypeDef",
    {
        "PublishedSchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSchemaFromJsonResponseTypeDef = TypedDict(
    "PutSchemaFromJsonResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateObjectAttributesResponseTypeDef = TypedDict(
    "UpdateObjectAttributesResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpgradeAppliedSchemaResponseTypeDef = TypedDict(
    "UpgradeAppliedSchemaResponseTypeDef",
    {
        "UpgradedSchemaArn": str,
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpgradePublishedSchemaResponseTypeDef = TypedDict(
    "UpgradePublishedSchemaResponseTypeDef",
    {
        "UpgradedSchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchCreateIndexTypeDef = TypedDict(
    "BatchCreateIndexTypeDef",
    {
        "OrderedIndexedAttributeList": Sequence[AttributeKeyTypeDef],
        "IsUnique": bool,
        "ParentReference": NotRequired[ObjectReferenceTypeDef],
        "LinkName": NotRequired[str],
        "BatchReferenceName": NotRequired[str],
    },
)
CreateIndexRequestRequestTypeDef = TypedDict(
    "CreateIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "OrderedIndexedAttributeList": Sequence[AttributeKeyTypeDef],
        "IsUnique": bool,
        "ParentReference": NotRequired[ObjectReferenceTypeDef],
        "LinkName": NotRequired[str],
    },
)
AttributeKeyAndValuePaginatorTypeDef = TypedDict(
    "AttributeKeyAndValuePaginatorTypeDef",
    {
        "Key": AttributeKeyTypeDef,
        "Value": TypedAttributeValuePaginatorTypeDef,
    },
)
AttributeNameAndValuePaginatorTypeDef = TypedDict(
    "AttributeNameAndValuePaginatorTypeDef",
    {
        "AttributeName": str,
        "Value": TypedAttributeValuePaginatorTypeDef,
    },
)
TypedAttributeValueRangePaginatorTypeDef = TypedDict(
    "TypedAttributeValueRangePaginatorTypeDef",
    {
        "StartMode": RangeModeType,
        "EndMode": RangeModeType,
        "StartValue": NotRequired[TypedAttributeValuePaginatorTypeDef],
        "EndValue": NotRequired[TypedAttributeValuePaginatorTypeDef],
    },
)
BatchListObjectParentPathsResponseTypeDef = TypedDict(
    "BatchListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": NotRequired[List[PathToObjectIdentifiersTypeDef]],
        "NextToken": NotRequired[str],
    },
)
ListObjectParentPathsResponseTypeDef = TypedDict(
    "ListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List[PathToObjectIdentifiersTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchListObjectParentsResponseTypeDef = TypedDict(
    "BatchListObjectParentsResponseTypeDef",
    {
        "ParentLinks": NotRequired[List[ObjectIdentifierAndLinkNameTupleTypeDef]],
        "NextToken": NotRequired[str],
    },
)
ListObjectParentsResponseTypeDef = TypedDict(
    "ListObjectParentsResponseTypeDef",
    {
        "Parents": Dict[str, str],
        "NextToken": str,
        "ParentLinks": List[ObjectIdentifierAndLinkNameTupleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDirectoryResponseTypeDef = TypedDict(
    "GetDirectoryResponseTypeDef",
    {
        "Directory": DirectoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDirectoriesResponseTypeDef = TypedDict(
    "ListDirectoriesResponseTypeDef",
    {
        "Directories": List[DirectoryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FacetAttributeDefinitionPaginatorTypeDef = TypedDict(
    "FacetAttributeDefinitionPaginatorTypeDef",
    {
        "Type": FacetAttributeTypeType,
        "DefaultValue": NotRequired[TypedAttributeValuePaginatorTypeDef],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Dict[str, RulePaginatorTypeDef]],
    },
)
TypedLinkAttributeDefinitionPaginatorTypeDef = TypedDict(
    "TypedLinkAttributeDefinitionPaginatorTypeDef",
    {
        "Name": str,
        "Type": FacetAttributeTypeType,
        "RequiredBehavior": RequiredAttributeBehaviorType,
        "DefaultValue": NotRequired[TypedAttributeValuePaginatorTypeDef],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Dict[str, RulePaginatorTypeDef]],
    },
)
GetFacetResponseTypeDef = TypedDict(
    "GetFacetResponseTypeDef",
    {
        "Facet": FacetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef = TypedDict(
    "ListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef",
    {
        "DirectoryArn": str,
        "SchemaArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef = TypedDict(
    "ListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef",
    {
        "DirectoryArn": str,
        "TargetReference": ObjectReferenceTypeDef,
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDevelopmentSchemaArnsRequestListDevelopmentSchemaArnsPaginateTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsRequestListDevelopmentSchemaArnsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDirectoriesRequestListDirectoriesPaginateTypeDef = TypedDict(
    "ListDirectoriesRequestListDirectoriesPaginateTypeDef",
    {
        "state": NotRequired[DirectoryStateType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFacetAttributesRequestListFacetAttributesPaginateTypeDef = TypedDict(
    "ListFacetAttributesRequestListFacetAttributesPaginateTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFacetNamesRequestListFacetNamesPaginateTypeDef = TypedDict(
    "ListFacetNamesRequestListFacetNamesPaginateTypeDef",
    {
        "SchemaArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListManagedSchemaArnsRequestListManagedSchemaArnsPaginateTypeDef = TypedDict(
    "ListManagedSchemaArnsRequestListManagedSchemaArnsPaginateTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListObjectAttributesRequestListObjectAttributesPaginateTypeDef = TypedDict(
    "ListObjectAttributesRequestListObjectAttributesPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "FacetFilter": NotRequired[SchemaFacetTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef = TypedDict(
    "ListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef = TypedDict(
    "ListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef = TypedDict(
    "ListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": ObjectReferenceTypeDef,
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPublishedSchemaArnsRequestListPublishedSchemaArnsPaginateTypeDef = TypedDict(
    "ListPublishedSchemaArnsRequestListPublishedSchemaArnsPaginateTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef = TypedDict(
    "ListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef",
    {
        "SchemaArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
LookupPolicyRequestLookupPolicyPaginateTypeDef = TypedDict(
    "LookupPolicyRequestLookupPolicyPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
PolicyToPathTypeDef = TypedDict(
    "PolicyToPathTypeDef",
    {
        "Path": NotRequired[str],
        "Policies": NotRequired[List[PolicyAttachmentTypeDef]],
    },
)
TypedAttributeValueTypeDef = TypedDict(
    "TypedAttributeValueTypeDef",
    {
        "StringValue": NotRequired[str],
        "BinaryValue": NotRequired[BlobTypeDef],
        "BooleanValue": NotRequired[bool],
        "NumberValue": NotRequired[str],
        "DatetimeValue": NotRequired[TimestampTypeDef],
    },
)
IndexAttachmentPaginatorTypeDef = TypedDict(
    "IndexAttachmentPaginatorTypeDef",
    {
        "IndexedAttributes": NotRequired[List[AttributeKeyAndValuePaginatorTypeDef]],
        "ObjectIdentifier": NotRequired[str],
    },
)
ListObjectAttributesResponsePaginatorTypeDef = TypedDict(
    "ListObjectAttributesResponsePaginatorTypeDef",
    {
        "Attributes": List[AttributeKeyAndValuePaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TypedLinkSpecifierPaginatorTypeDef = TypedDict(
    "TypedLinkSpecifierPaginatorTypeDef",
    {
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "IdentityAttributeValues": List[AttributeNameAndValuePaginatorTypeDef],
    },
)
ObjectAttributeRangePaginatorTypeDef = TypedDict(
    "ObjectAttributeRangePaginatorTypeDef",
    {
        "AttributeKey": NotRequired[AttributeKeyTypeDef],
        "Range": NotRequired[TypedAttributeValueRangePaginatorTypeDef],
    },
)
TypedLinkAttributeRangePaginatorTypeDef = TypedDict(
    "TypedLinkAttributeRangePaginatorTypeDef",
    {
        "Range": TypedAttributeValueRangePaginatorTypeDef,
        "AttributeName": NotRequired[str],
    },
)
FacetAttributePaginatorTypeDef = TypedDict(
    "FacetAttributePaginatorTypeDef",
    {
        "Name": str,
        "AttributeDefinition": NotRequired[FacetAttributeDefinitionPaginatorTypeDef],
        "AttributeReference": NotRequired[FacetAttributeReferenceTypeDef],
        "RequiredBehavior": NotRequired[RequiredAttributeBehaviorType],
    },
)
ListTypedLinkFacetAttributesResponsePaginatorTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesResponsePaginatorTypeDef",
    {
        "Attributes": List[TypedLinkAttributeDefinitionPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchLookupPolicyResponseTypeDef = TypedDict(
    "BatchLookupPolicyResponseTypeDef",
    {
        "PolicyToPathList": NotRequired[List[PolicyToPathTypeDef]],
        "NextToken": NotRequired[str],
    },
)
LookupPolicyResponseTypeDef = TypedDict(
    "LookupPolicyResponseTypeDef",
    {
        "PolicyToPathList": List[PolicyToPathTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttributeKeyAndValueTypeDef = TypedDict(
    "AttributeKeyAndValueTypeDef",
    {
        "Key": AttributeKeyTypeDef,
        "Value": TypedAttributeValueTypeDef,
    },
)
AttributeNameAndValueTypeDef = TypedDict(
    "AttributeNameAndValueTypeDef",
    {
        "AttributeName": str,
        "Value": TypedAttributeValueTypeDef,
    },
)
FacetAttributeDefinitionTypeDef = TypedDict(
    "FacetAttributeDefinitionTypeDef",
    {
        "Type": FacetAttributeTypeType,
        "DefaultValue": NotRequired[TypedAttributeValueTypeDef],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Mapping[str, RuleTypeDef]],
    },
)
LinkAttributeActionTypeDef = TypedDict(
    "LinkAttributeActionTypeDef",
    {
        "AttributeActionType": NotRequired[UpdateActionTypeType],
        "AttributeUpdateValue": NotRequired[TypedAttributeValueTypeDef],
    },
)
ObjectAttributeActionTypeDef = TypedDict(
    "ObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": NotRequired[UpdateActionTypeType],
        "ObjectAttributeUpdateValue": NotRequired[TypedAttributeValueTypeDef],
    },
)
TypedAttributeValueRangeTypeDef = TypedDict(
    "TypedAttributeValueRangeTypeDef",
    {
        "StartMode": RangeModeType,
        "EndMode": RangeModeType,
        "StartValue": NotRequired[TypedAttributeValueTypeDef],
        "EndValue": NotRequired[TypedAttributeValueTypeDef],
    },
)
TypedLinkAttributeDefinitionTypeDef = TypedDict(
    "TypedLinkAttributeDefinitionTypeDef",
    {
        "Name": str,
        "Type": FacetAttributeTypeType,
        "RequiredBehavior": RequiredAttributeBehaviorType,
        "DefaultValue": NotRequired[TypedAttributeValueTypeDef],
        "IsImmutable": NotRequired[bool],
        "Rules": NotRequired[Mapping[str, RuleTypeDef]],
    },
)
ListAttachedIndicesResponsePaginatorTypeDef = TypedDict(
    "ListAttachedIndicesResponsePaginatorTypeDef",
    {
        "IndexAttachments": List[IndexAttachmentPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIndexResponsePaginatorTypeDef = TypedDict(
    "ListIndexResponsePaginatorTypeDef",
    {
        "IndexAttachments": List[IndexAttachmentPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIncomingTypedLinksResponsePaginatorTypeDef = TypedDict(
    "ListIncomingTypedLinksResponsePaginatorTypeDef",
    {
        "LinkSpecifiers": List[TypedLinkSpecifierPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOutgoingTypedLinksResponsePaginatorTypeDef = TypedDict(
    "ListOutgoingTypedLinksResponsePaginatorTypeDef",
    {
        "TypedLinkSpecifiers": List[TypedLinkSpecifierPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIndexRequestListIndexPaginateTypeDef = TypedDict(
    "ListIndexRequestListIndexPaginateTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": ObjectReferenceTypeDef,
        "RangesOnIndexedValues": NotRequired[Sequence[ObjectAttributeRangePaginatorTypeDef]],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef = TypedDict(
    "ListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "FilterAttributeRanges": NotRequired[Sequence[TypedLinkAttributeRangePaginatorTypeDef]],
        "FilterTypedLink": NotRequired[TypedLinkSchemaAndFacetNameTypeDef],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef = TypedDict(
    "ListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "FilterAttributeRanges": NotRequired[Sequence[TypedLinkAttributeRangePaginatorTypeDef]],
        "FilterTypedLink": NotRequired[TypedLinkSchemaAndFacetNameTypeDef],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFacetAttributesResponsePaginatorTypeDef = TypedDict(
    "ListFacetAttributesResponsePaginatorTypeDef",
    {
        "Attributes": List[FacetAttributePaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddFacetToObjectRequestRequestTypeDef = TypedDict(
    "AddFacetToObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacet": SchemaFacetTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
        "ObjectAttributeList": NotRequired[Sequence[AttributeKeyAndValueTypeDef]],
    },
)
BatchAddFacetToObjectTypeDef = TypedDict(
    "BatchAddFacetToObjectTypeDef",
    {
        "SchemaFacet": SchemaFacetTypeDef,
        "ObjectAttributeList": Sequence[AttributeKeyAndValueTypeDef],
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
BatchCreateObjectTypeDef = TypedDict(
    "BatchCreateObjectTypeDef",
    {
        "SchemaFacet": Sequence[SchemaFacetTypeDef],
        "ObjectAttributeList": Sequence[AttributeKeyAndValueTypeDef],
        "ParentReference": NotRequired[ObjectReferenceTypeDef],
        "LinkName": NotRequired[str],
        "BatchReferenceName": NotRequired[str],
    },
)
BatchGetLinkAttributesResponseTypeDef = TypedDict(
    "BatchGetLinkAttributesResponseTypeDef",
    {
        "Attributes": NotRequired[List[AttributeKeyAndValueTypeDef]],
    },
)
BatchGetObjectAttributesResponseTypeDef = TypedDict(
    "BatchGetObjectAttributesResponseTypeDef",
    {
        "Attributes": NotRequired[List[AttributeKeyAndValueTypeDef]],
    },
)
BatchListObjectAttributesResponseTypeDef = TypedDict(
    "BatchListObjectAttributesResponseTypeDef",
    {
        "Attributes": NotRequired[List[AttributeKeyAndValueTypeDef]],
        "NextToken": NotRequired[str],
    },
)
CreateObjectRequestRequestTypeDef = TypedDict(
    "CreateObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacets": Sequence[SchemaFacetTypeDef],
        "ObjectAttributeList": NotRequired[Sequence[AttributeKeyAndValueTypeDef]],
        "ParentReference": NotRequired[ObjectReferenceTypeDef],
        "LinkName": NotRequired[str],
    },
)
GetLinkAttributesResponseTypeDef = TypedDict(
    "GetLinkAttributesResponseTypeDef",
    {
        "Attributes": List[AttributeKeyAndValueTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetObjectAttributesResponseTypeDef = TypedDict(
    "GetObjectAttributesResponseTypeDef",
    {
        "Attributes": List[AttributeKeyAndValueTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IndexAttachmentTypeDef = TypedDict(
    "IndexAttachmentTypeDef",
    {
        "IndexedAttributes": NotRequired[List[AttributeKeyAndValueTypeDef]],
        "ObjectIdentifier": NotRequired[str],
    },
)
ListObjectAttributesResponseTypeDef = TypedDict(
    "ListObjectAttributesResponseTypeDef",
    {
        "Attributes": List[AttributeKeyAndValueTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachTypedLinkRequestRequestTypeDef = TypedDict(
    "AttachTypedLinkRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "Attributes": Sequence[AttributeNameAndValueTypeDef],
    },
)
BatchAttachTypedLinkTypeDef = TypedDict(
    "BatchAttachTypedLinkTypeDef",
    {
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "Attributes": Sequence[AttributeNameAndValueTypeDef],
    },
)
TypedLinkSpecifierTypeDef = TypedDict(
    "TypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "IdentityAttributeValues": List[AttributeNameAndValueTypeDef],
    },
)
FacetAttributeTypeDef = TypedDict(
    "FacetAttributeTypeDef",
    {
        "Name": str,
        "AttributeDefinition": NotRequired[FacetAttributeDefinitionTypeDef],
        "AttributeReference": NotRequired[FacetAttributeReferenceTypeDef],
        "RequiredBehavior": NotRequired[RequiredAttributeBehaviorType],
    },
)
LinkAttributeUpdateTypeDef = TypedDict(
    "LinkAttributeUpdateTypeDef",
    {
        "AttributeKey": NotRequired[AttributeKeyTypeDef],
        "AttributeAction": NotRequired[LinkAttributeActionTypeDef],
    },
)
ObjectAttributeUpdateTypeDef = TypedDict(
    "ObjectAttributeUpdateTypeDef",
    {
        "ObjectAttributeKey": NotRequired[AttributeKeyTypeDef],
        "ObjectAttributeAction": NotRequired[ObjectAttributeActionTypeDef],
    },
)
ObjectAttributeRangeTypeDef = TypedDict(
    "ObjectAttributeRangeTypeDef",
    {
        "AttributeKey": NotRequired[AttributeKeyTypeDef],
        "Range": NotRequired[TypedAttributeValueRangeTypeDef],
    },
)
TypedLinkAttributeRangeTypeDef = TypedDict(
    "TypedLinkAttributeRangeTypeDef",
    {
        "Range": TypedAttributeValueRangeTypeDef,
        "AttributeName": NotRequired[str],
    },
)
ListTypedLinkFacetAttributesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesResponseTypeDef",
    {
        "Attributes": List[TypedLinkAttributeDefinitionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TypedLinkFacetAttributeUpdateTypeDef = TypedDict(
    "TypedLinkFacetAttributeUpdateTypeDef",
    {
        "Attribute": TypedLinkAttributeDefinitionTypeDef,
        "Action": UpdateActionTypeType,
    },
)
TypedLinkFacetTypeDef = TypedDict(
    "TypedLinkFacetTypeDef",
    {
        "Name": str,
        "Attributes": Sequence[TypedLinkAttributeDefinitionTypeDef],
        "IdentityAttributeOrder": Sequence[str],
    },
)
BatchListAttachedIndicesResponseTypeDef = TypedDict(
    "BatchListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": NotRequired[List[IndexAttachmentTypeDef]],
        "NextToken": NotRequired[str],
    },
)
BatchListIndexResponseTypeDef = TypedDict(
    "BatchListIndexResponseTypeDef",
    {
        "IndexAttachments": NotRequired[List[IndexAttachmentTypeDef]],
        "NextToken": NotRequired[str],
    },
)
ListAttachedIndicesResponseTypeDef = TypedDict(
    "ListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": List[IndexAttachmentTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIndexResponseTypeDef = TypedDict(
    "ListIndexResponseTypeDef",
    {
        "IndexAttachments": List[IndexAttachmentTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachTypedLinkResponseTypeDef = TypedDict(
    "AttachTypedLinkResponseTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchAttachTypedLinkResponseTypeDef = TypedDict(
    "BatchAttachTypedLinkResponseTypeDef",
    {
        "TypedLinkSpecifier": NotRequired[TypedLinkSpecifierTypeDef],
    },
)
BatchDetachTypedLinkTypeDef = TypedDict(
    "BatchDetachTypedLinkTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
    },
)
BatchGetLinkAttributesTypeDef = TypedDict(
    "BatchGetLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
        "AttributeNames": Sequence[str],
    },
)
BatchListIncomingTypedLinksResponseTypeDef = TypedDict(
    "BatchListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": NotRequired[List[TypedLinkSpecifierTypeDef]],
        "NextToken": NotRequired[str],
    },
)
BatchListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "BatchListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": NotRequired[List[TypedLinkSpecifierTypeDef]],
        "NextToken": NotRequired[str],
    },
)
DetachTypedLinkRequestRequestTypeDef = TypedDict(
    "DetachTypedLinkRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
    },
)
GetLinkAttributesRequestRequestTypeDef = TypedDict(
    "GetLinkAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
        "AttributeNames": Sequence[str],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListIncomingTypedLinksResponseTypeDef = TypedDict(
    "ListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": List[TypedLinkSpecifierTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "ListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": List[TypedLinkSpecifierTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFacetRequestRequestTypeDef = TypedDict(
    "CreateFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "Attributes": NotRequired[Sequence[FacetAttributeTypeDef]],
        "ObjectType": NotRequired[ObjectTypeType],
        "FacetStyle": NotRequired[FacetStyleType],
    },
)
FacetAttributeUpdateTypeDef = TypedDict(
    "FacetAttributeUpdateTypeDef",
    {
        "Attribute": NotRequired[FacetAttributeTypeDef],
        "Action": NotRequired[UpdateActionTypeType],
    },
)
ListFacetAttributesResponseTypeDef = TypedDict(
    "ListFacetAttributesResponseTypeDef",
    {
        "Attributes": List[FacetAttributeTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateLinkAttributesTypeDef = TypedDict(
    "BatchUpdateLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
        "AttributeUpdates": Sequence[LinkAttributeUpdateTypeDef],
    },
)
UpdateLinkAttributesRequestRequestTypeDef = TypedDict(
    "UpdateLinkAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
        "AttributeUpdates": Sequence[LinkAttributeUpdateTypeDef],
    },
)
BatchUpdateObjectAttributesTypeDef = TypedDict(
    "BatchUpdateObjectAttributesTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "AttributeUpdates": Sequence[ObjectAttributeUpdateTypeDef],
    },
)
UpdateObjectAttributesRequestRequestTypeDef = TypedDict(
    "UpdateObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "AttributeUpdates": Sequence[ObjectAttributeUpdateTypeDef],
    },
)
BatchListIndexTypeDef = TypedDict(
    "BatchListIndexTypeDef",
    {
        "IndexReference": ObjectReferenceTypeDef,
        "RangesOnIndexedValues": NotRequired[Sequence[ObjectAttributeRangeTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListIndexRequestRequestTypeDef = TypedDict(
    "ListIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": ObjectReferenceTypeDef,
        "RangesOnIndexedValues": NotRequired[Sequence[ObjectAttributeRangeTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
BatchListIncomingTypedLinksTypeDef = TypedDict(
    "BatchListIncomingTypedLinksTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "FilterAttributeRanges": NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]],
        "FilterTypedLink": NotRequired[TypedLinkSchemaAndFacetNameTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchListOutgoingTypedLinksTypeDef = TypedDict(
    "BatchListOutgoingTypedLinksTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "FilterAttributeRanges": NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]],
        "FilterTypedLink": NotRequired[TypedLinkSchemaAndFacetNameTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIncomingTypedLinksRequestRequestTypeDef = TypedDict(
    "ListIncomingTypedLinksRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "FilterAttributeRanges": NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]],
        "FilterTypedLink": NotRequired[TypedLinkSchemaAndFacetNameTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
ListOutgoingTypedLinksRequestRequestTypeDef = TypedDict(
    "ListOutgoingTypedLinksRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "FilterAttributeRanges": NotRequired[Sequence[TypedLinkAttributeRangeTypeDef]],
        "FilterTypedLink": NotRequired[TypedLinkSchemaAndFacetNameTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
UpdateTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "UpdateTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "AttributeUpdates": Sequence[TypedLinkFacetAttributeUpdateTypeDef],
        "IdentityAttributeOrder": Sequence[str],
    },
)
CreateTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "CreateTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Facet": TypedLinkFacetTypeDef,
    },
)
BatchWriteOperationResponseTypeDef = TypedDict(
    "BatchWriteOperationResponseTypeDef",
    {
        "CreateObject": NotRequired[BatchCreateObjectResponseTypeDef],
        "AttachObject": NotRequired[BatchAttachObjectResponseTypeDef],
        "DetachObject": NotRequired[BatchDetachObjectResponseTypeDef],
        "UpdateObjectAttributes": NotRequired[BatchUpdateObjectAttributesResponseTypeDef],
        "DeleteObject": NotRequired[Dict[str, Any]],
        "AddFacetToObject": NotRequired[Dict[str, Any]],
        "RemoveFacetFromObject": NotRequired[Dict[str, Any]],
        "AttachPolicy": NotRequired[Dict[str, Any]],
        "DetachPolicy": NotRequired[Dict[str, Any]],
        "CreateIndex": NotRequired[BatchCreateIndexResponseTypeDef],
        "AttachToIndex": NotRequired[BatchAttachToIndexResponseTypeDef],
        "DetachFromIndex": NotRequired[BatchDetachFromIndexResponseTypeDef],
        "AttachTypedLink": NotRequired[BatchAttachTypedLinkResponseTypeDef],
        "DetachTypedLink": NotRequired[Dict[str, Any]],
        "UpdateLinkAttributes": NotRequired[Dict[str, Any]],
    },
)
BatchReadSuccessfulResponseTypeDef = TypedDict(
    "BatchReadSuccessfulResponseTypeDef",
    {
        "ListObjectAttributes": NotRequired[BatchListObjectAttributesResponseTypeDef],
        "ListObjectChildren": NotRequired[BatchListObjectChildrenResponseTypeDef],
        "GetObjectInformation": NotRequired[BatchGetObjectInformationResponseTypeDef],
        "GetObjectAttributes": NotRequired[BatchGetObjectAttributesResponseTypeDef],
        "ListAttachedIndices": NotRequired[BatchListAttachedIndicesResponseTypeDef],
        "ListObjectParentPaths": NotRequired[BatchListObjectParentPathsResponseTypeDef],
        "ListObjectPolicies": NotRequired[BatchListObjectPoliciesResponseTypeDef],
        "ListPolicyAttachments": NotRequired[BatchListPolicyAttachmentsResponseTypeDef],
        "LookupPolicy": NotRequired[BatchLookupPolicyResponseTypeDef],
        "ListIndex": NotRequired[BatchListIndexResponseTypeDef],
        "ListOutgoingTypedLinks": NotRequired[BatchListOutgoingTypedLinksResponseTypeDef],
        "ListIncomingTypedLinks": NotRequired[BatchListIncomingTypedLinksResponseTypeDef],
        "GetLinkAttributes": NotRequired[BatchGetLinkAttributesResponseTypeDef],
        "ListObjectParents": NotRequired[BatchListObjectParentsResponseTypeDef],
    },
)
UpdateFacetRequestRequestTypeDef = TypedDict(
    "UpdateFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "AttributeUpdates": NotRequired[Sequence[FacetAttributeUpdateTypeDef]],
        "ObjectType": NotRequired[ObjectTypeType],
    },
)
BatchWriteOperationTypeDef = TypedDict(
    "BatchWriteOperationTypeDef",
    {
        "CreateObject": NotRequired[BatchCreateObjectTypeDef],
        "AttachObject": NotRequired[BatchAttachObjectTypeDef],
        "DetachObject": NotRequired[BatchDetachObjectTypeDef],
        "UpdateObjectAttributes": NotRequired[BatchUpdateObjectAttributesTypeDef],
        "DeleteObject": NotRequired[BatchDeleteObjectTypeDef],
        "AddFacetToObject": NotRequired[BatchAddFacetToObjectTypeDef],
        "RemoveFacetFromObject": NotRequired[BatchRemoveFacetFromObjectTypeDef],
        "AttachPolicy": NotRequired[BatchAttachPolicyTypeDef],
        "DetachPolicy": NotRequired[BatchDetachPolicyTypeDef],
        "CreateIndex": NotRequired[BatchCreateIndexTypeDef],
        "AttachToIndex": NotRequired[BatchAttachToIndexTypeDef],
        "DetachFromIndex": NotRequired[BatchDetachFromIndexTypeDef],
        "AttachTypedLink": NotRequired[BatchAttachTypedLinkTypeDef],
        "DetachTypedLink": NotRequired[BatchDetachTypedLinkTypeDef],
        "UpdateLinkAttributes": NotRequired[BatchUpdateLinkAttributesTypeDef],
    },
)
BatchReadOperationTypeDef = TypedDict(
    "BatchReadOperationTypeDef",
    {
        "ListObjectAttributes": NotRequired[BatchListObjectAttributesTypeDef],
        "ListObjectChildren": NotRequired[BatchListObjectChildrenTypeDef],
        "ListAttachedIndices": NotRequired[BatchListAttachedIndicesTypeDef],
        "ListObjectParentPaths": NotRequired[BatchListObjectParentPathsTypeDef],
        "GetObjectInformation": NotRequired[BatchGetObjectInformationTypeDef],
        "GetObjectAttributes": NotRequired[BatchGetObjectAttributesTypeDef],
        "ListObjectParents": NotRequired[BatchListObjectParentsTypeDef],
        "ListObjectPolicies": NotRequired[BatchListObjectPoliciesTypeDef],
        "ListPolicyAttachments": NotRequired[BatchListPolicyAttachmentsTypeDef],
        "LookupPolicy": NotRequired[BatchLookupPolicyTypeDef],
        "ListIndex": NotRequired[BatchListIndexTypeDef],
        "ListOutgoingTypedLinks": NotRequired[BatchListOutgoingTypedLinksTypeDef],
        "ListIncomingTypedLinks": NotRequired[BatchListIncomingTypedLinksTypeDef],
        "GetLinkAttributes": NotRequired[BatchGetLinkAttributesTypeDef],
    },
)
BatchWriteResponseTypeDef = TypedDict(
    "BatchWriteResponseTypeDef",
    {
        "Responses": List[BatchWriteOperationResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchReadOperationResponseTypeDef = TypedDict(
    "BatchReadOperationResponseTypeDef",
    {
        "SuccessfulResponse": NotRequired[BatchReadSuccessfulResponseTypeDef],
        "ExceptionResponse": NotRequired[BatchReadExceptionTypeDef],
    },
)
BatchWriteRequestRequestTypeDef = TypedDict(
    "BatchWriteRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "Operations": Sequence[BatchWriteOperationTypeDef],
    },
)
BatchReadRequestRequestTypeDef = TypedDict(
    "BatchReadRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "Operations": Sequence[BatchReadOperationTypeDef],
        "ConsistencyLevel": NotRequired[ConsistencyLevelType],
    },
)
BatchReadResponseTypeDef = TypedDict(
    "BatchReadResponseTypeDef",
    {
        "Responses": List[BatchReadOperationResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
