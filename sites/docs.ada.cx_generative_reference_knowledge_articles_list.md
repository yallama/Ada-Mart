---
url: "https://docs.ada.cx/generative/reference/knowledge/articles/list"
title: "Get knowledge articles | Ada | Documentation"
---

Get knowledge articles

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Query parameters

cursorstringOptional `format: "id"`

The article cursor that marks the start or beginning of the returned article records

limitintegerOptional `>=1` `<=100`

The number of article records to return

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

### Response

Matching knowledge articles

datalist of objectsOptional

Show 13 properties

metaobjectOptional

Show 1 properties

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