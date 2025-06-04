---
url: "https://docs.ada.cx/generative/reference/knowledge/tags/upsert-multiple"
title: "Upsert multiple tags | Ada | Documentation"
---

Upsert an array of tags for articles

This endpoint will create or update tags based on the unique `id` field of each tag. If a tag with the same `id` already exists, it will be updated. Otherwise, a new tag will be created.

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Request

This endpoint expects a list of objects.

idstringRequired `>=1 character` `<=40 characters`

A unique identifier for the tag

namestringRequired `>=1 character` `<=40 characters`

The name of the tag

### Response

Tags upserted

successboolean

Whether the article tag was successfully created/updated

createdboolean

`True` if a new article tag was created, `false` if an existing article tag was updated

idstring

The id of the article tag

### Errors

400

Bad Request Error

401

Unauthorized Error

429

Too Many Requests Error

500

Internal Server Error