# MeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getMe**](MeApi.md#getMe) | **GET** /api/v1/me |  |
| [**listSessions**](MeApi.md#listSessions) | **GET** /api/v1/me/sessions |  |


<a id="getMe"></a>
# **getMe**
> User getMe()



### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = MeApi()
try {
    val result : User = apiInstance.getMe()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MeApi#getMe")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MeApi#getMe")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

<a id="listSessions"></a>
# **listSessions**
> kotlin.collections.List&lt;RefreshToken&gt; listSessions()



### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = MeApi()
try {
    val result : kotlin.collections.List<RefreshToken> = apiInstance.listSessions()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling MeApi#listSessions")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling MeApi#listSessions")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;RefreshToken&gt;**](RefreshToken.md)

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

