---
url: "https://docs.ada.cx/generative/reference/integrations/update-single-platform-integration"
title: "Update an integration | Ada | Documentation"
---

Update a platform integration. **_Note:_ only integrations in development may be updated. Integrations submitted for publication cannot be updated.**

### Path parameters

idstringRequired `format: "id"`

The id of the platform integration to update

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Request

This endpoint expects an object.

authorstringOptional `>=1 character` `<=160 characters`

The name of the integration developer

call\_to\_actionstringOptional `>=1 character`

The call to action text

configuration\_fieldsobjectOptional

A json-schema describing the settings fields that a user should be presented with when installing the integration

contactstringOptional `>=1 character`

The URL or email address where users of the integration can reach out for support

descriptionstringOptional `>=1 character`

A description of what the integration does and how to use it

error\_codesobjectOptional

An object containing error codes and their corresponding error message the integration may return to the OAuth failure page to be displayed

identifier\_field\_pathstringOptional

JMESPath describing which of the fields in `configuration_fields` is the best human-friendly field to use to identify a specific installation (e.g., account name)

namestringOptional `>=1 character` `<=160 characters`

The name of the integration

oauth\_callback\_urlstringOptional `format: "url"` `>=1 character`

The `get` endpoint that will be invoked after OAuth authorization

scopeslist of stringsOptional

The list of OAuth token permissions the integration requests when installed

tagslist of enumsOptional

A list of tags that describe the type of integration

Allowed values:knowledge

uninstallation\_urlstringOptional `format: "url"` `>=1 character`

The `delete` endpoint that initiates the uninstallation flow for the integration

### Response

Platform integration updated

idstring

The unique identifier for the integration

identifier\_field\_pathstring

JMESPath describing which of the fields in `configuration_fields` is the best human-friendly field to use to identify a specific installation (e.g., account name)

statusstring

The current state of the integration (development, approved, archived)

authorstringOptional `>=1 character` `<=160 characters`

The name of the integration developer

call\_to\_actionstringOptional `>=1 character`

The call to action text

configuration\_fieldsobjectOptional

A json-schema describing the settings fields that a user should be presented with when installing the integration

contactstringOptional `>=1 character`

The URL or email address where users of the integration can reach out for support

createdstringOptional `format: "date-time"`

The date the integration was created

descriptionstringOptional `>=1 character`

A description of what the integration does and how to use it

error\_codesobjectOptional

An object containing error codes and their corresponding error message the integration may return to the OAuth failure page to be displayed

namestringOptional `>=1 character` `<=160 characters`

The name of the integration

oauth\_callback\_urlstringOptional `format: "url"` `>=1 character`

The `get` endpoint that will be invoked after OAuth authorization

scopeslist of stringsOptional

The list of OAuth token permissions the integration requests when installed

tagslist of enumsOptional

A list of tags that describe the type of integration

Allowed values:knowledge

uninstallation\_urlstringOptional `format: "url"` `>=1 character`

The `delete` endpoint that initiates the uninstallation flow for the integration

updatedstringOptional `format: "date-time"`

The date the integration was last updated

### Errors

400

Bad Request Error

401

Unauthorized Error

403

Forbidden Error

429

Too Many Requests Error

500

Internal Server Error