---
url: "https://docs.ada.cx/generative/reference/knowledge/articles/delete"
title: "Delete multiple articles | Ada | Documentation"
---

Delete multiple articles

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Query parameters

idlist of stringsOptional

Filter by article id

enabledlist of booleansOptional

Filter by enabled status

languagelist of stringsOptional

Filter by language

knowledge\_source\_idlist of stringsOptional

Filter by knowledge source

tag\_idslist of stringsOptional

Filter by tag ids

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