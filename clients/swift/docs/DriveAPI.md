# DriveAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1DriveFoldersPost**](DriveAPI.md#apiv1drivefolderspost) | **POST** /api/v1/drive/folders | Create a folder.
[**apiV1DriveIdDownloadGet**](DriveAPI.md#apiv1driveiddownloadget) | **GET** /api/v1/drive/{id}/download | Download a file&#39;s content.
[**apiV1DriveIdTrashPost**](DriveAPI.md#apiv1driveidtrashpost) | **POST** /api/v1/drive/{id}/trash | Move a file to trash.
[**apiV1DriveUploadPost**](DriveAPI.md#apiv1driveuploadpost) | **POST** /api/v1/drive/upload | Upload a new file (multipart).


# **apiV1DriveFoldersPost**
```swift
    open class func apiV1DriveFoldersPost(createFolderDto: CreateFolderDto, idempotencyKey: String? = nil, completion: @escaping (_ data: ApiV1DriveFoldersPost200Response?, _ error: Error?) -> Void)
```

Create a folder.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let createFolderDto = CreateFolderDto(parentId: 123, name: "name_example") // CreateFolderDto | 
let idempotencyKey = "idempotencyKey_example" // String | Stable key so a replayed mutation is not applied twice. (optional)

// Create a folder.
DriveAPI.apiV1DriveFoldersPost(createFolderDto: createFolderDto, idempotencyKey: idempotencyKey) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createFolderDto** | [**CreateFolderDto**](CreateFolderDto.md) |  | 
 **idempotencyKey** | **String** | Stable key so a replayed mutation is not applied twice. | [optional] 

### Return type

[**ApiV1DriveFoldersPost200Response**](ApiV1DriveFoldersPost200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiV1DriveIdDownloadGet**
```swift
    open class func apiV1DriveIdDownloadGet(id: UUID, completion: @escaping (_ data: URL?, _ error: Error?) -> Void)
```

Download a file's content.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let id = 987 // UUID | 

// Download a file's content.
DriveAPI.apiV1DriveIdDownloadGet(id: id) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID** |  | 

### Return type

**URL**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiV1DriveIdTrashPost**
```swift
    open class func apiV1DriveIdTrashPost(id: UUID, idempotencyKey: String? = nil, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Move a file to trash.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let id = 987 // UUID | 
let idempotencyKey = "idempotencyKey_example" // String | Stable key so a replayed mutation is not applied twice. (optional)

// Move a file to trash.
DriveAPI.apiV1DriveIdTrashPost(id: id, idempotencyKey: idempotencyKey) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID** |  | 
 **idempotencyKey** | **String** | Stable key so a replayed mutation is not applied twice. | [optional] 

### Return type

Void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiV1DriveUploadPost**
```swift
    open class func apiV1DriveUploadPost(file: URL, idempotencyKey: String? = nil, folderId: UUID? = nil, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Upload a new file (multipart).

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let file = URL(string: "https://example.com")! // URL | 
let idempotencyKey = "idempotencyKey_example" // String | Stable key so a replayed mutation is not applied twice. (optional)
let folderId = 987 // UUID |  (optional)

// Upload a new file (multipart).
DriveAPI.apiV1DriveUploadPost(file: file, idempotencyKey: idempotencyKey, folderId: folderId) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **URL** |  | 
 **idempotencyKey** | **String** | Stable key so a replayed mutation is not applied twice. | [optional] 
 **folderId** | **UUID** |  | [optional] 

### Return type

Void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

