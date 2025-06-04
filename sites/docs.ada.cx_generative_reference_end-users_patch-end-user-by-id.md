---
url: "https://docs.ada.cx/generative/reference/end-users/patch-end-user-by-id"
title: "Update an end user | Ada | Documentation"
---

Update a specific end user by id

### Path parameters

end\_user\_idstringRequired `format: "id"`

The Ada end\_user\_id

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Request

This endpoint expects an object.

profileobjectRequired

The end user’s profile information

Show 7 properties

### Response

OK

end\_user\_idstringOptional

The unique Ada-generated id for the end user

profileobjectOptional

The end user’s profile information

Show 8 properties

created\_atstringOptional

The date and time the end user was created

updated\_atstringOptional

The date and time the end user was updated

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