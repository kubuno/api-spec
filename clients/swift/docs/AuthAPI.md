# AuthAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthAPI.md#login) | **POST** /api/v1/auth/login | 
[**logout**](AuthAPI.md#logout) | **POST** /api/v1/auth/logout | 
[**refresh**](AuthAPI.md#refresh) | **POST** /api/v1/auth/refresh | 
[**register**](AuthAPI.md#register) | **POST** /api/v1/auth/register | 
[**totpVerify**](AuthAPI.md#totpverify) | **POST** /api/v1/auth/totp | 


# **login**
```swift
    open class func login(loginDto: LoginDto, completion: @escaping (_ data: NativeTokenResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let loginDto = LoginDto(clientType: "clientType_example", deviceName: "deviceName_example", deviceType: "deviceType_example", login: "login_example", password: "password_example") // LoginDto | 

AuthAPI.login(loginDto: loginDto) { (response, error) in
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
 **loginDto** | [**LoginDto**](LoginDto.md) |  | 

### Return type

[**NativeTokenResponse**](NativeTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
```swift
    open class func logout(refreshRequest: RefreshRequest, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let refreshRequest = RefreshRequest(refreshToken: "refreshToken_example") // RefreshRequest | Optionnel — clients natifs. Le web envoie le refresh via cookie.

AuthAPI.logout(refreshRequest: refreshRequest) { (response, error) in
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
 **refreshRequest** | [**RefreshRequest**](RefreshRequest.md) | Optionnel — clients natifs. Le web envoie le refresh via cookie. | 

### Return type

Void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh**
```swift
    open class func refresh(refreshRequest: RefreshRequest, completion: @escaping (_ data: NativeTokenResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let refreshRequest = RefreshRequest(refreshToken: "refreshToken_example") // RefreshRequest | Optionnel — clients natifs. Le web envoie le refresh via cookie.

AuthAPI.refresh(refreshRequest: refreshRequest) { (response, error) in
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
 **refreshRequest** | [**RefreshRequest**](RefreshRequest.md) | Optionnel — clients natifs. Le web envoie le refresh via cookie. | 

### Return type

[**NativeTokenResponse**](NativeTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
```swift
    open class func register(createUserDto: CreateUserDto, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let createUserDto = CreateUserDto(displayName: "displayName_example", email: "email_example", password: "password_example", username: "username_example") // CreateUserDto | 

AuthAPI.register(createUserDto: createUserDto) { (response, error) in
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
 **createUserDto** | [**CreateUserDto**](CreateUserDto.md) |  | 

### Return type

Void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **totpVerify**
```swift
    open class func totpVerify(totpVerifyDto: TotpVerifyDto, completion: @escaping (_ data: NativeTokenResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import KubunoAPI

let totpVerifyDto = TotpVerifyDto(clientType: "clientType_example", code: "code_example", totpSession: "totpSession_example") // TotpVerifyDto | 

AuthAPI.totpVerify(totpVerifyDto: totpVerifyDto) { (response, error) in
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
 **totpVerifyDto** | [**TotpVerifyDto**](TotpVerifyDto.md) |  | 

### Return type

[**NativeTokenResponse**](NativeTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

