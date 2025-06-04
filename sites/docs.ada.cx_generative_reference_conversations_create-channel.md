---
url: "https://docs.ada.cx/generative/reference/conversations/create-channel"
title: "Create a new channel | Ada | Documentation"
---

Create a new channel. A maximum of 100 channels can be created per account per day. The maximum request size is 10MB.

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Request

This endpoint expects an object.

namestringRequired

The name of the channel

descriptionstringRequired

A description of the channel

modalityenumRequired

The modality of the channel

Allowed values:messagingemail

metadatamap from strings to strings or booleans or doublesOptional

A dictionary of key, value pairs assigned to the channel. Metadata may not exceed 4KB total

- `metadata` keys may only be of type: `string`
- `metadata` values may only be one of type: `string`, `boolean`, or `number`

Show 3 variants

### Response

Channel created

namestring

The name of the channel

descriptionstring

A description of the channel

modalityenum

The modality of the channel

Allowed values:messagingemail

idstringOptional `format: "id"`

The channel ID

metadatamap from strings to strings or booleans or doublesOptional

A dictionary of key, value pairs assigned to the channel. Metadata may not exceed 4KB total

- `metadata` keys may only be of type: `string`
- `metadata` values may only be one of type: `string`, `boolean`, or `number`

Show 3 variants

created\_atstringOptional `format: "date-time"`

The date and time the channel was created

### Errors

400

Bad Request Error

401

Unauthorized Error

413

Content Too Large Error

429

Too Many Requests Error

500

Internal Server Error