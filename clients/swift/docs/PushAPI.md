# PushAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1MePushDevicesIdDelete**](PushAPI.md#apiv1mepushdevicesiddelete) | **DELETE** /api/v1/me/push/devices/{id} | Unregister a push device.
[**apiV1MePushDevicesPost**](PushAPI.md#apiv1mepushdevicespost) | **POST** /api/v1/me/push/devices | Register (or refresh) a push device.
[**apiV1MePushPreferencesGet**](PushAPI.md#apiv1mepushpreferencesget) | **GET** /api/v1/me/push/preferences | List push opt-out preferences.
[**apiV1MePushPreferencesPatch**](PushAPI.md#apiv1mepushpreferencespatch) | **PATCH** /api/v1/me/push/preferences | Upsert one push preference.


# **apiV1MePushDevicesIdDelete**
```swift
    open class func apiV1MePushDevicesIdDelete(id: UUID, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Unregister a push device.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let id = 987 // UUID | 

// Unregister a push device.
PushAPI.apiV1MePushDevicesIdDelete(id: id) { (response, error) in
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

Void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiV1MePushDevicesPost**
```swift
    open class func apiV1MePushDevicesPost(registerDeviceDto: RegisterDeviceDto, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Register (or refresh) a push device.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let registerDeviceDto = RegisterDeviceDto(provider: "provider_example", deviceToken: "deviceToken_example", appId: "appId_example", locale: "locale_example") // RegisterDeviceDto | 

// Register (or refresh) a push device.
PushAPI.apiV1MePushDevicesPost(registerDeviceDto: registerDeviceDto) { (response, error) in
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
 **registerDeviceDto** | [**RegisterDeviceDto**](RegisterDeviceDto.md) |  | 

### Return type

Void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiV1MePushPreferencesGet**
```swift
    open class func apiV1MePushPreferencesGet(completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

List push opt-out preferences.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI


// List push opt-out preferences.
PushAPI.apiV1MePushPreferencesGet() { (response, error) in
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
This endpoint does not need any parameter.

### Return type

Void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiV1MePushPreferencesPatch**
```swift
    open class func apiV1MePushPreferencesPatch(setPreferenceDto: SetPreferenceDto, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Upsert one push preference.

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let setPreferenceDto = SetPreferenceDto(moduleId: "moduleId_example", eventType: "eventType_example", enabled: false) // SetPreferenceDto | 

// Upsert one push preference.
PushAPI.apiV1MePushPreferencesPatch(setPreferenceDto: setPreferenceDto) { (response, error) in
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
 **setPreferenceDto** | [**SetPreferenceDto**](SetPreferenceDto.md) |  | 

### Return type

Void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

