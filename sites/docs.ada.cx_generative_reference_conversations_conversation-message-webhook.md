---
url: "https://docs.ada.cx/generative/reference/conversations/conversation-message-webhook"
title: "Webhook: Conversation message | Ada | Documentation"
---

A webhook sent when a message is sent to a conversation

### Payload

The payload of this webhook request is an object.

typestringOptional

The webhook event type

timestampstringOptional

The timestamp for when the event was generated, uses millisecond precision to help with event ordering needs

dataobjectOptional

The webhook event data

Show 6 properties

### Response

200

any

Return a 200 status to indicate that the data was received successfully.