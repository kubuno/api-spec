
# LoginDto

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **login** | **kotlin.String** | Email ou nom d&#39;utilisateur. |  |
| **password** | **kotlin.String** |  |  |
| **clientType** | **kotlin.String** | &#39;web&#39; (default) keeps the HttpOnly cookie. &#39;native&#39;/&#39;desktop&#39; receive the refresh token in the JSON body (no cookie) so non-browser clients can store it in the OS keychain and refresh without a cookie jar. |  [optional] |
| **deviceName** | **kotlin.String** |  |  [optional] |
| **deviceType** | **kotlin.String** |  |  [optional] |



