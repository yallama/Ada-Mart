---
url: "https://docs.ada.cx/generative/reference/conversations/get-conversation-by-id"
title: "Get a conversation | Ada | Documentation"
---

Get a conversation by its ID

### Path parameters

conversation\_idstringRequired `format: "id"`

The ID of the conversation to retrieve

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Response

Conversation retrieved

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