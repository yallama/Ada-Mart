---
url: "https://docs.ada.cx/generative/reference/integrations/update-platform-integration-installation"
title: "Update installation status | Ada | Documentation"
---

Update status after installation. An installation can be `complete` or `incomplete`.

### Path parameters

platform\_integration\_idstringRequired `format: "id"`

The id of the platform integration

installation\_idstringRequired `format: "id"`

The id of the installation to update

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Request

This endpoint expects an object.

statusenumOptional

The new status of the installation

Allowed values:completeincomplete

### Response

Installation updated

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