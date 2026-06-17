# PushApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**apiV1MePushDevicesIdDelete**](PushApi.md#apiV1MePushDevicesIdDelete) | **DELETE** /api/v1/me/push/devices/{id} | Unregister a push device. |
| [**apiV1MePushDevicesPost**](PushApi.md#apiV1MePushDevicesPost) | **POST** /api/v1/me/push/devices | Register (or refresh) a push device. |
| [**apiV1MePushPreferencesGet**](PushApi.md#apiV1MePushPreferencesGet) | **GET** /api/v1/me/push/preferences | List push opt-out preferences. |
| [**apiV1MePushPreferencesPatch**](PushApi.md#apiV1MePushPreferencesPatch) | **PATCH** /api/v1/me/push/preferences | Upsert one push preference. |


<a id="apiV1MePushDevicesIdDelete"></a>
# **apiV1MePushDevicesIdDelete**
> apiV1MePushDevicesIdDelete(id)

Unregister a push device.

### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = PushApi()
val id : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
try {
    apiInstance.apiV1MePushDevicesIdDelete(id)
} catch (e: ClientException) {
    println("4xx response calling PushApi#apiV1MePushDevicesIdDelete")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PushApi#apiV1MePushDevicesIdDelete")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **java.util.UUID**|  | |

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

<a id="apiV1MePushDevicesPost"></a>
# **apiV1MePushDevicesPost**
> apiV1MePushDevicesPost(registerDeviceDto)

Register (or refresh) a push device.

### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = PushApi()
val registerDeviceDto : RegisterDeviceDto =  // RegisterDeviceDto | 
try {
    apiInstance.apiV1MePushDevicesPost(registerDeviceDto)
} catch (e: ClientException) {
    println("4xx response calling PushApi#apiV1MePushDevicesPost")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PushApi#apiV1MePushDevicesPost")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registerDeviceDto** | [**RegisterDeviceDto**](RegisterDeviceDto.md)|  | |

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

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a id="apiV1MePushPreferencesGet"></a>
# **apiV1MePushPreferencesGet**
> apiV1MePushPreferencesGet()

List push opt-out preferences.

### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = PushApi()
try {
    apiInstance.apiV1MePushPreferencesGet()
} catch (e: ClientException) {
    println("4xx response calling PushApi#apiV1MePushPreferencesGet")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PushApi#apiV1MePushPreferencesGet")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="apiV1MePushPreferencesPatch"></a>
# **apiV1MePushPreferencesPatch**
> apiV1MePushPreferencesPatch(setPreferenceDto)

Upsert one push preference.

### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = PushApi()
val setPreferenceDto : SetPreferenceDto =  // SetPreferenceDto | 
try {
    apiInstance.apiV1MePushPreferencesPatch(setPreferenceDto)
} catch (e: ClientException) {
    println("4xx response calling PushApi#apiV1MePushPreferencesPatch")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling PushApi#apiV1MePushPreferencesPatch")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **setPreferenceDto** | [**SetPreferenceDto**](SetPreferenceDto.md)|  | |

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

 - **Content-Type**: application/json
 - **Accept**: Not defined

