---
url: "https://docs.ada.cx/generative/reference/integrations/get-platform-integration-installation-self"
title: "Get an installation | Ada | Documentation"
---

Get the platform integration installation associated with the access token. Use this endpoint to get the details of an installation, including the configuration form completed by the admin.

### Path parameters

idstringRequired `format: "id"`

The id of the platform integration to fetch installation for

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Response

Success

idstringOptional `format: "id"`

The unique identifier for the integration installation

platform\_integration\_idstringOptional `format: "id"`

The unique identifier for the integration

createdstringOptional `format: "date-time"`

The date and time the installation was created

updatedstringOptional `format: "date-time"`

The date and time the installation was last updated

configurationobjectOptional

The configuration settings for the integration

statusstringOptional

The current state of the integration installation (incomplete, complete)

### Errors

400

Bad Request Error

401

Unauthorized Error

403

Forbidden Error

404

Not Found Error

429

Too Many Requests Error

500

Internal Server Error