---
url: "https://docs.ada.cx/generative/reference/conversations/end-conversation"
title: "End a conversation | Ada | Documentation"
---

Ends the conversation specified by the `conversation_id`

### Path parameters

conversation\_idstringRequired `format: "id"`

The ID of the conversation to end

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Response

Conversation ended successfully

messagestringOptional

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