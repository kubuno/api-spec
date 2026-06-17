# DriveSyncApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**apiV1DriveSyncDeltaGet**](DriveSyncApi.md#apiV1DriveSyncDeltaGet) | **GET** /api/v1/drive/sync/delta | Changes since a cursor (delta sync). |
| [**apiV1DriveSyncFileIdContentPut**](DriveSyncApi.md#apiV1DriveSyncFileIdContentPut) | **PUT** /api/v1/drive/sync/file/{id}/content | Replace a file&#39;s content (conflict-safe). |


<a id="apiV1DriveSyncDeltaGet"></a>
# **apiV1DriveSyncDeltaGet**
> DriveDelta apiV1DriveSyncDeltaGet(cursor, limit)

Changes since a cursor (delta sync).

### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = DriveSyncApi()
val cursor : kotlin.Long = 789 // kotlin.Long | Last change_seq seen (0 = full snapshot).
val limit : kotlin.Int = 56 // kotlin.Int | 
try {
    val result : DriveDelta = apiInstance.apiV1DriveSyncDeltaGet(cursor, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DriveSyncApi#apiV1DriveSyncDeltaGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DriveSyncApi#apiV1DriveSyncDeltaGet")
    e.printStackTrace()
}
```

### Parameters
| **cursor** | **kotlin.Long**| Last change_seq seen (0 &#x3D; full snapshot). | [optional] [default to 0L] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **kotlin.Int**|  | [optional] [default to 500] |

### Return type

[**DriveDelta**](DriveDelta.md)

### Authorization


Configure bearer statically:
```kotlin
ApiClient.accessToken = ""
```
Configure bearer dynamically:
```kotlin
apiInstance.accessTokenProvider = { "" }
```

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="apiV1DriveSyncFileIdContentPut"></a>
# **apiV1DriveSyncFileIdContentPut**
> apiV1DriveSyncFileIdContentPut(id, body, ifMatch, idempotencyKey)

Replace a file&#39;s content (conflict-safe).

### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = DriveSyncApi()
val id : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val body : java.io.File = BINARY_DATA_HERE // java.io.File | 
val ifMatch : kotlin.String = ifMatch_example // kotlin.String | Expected etag; mismatch returns 412 (conflict).
val idempotencyKey : kotlin.String = idempotencyKey_example // kotlin.String | Stable key so a replayed mutation is not applied twice.
try {
    apiInstance.apiV1DriveSyncFileIdContentPut(id, body, ifMatch, idempotencyKey)
} catch (e: ClientException) {
    println("4xx response calling DriveSyncApi#apiV1DriveSyncFileIdContentPut")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DriveSyncApi#apiV1DriveSyncFileIdContentPut")
    e.printStackTrace()
}
```

### Parameters
| **id** | **java.util.UUID**|  | |
| **body** | **java.io.File**|  | |
| **ifMatch** | **kotlin.String**| Expected etag; mismatch returns 412 (conflict). | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotencyKey** | **kotlin.String**| Stable key so a replayed mutation is not applied twice. | [optional] |

### Return type

null (empty response body)

### Authorization


Configure bearer statically:
```kotlin
ApiClient.accessToken = ""
```
Configure bearer dynamically:
```kotlin
apiInstance.accessTokenProvider = { "" }
```

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

