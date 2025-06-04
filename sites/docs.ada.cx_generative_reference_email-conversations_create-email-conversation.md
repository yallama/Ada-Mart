---
url: "https://docs.ada.cx/generative/reference/email-conversations/create-email-conversation"
title: "Start a conversation over Ada's email channel | Ada | Documentation"
---

Start a conversation with a customer over Ada’s email channel, providing context for their inquiry. Your AI agent can only start conversations using the default Ada provided email, or email addresses you’ve set up in your bring your own domain settings.

### Headers

AuthorizationstringRequired

Bearer authentication of the form Bearer <token>, where token is your auth token.

### Request

This endpoint expects an object.

namestringRequired

The customer’s full name

subjectstringRequired

The subject of the customer’s inquiry; used as the subject for the AI Agent’s reply

reply\_tostringRequired

The customer’s email address

textstringOptional

The customer’s inquiry, limited to 10 KB

reply\_asstringOptional

The company email address you want to use to reply to the customer. Defaults to the Ada provided email address.

metadataobjectOptional

Any metadata associated with the conversation, up to 4 KB. All metadata passed through this field will appear as metavariables in your dashboard.

### Response

Conversation Created

conversation\_idstringOptional

The Ada-generated conversation id

### Errors

400

Bad Request Error

401

Unauthorized Error

422

Unprocessable Entity Error

429

Too Many Requests Error

500

Internal Server Error