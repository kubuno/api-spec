# DriveSyncAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1DriveSyncDeltaGet**](DriveSyncAPI.md#apiv1drivesyncdeltaget) | **GET** /api/v1/drive/sync/delta | Changes since a cursor (delta sync).
[**apiV1DriveSyncFileIdContentPut**](DriveSyncAPI.md#apiv1drivesyncfileidcontentput) | **PUT** /api/v1/drive/sync/file/{id}/content | Replace a file&#39;s content (conflict-safe).


# **apiV1DriveSyncDeltaGet**
```swift
    open class func apiV1DriveSyncDeltaGet(cursor: Int64? = nil, limit: Int? = nil, completion: @escaping (_ data: DriveDelta?, _ error: Error?) -> Void)
```

Changes since a cursor (delta sync).

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let cursor = 987 // Int64 | Last change_seq seen (0 = full snapshot). (optional) (default to 0)
let limit = 987 // Int |  (optional) (default to 500)

// Changes since a cursor (delta sync).
DriveSyncAPI.apiV1DriveSyncDeltaGet(cursor: cursor, limit: limit) { (response, error) in
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
 **cursor** | **Int64** | Last change_seq seen (0 &#x3D; full snapshot). | [optional] [default to 0]
 **limit** | **Int** |  | [optional] [default to 500]

### Return type

[**DriveDelta**](DriveDelta.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiV1DriveSyncFileIdContentPut**
```swift
    open class func apiV1DriveSyncFileIdContentPut(id: UUID, body: URL, ifMatch: String? = nil, idempotencyKey: String? = nil, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Replace a file's content (conflict-safe).

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let id = 987 // UUID | 
let body = URL(string: "https://example.com")! // URL | 
let ifMatch = "ifMatch_example" // String | Expected etag; mismatch returns 412 (conflict). (optional)
let idempotencyKey = "idempotencyKey_example" // String | Stable key so a replayed mutation is not applied twice. (optional)

// Replace a file's content (conflict-safe).
DriveSyncAPI.apiV1DriveSyncFileIdContentPut(id: id, body: body, ifMatch: ifMatch, idempotencyKey: idempotencyKey) { (response, error) in
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
 **body** | **URL** |  | 
 **ifMatch** | **String** | Expected etag; mismatch returns 412 (conflict). | [optional] 
 **idempotencyKey** | **String** | Stable key so a replayed mutation is not applied twice. | [optional] 

### Return type

Void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

