# AuthApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**login**](AuthApi.md#login) | **POST** /api/v1/auth/login |  |
| [**logout**](AuthApi.md#logout) | **POST** /api/v1/auth/logout |  |
| [**refresh**](AuthApi.md#refresh) | **POST** /api/v1/auth/refresh |  |
| [**register**](AuthApi.md#register) | **POST** /api/v1/auth/register |  |
| [**totpVerify**](AuthApi.md#totpVerify) | **POST** /api/v1/auth/totp |  |


<a id="login"></a>
# **login**
> NativeTokenResponse login(loginDto)



### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = AuthApi()
val loginDto : LoginDto =  // LoginDto | 
try {
    val result : NativeTokenResponse = apiInstance.login(loginDto)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AuthApi#login")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthApi#login")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **loginDto** | [**LoginDto**](LoginDto.md)|  | |

### Return type

[**NativeTokenResponse**](NativeTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a id="logout"></a>
# **logout**
> logout(refreshRequest)



### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = AuthApi()
val refreshRequest : RefreshRequest =  // RefreshRequest | Optionnel — clients natifs. Le web envoie le refresh via cookie.
try {
    apiInstance.logout(refreshRequest)
} catch (e: ClientException) {
    println("4xx response calling AuthApi#logout")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthApi#logout")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **refreshRequest** | [**RefreshRequest**](RefreshRequest.md)| Optionnel — clients natifs. Le web envoie le refresh via cookie. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a id="refresh"></a>
# **refresh**
> NativeTokenResponse refresh(refreshRequest)



### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = AuthApi()
val refreshRequest : RefreshRequest =  // RefreshRequest | Optionnel — clients natifs. Le web envoie le refresh via cookie.
try {
    val result : NativeTokenResponse = apiInstance.refresh(refreshRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AuthApi#refresh")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthApi#refresh")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **refreshRequest** | [**RefreshRequest**](RefreshRequest.md)| Optionnel — clients natifs. Le web envoie le refresh via cookie. | |

### Return type

[**NativeTokenResponse**](NativeTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a id="register"></a>
# **register**
> register(createUserDto)



### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = AuthApi()
val createUserDto : CreateUserDto =  // CreateUserDto | 
try {
    apiInstance.register(createUserDto)
} catch (e: ClientException) {
    println("4xx response calling AuthApi#register")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthApi#register")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **createUserDto** | [**CreateUserDto**](CreateUserDto.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a id="totpVerify"></a>
# **totpVerify**
> NativeTokenResponse totpVerify(totpVerifyDto)



### Example
```kotlin
// Import classes:
//import com.kubuno.api.infrastructure.*
//import com.kubuno.api.models.*

val apiInstance = AuthApi()
val totpVerifyDto : TotpVerifyDto =  // TotpVerifyDto | 
try {
    val result : NativeTokenResponse = apiInstance.totpVerify(totpVerifyDto)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AuthApi#totpVerify")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AuthApi#totpVerify")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **totpVerifyDto** | [**TotpVerifyDto**](TotpVerifyDto.md)|  | |

### Return type

[**NativeTokenResponse**](NativeTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

