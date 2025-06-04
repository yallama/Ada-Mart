---
url: "https://docs.ada.cx/generative/reference/conversations/conversation-ended-webhook"
title: "Webhook: Conversation ended | Ada | Documentation"
---

A webhook sent when a conversation ends

### Payload

The payload of this webhook request is an object.

typestringOptional

The webhook event type

timestampstringOptional

The timestamp for when the event was generated, uses millisecond precision to help with event ordering

dataobjectOptional

The webhook event data

Show 6 properties

### Response

200

any

Return a 200 status to indicate that the data was received successfully.