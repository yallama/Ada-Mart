---
url: "https://docs.ada.cx/generative/reference/introduction/versioning"
title: "Versioning | Ada | Documentation"
---

Ada’s API follows a strict versioning policy designed to avoid disruption by enabling controlled adoption of breaking changes.
Versioning applies to both API calls and webhooks.
New versions are introduced when changes are not [backwards-compatible](https://docs.ada.cx/generative/reference/introduction/versioning#backwards-compatible-changes).

## Major Versions

Ada’s API uses path-based versioning to indicate major updates, shown in URLs like:

```code-block text-sm

https://example.ada.support/api/v2/end-users/
```

## Webhook Versioning

Webhooks follow a similar versioning scheme within their payloads. For example:

```code-block text-sm

1{2  "type": "v1.end_user.created",3  "timestamp": "2024-01-17T22:23:35.835",4  "data": {5    "end_user_id": "5f7e0e2c1e7c7e000f0f9c3a",6    "profile": {7      "email": "ada.lovelace@ada.cx",8    },9    "created_at": "2023-12-08T19:06:04.890000",10    "updated_at": "2023-12-08T19:06:04.890000"11  }12}
```

## Backwards compatible changes

The following types of changes are considered backwards-compatible and do not require a new major version.
When integrating with Ada’s APIs and webhook payloads, ensure that code handles these changes gracefully to avoid disruptions.
For example, parsing logic should ignore unexpected keys and accommodate new enum values without errors

- New authentication options
- Additional endpoints or HTTP headers
- Optional request fields or query parameters
- New properties in responses or webhook payloads
- Expanded enum values or webhook triggers
- Field order adjustments in responses
- Relaxed input validation rules
- More specific error status codes (e.g., 500 to 401)
- Modified string formats or lengths (e.g., IDs, messages)