---
url: "https://docs.ada.cx/generative/reference/knowledge/articles/get"
title: "Get a single knowledge article | Ada | Documentation"
---

Get knowledge article by id

### Path parameters

idstringRequired

The id of the article to retrieve

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Response

Knowledge article

idstring `>=1 character` `<=160 characters`

A unique identifier for the article

namestring `>=1 character` `<=255 characters`

The name or title of the article

contentstring `>=1 character`

The content of the article in markdown format

urlstringOptional `format: "url"`

The url of the article

knowledge\_source\_idstringOptional

The id of the `knowledge_source` the article belongs to

languageenumOptional

The ISO 639-1 language code of the article, defaults to `en`

Show 50 enum values

tag\_idslist of stringsOptional

A list of ids for the tags associated with the article

createdstringOptional `format: "date-time"`

The date the article was created in Ada

updatedstringOptional `format: "date-time"`

The date the article was last updated in Ada

external\_createdstringOptional `format: "date-time"`

The date the article was created in the source system

external\_updatedstringOptional `format: "date-time"`

The date the article was last updated in the source system

enabledbooleanOptional

Whether the article should be referenced during response generation, defaults to `true`

metadataobjectOptional

A dictionary of arbitrary key,value pairs. This data is not used by Ada, but can be used by the client to store additional information about the article.

### Errors

401

Unauthorized Error

404

Not Found Error

429

Too Many Requests Error

500

Internal Server Error