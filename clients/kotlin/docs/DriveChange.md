
# DriveChange

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **kind** | [**inline**](#Kind) |  |  |
| **changeSeq** | **kotlin.Long** |  |  |
| **id** | [**java.util.UUID**](java.util.UUID.md) |  |  [optional] |
| **name** | **kotlin.String** |  |  [optional] |
| **folderId** | [**java.util.UUID**](java.util.UUID.md) |  |  [optional] |
| **parentId** | [**java.util.UUID**](java.util.UUID.md) |  |  [optional] |
| **path** | **kotlin.String** | Materialized folder path (folders). |  [optional] |
| **etag** | **kotlin.String** | Content hash (files). |  [optional] |
| **propertySize** | **kotlin.Long** |  |  [optional] |
| **mimeType** | **kotlin.String** |  |  [optional] |
| **trashed** | **kotlin.Boolean** |  |  [optional] |
| **target** | [**inline**](#Target) | Deleted item kind. |  [optional] |
| **deletedAt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] |


<a id="Kind"></a>
## Enum: kind
| Name | Value |
| ---- | ----- |
| kind | file, folder, deleted |


<a id="Target"></a>
## Enum: target
| Name | Value |
| ---- | ----- |
| target | file, folder |



