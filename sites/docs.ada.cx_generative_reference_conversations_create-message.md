---
url: "https://docs.ada.cx/generative/reference/conversations/create-message"
title: "Create a new message | Ada | Documentation"
---

Create a new message in a conversation. The maximum request size is 10MB.

### Path parameters

conversation\_idstringRequired `format: "id"`

The ID of the conversation

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Request

This endpoint expects an object.

authorobjectRequired

Show 4 properties

contentobjectRequired

The message content

Show 2 properties

### Response

Message created

idstringOptional

The ID of the message

conversation\_idstringOptional

The ID of the conversation

authorobjectOptional

Show 4 properties

contentobjectOptional

The message content

Show 2 properties

created\_atstringOptional `format: "date-time"`

The date and time the message was created

updated\_atstringOptional `format: "date-time"`

The date and time the message was updated

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