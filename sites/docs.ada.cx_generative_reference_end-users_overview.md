---
url: "https://docs.ada.cx/generative/reference/end-users/overview"
title: "Overview | Ada | Documentation"
---

The End Users API allows you to update and manage your users’ data in real time. It also comes with webhook events you can subscribe to so you can keep track of changes to user profiles in Ada.

This API allows integrators to:

- Programmatically sync user details from external systems with Ada using webhooks so that Action and Knowledge rules apply to those users.
- Get notified at your [webhook endpoint](https://docs.ada.cx/generative/reference/end-users/overview#webhook-support) when Ada users are created or updated through the API.
- Update metavariables using request blocks or Actions.
  - The `end_user_id` is a variable that will fill in this part of the URL programmatically for requests or actions (so you don’t have to consume webhooks unless needed).

## User Profile Structure

The End User Profile entity is represented as a JSON object composed of `key,value` pairs. Each key in the End User object represents a metavariable you can use throughout Ada. [Learn more about metavariables](https://docs.ada.cx/docs/scripted/build-and-maintain-your-bot/personalize-conversations/get-started-with-variables/#UUID-47544806-121d-a9b6-bc67-8761f3b53924_id_360026518374_id_h_a4b9bdb4-9a05-4772-8f4d-55b8399274c0).

You can use the `profile.metadata` object to create a custom mapping of key, value pairs to reflect your company’s
data schema. All values must be strings, integers, or booleans.

The `system_properties` object includes select keys automatically created by Ada, and is read-only. Note that depending on your Ada configuration, not all keys defined in the End Users API specification may be present or may have values.

The end user profile is composed of metavariables, which may be set through Ada’s embed SDK as well as through the End Users API. Use caution when storing user information in metavariables - they are not intended to replace an authentication flow to verify a user’s identity and information.

## Webhook Support

Ada supports event notifications that enable you to track specific user actions and updates. The following events are currently supported:

- [`v1.end_user.created`](https://docs.ada.cx/generative/reference/end-users/end-user-created-webhook): Triggered when a new user is created through any of Ada’s supported channels. The bot’s customer persistence setting influences the rate of these events.
- [`v1.end_user.updated`](https://docs.ada.cx/generative/reference/end-users/end-user-updated-webhook): Triggered when a value on the end user’s profile changes. Updates may occur via:

  - API calls (e.g., PATCH requests to the End Users API).
  - Updates through Ada-supported channels (e.g., setMetafields on embeds).
  - Profile field mappings from Sunshine Conversations.

### Changes That Do Not Trigger Events

Certain updates do not generate `end_user.updated` events:

- Changes to system.properties.
- Modifications to metavariables like:
  - ip\_address
  - user\_agent
  - browser
  - device
  - last\_answer\_id
  - channel\_status

For more details on how to implement and use webhooks, refer to the [webhook documentation](https://docs.ada.cx/generative/reference/introduction/webhooks).