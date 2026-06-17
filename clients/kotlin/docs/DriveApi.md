# DriveApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**apiV1DriveFoldersPost**](DriveApi.md#apiV1DriveFoldersPost) | **POST** /api/v1/drive/folders | Create a folder. |
| [**apiV1DriveIdDownloadGet**](DriveApi.md#apiV1DriveIdDownloadGet) | **GET** /api/v1/drive/{id}/download | Download a file&#39;s content. |
| [**apiV1DriveIdTrashPost**](DriveApi.md#apiV1DriveIdTrashPost) | **POST** /api/v1/drive/{id}/trash | Move a file to trash. |
| [**apiV1DriveUploadPost**](DriveApi.md#apiV1DriveUploadPost) | **POST** /api/v1/drive/upload | Upload a new file (multipart). |


<a id="apiV1DriveFoldersPost"></a>
# **apiV1DriveFoldersPost**
> ApiV1DriveFoldersPost200Response apiV1DriveFoldersPost(createFolderDto, idempotencyKey)

Create a folder.

### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = DriveApi()
val createFolderDto : CreateFolderDto =  // CreateFolderDto | 
val idempotencyKey : kotlin.String = idempotencyKey_example // kotlin.String | Stable key so a replayed mutation is not applied twice.
try {
    val result : ApiV1DriveFoldersPost200Response = apiInstance.apiV1DriveFoldersPost(createFolderDto, idempotencyKey)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DriveApi#apiV1DriveFoldersPost")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DriveApi#apiV1DriveFoldersPost")
    e.printStackTrace()
}
```

### Parameters
| **createFolderDto** | [**CreateFolderDto**](CreateFolderDto.md)|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotencyKey** | **kotlin.String**| Stable key so a replayed mutation is not applied twice. | [optional] |

### Return type

[**ApiV1DriveFoldersPost200Response**](ApiV1DriveFoldersPost200Response.md)

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

 - **Content-Type**: application/json
 - **Accept**: application/json

<a id="apiV1DriveIdDownloadGet"></a>
# **apiV1DriveIdDownloadGet**
> java.io.File apiV1DriveIdDownloadGet(id)

Download a file&#39;s content.

### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = DriveApi()
val id : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
try {
    val result : java.io.File = apiInstance.apiV1DriveIdDownloadGet(id)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DriveApi#apiV1DriveIdDownloadGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DriveApi#apiV1DriveIdDownloadGet")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **java.util.UUID**|  | |

### Return type

[**java.io.File**](java.io.File.md)

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
 - **Accept**: application/octet-stream

<a id="apiV1DriveIdTrashPost"></a>
# **apiV1DriveIdTrashPost**
> apiV1DriveIdTrashPost(id, idempotencyKey)

Move a file to trash.

### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = DriveApi()
val id : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val idempotencyKey : kotlin.String = idempotencyKey_example // kotlin.String | Stable key so a replayed mutation is not applied twice.
try {
    apiInstance.apiV1DriveIdTrashPost(id, idempotencyKey)
} catch (e: ClientException) {
    println("4xx response calling DriveApi#apiV1DriveIdTrashPost")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DriveApi#apiV1DriveIdTrashPost")
    e.printStackTrace()
}
```

### Parameters
| **id** | **java.util.UUID**|  | |
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a id="apiV1DriveUploadPost"></a>
# **apiV1DriveUploadPost**
> apiV1DriveUploadPost(file, idempotencyKey, folderId)

Upload a new file (multipart).

### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = DriveApi()
val file : java.io.File = BINARY_DATA_HERE // java.io.File | 
val idempotencyKey : kotlin.String = idempotencyKey_example // kotlin.String | Stable key so a replayed mutation is not applied twice.
val folderId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
try {
    apiInstance.apiV1DriveUploadPost(file, idempotencyKey, folderId)
} catch (e: ClientException) {
    println("4xx response calling DriveApi#apiV1DriveUploadPost")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DriveApi#apiV1DriveUploadPost")
    e.printStackTrace()
}
```

### Parameters
| **file** | **java.io.File**|  | |
| **idempotencyKey** | **kotlin.String**| Stable key so a replayed mutation is not applied twice. | [optional] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **folderId** | **java.util.UUID**|  | [optional] |

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

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

