---
url: "https://docs.ada.cx/generative/reference/knowledge/articles/bulk-upsert"
title: "Upsert multiple articles | Ada | Documentation"
---

Upsert an array of knowledge articles

This endpoint will create or update articles based on the unique `id` field of each article. If an article with the same `id` already exists, it will be updated. Otherwise, a new article will be created.

**Limits:**

- The maximum size of a request payload is 10MB
- The maximum size of an article is 100KB
- The maximum number of articles is 50,000

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Request

This endpoint expects a list of objects.

idstringRequired `>=1 character` `<=160 characters`

A unique identifier for the article

namestringRequired `>=1 character` `<=255 characters`

The name or title of the article

contentstringRequired `>=1 character`

The content of the article in markdown format

knowledge\_source\_idstringRequired

The id of the `knowledge_source` the article belongs to

urlstringOptional `format: "url"`

The url of the article

tag\_idslist of stringsOptional

A list of ids for the tags associated with the article

languagestringOptional

The IETF BCP 47 language code for the article, defaults to `en`

external\_createdstringOptional `format: "date-time"`

The date the article was created in the source system

external\_updatedstringOptional `format: "date-time"`

The date the article was last updated in the source system

enabledbooleanOptional

Whether the article should be referenced during response generation, defaults to `true`

metadataobjectOptional

A dictionary of arbitrary key,value pairs. This data is not used by Ada, but can be used by the client to store additional information about the article.

### Response

Articles upserted

idstring `>=1 character` `<=160 characters`

A unique identifier for the article

successbooleanOptional

Whether the article was successfully created/updated

createdbooleanOptional

`True` if a new article was created, `false` if an existing article was updated

### Errors

400

Bad Request Error

401

Unauthorized Error

429

Too Many Requests Error

500

Internal Server Error