# ModulesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listModules**](ModulesApi.md#listModules) | **GET** /api/v1/modules |  |


<a id="listModules"></a>
# **listModules**
> listModules()



### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = ModulesApi()
try {
    apiInstance.listModules()
} catch (e: ClientException) {
    println("4xx response calling ModulesApi#listModules")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ModulesApi#listModules")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

