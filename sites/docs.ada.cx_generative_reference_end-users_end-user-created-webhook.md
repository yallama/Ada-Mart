---
url: "https://docs.ada.cx/generative/reference/end-users/end-user-created-webhook"
title: "Webhook: End user created | Ada | Documentation"
---

A webhook sent when a new end user is created

### Payload

The payload of this webhook request is an object.

typestringOptional

The webhook event type description

timestampstringOptional

The timestamp for when the event was generated. Uses millisecond precision to help with event ordering needs.

dataobjectOptional

The webhook event data

Show 4 properties

tagslist of stringsOptional

A list of tags that Ada provides. You can use tags to filter webhook events in the Ada dashboard. Includes the `end_user_id` value for the webhook payload by default. Ada may add additional tags at any time.

### Response

200

any

Return a 200 status to indicate that the data was received successfully.