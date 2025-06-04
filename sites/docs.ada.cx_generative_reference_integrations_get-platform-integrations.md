---
url: "https://docs.ada.cx/generative/reference/integrations/get-platform-integrations"
title: "List integrations | Ada | Documentation"
---

Get a list of platform integrations owned by your Ada account (e.g. a developer sandbox)

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Query parameters

cursorstringOptional `format: "id"`

The id that marks the start or beginning of the returned records

limitintegerOptional `>=1` `<=100`

The number of records to return

### Response

Platform integrations

datalist of objectsOptional

Show 16 properties

metaobjectOptional

Show 1 properties

### Errors

401

Unauthorized Error

404

Not Found Error

429

Too Many Requests Error

500

Internal Server Error