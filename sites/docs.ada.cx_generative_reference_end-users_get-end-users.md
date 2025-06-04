---
url: "https://docs.ada.cx/generative/reference/end-users/get-end-users"
title: "Get multiple end users | Ada | Documentation"
---

Get multiple end users. You can specify how many users appear per page, and which user id to start from.

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Query parameters

cursorstringOptional `format: "id"`

The id that marks the start or beginning of the returned records

limitintegerOptional `>=1` `<=100`

The number of records to return

### Response

OK

datalist of objectsOptional

The list of end user profiles

Show 4 properties

metaobjectOptional

Metadata returned with the results including but not limited to a link to the next page of data

Show 1 properties

### Errors

400

Bad Request Error

401

Unauthorized Error

429

Too Many Requests Error

500

Internal Server Error