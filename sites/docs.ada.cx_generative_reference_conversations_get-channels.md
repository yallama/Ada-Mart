---
url: "https://docs.ada.cx/generative/reference/conversations/get-channels"
title: "Get a list of channels | Ada | Documentation"
---

Get a list of channels. This list can be filtered by modality and paginated. The default and maximum limits are 100 channels per page

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Query parameters

cursorstringOptional `format: "id"`

The ID that marks the start or beginning of the returned records

limitintegerOptional `>=1` `<=100`

The number of records to return

modalityenumOptional

The modality of the channels to retrieve

Allowed values:messagingemail

### Response

Channels

datalist of objectsOptional

Show 6 properties

metaobjectOptional

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