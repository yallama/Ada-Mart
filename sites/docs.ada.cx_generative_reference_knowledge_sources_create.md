---
url: "https://docs.ada.cx/generative/reference/knowledge/sources/create"
title: "Create a knowledge source | Ada | Documentation"
---

Create a knowledge source

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Request

This endpoint expects an object.

idstringRequired `>=1 character` `<=160 characters`

A unique identifier for the knowledge source

namestringRequired `>=1 character`

The name of the knowledge source

metadataobjectOptional

A dictionary of arbitrary key,value pairs. This data is not used by Ada, but can be used by the client to store additional information about the knowledge source.

### Response

Knowledge source created

idstring

A unique identifier for the knowledge source

namestring `>=1 character`

The name of the knowledge source

external\_idstringOptional

An external identifier for the knowledge source

metadataobjectOptional

A dictionary of arbitrary key,value pairs. This data is not used by Ada, but can be used by the client to store additional information about the knowledge source.

createdstringOptional `format: "date-time"`

The date the knowledge source was created

updatedstringOptional `format: "date-time"`

The date the knowledge source was last updated

### Errors

400

Bad Request Error

401

Unauthorized Error

409

Conflict Error

429

Too Many Requests Error

500

Internal Server Error