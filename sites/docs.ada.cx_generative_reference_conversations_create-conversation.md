---
url: "https://docs.ada.cx/generative/reference/conversations/create-conversation"
title: "Create a new conversation | Ada | Documentation"
---

Create a new conversation. If `end_user_id` is not provided, the system creates a new end user automatically. The maximum request size is 10MB, and metadata must not exceed 4KB.

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Request

This endpoint expects an object.

channel\_idstringRequired

The ID of the channel to create a conversation in

end\_user\_idstringOptional

The ID of the end user participating in the conversation. If not provided, the system will create a new end user automatically.

metadatamap from strings to anyOptional

A dictionary of key, value pairs assigned to the conversation - `metadata` keys may only be of type: `string` \- `metadata` values may only be one of type: `string`, `boolean`, or `integer`

### Response

Conversation created

idstringOptional

The ID of the conversation

channel\_idstringOptional

The ID of the channel

end\_user\_idstringOptional

The ID of the end user participating in the conversation

statusenumOptional

The status of the conversation

Allowed values:activeended

created\_atstringOptional

The date and time the conversation was created

updated\_atstringOptional

The date and time the conversation was last updated

metadatamap from strings to anyOptional

A dictionary of key, value pairs assigned to the conversation - `metadata` keys may only be of type: `string` \- `metadata` values may only be one of type: `string`, `boolean`, or `integer`

### Errors

400

Bad Request Error

401

Unauthorized Error

404

Not Found Error

429

Too Many Requests Error

500

Internal Server Error