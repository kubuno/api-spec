
# RefreshToken

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **createdAt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  |
| **expiresAt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  |
| **id** | [**java.util.UUID**](java.util.UUID.md) |  |  |
| **lastUsedAt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  |
| **userId** | [**java.util.UUID**](java.util.UUID.md) |  |  |
| **clientType** | **kotlin.String** | How the session was opened: &#39;web&#39; | &#39;native&#39; | &#39;desktop&#39; | &#39;api&#39;. |  [optional] |
| **deviceName** | **kotlin.String** |  |  [optional] |
| **deviceType** | **kotlin.String** |  |  [optional] |
| **familyId** | [**java.util.UUID**](java.util.UUID.md) | Root of the rotation chain (all refresh tokens issued from one device login). |  [optional] |
| **ipAddress** | **kotlin.String** |  |  [optional] |
| **revokeReason** | **kotlin.String** |  |  [optional] |
| **revokedAt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] |
| **userAgent** | **kotlin.String** |  |  [optional] |



