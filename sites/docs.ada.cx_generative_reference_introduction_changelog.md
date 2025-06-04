---
url: "https://docs.ada.cx/generative/reference/introduction/changelog"
title: "Changelog | Ada | Documentation"
---

[May 7, 2025](https://docs.ada.cx/changelog/end-user-profile-fields)

## [New End User profile fields](https://docs.ada.cx/changelog/end-user-profile-fields)

We have added two new optional fields to the [End User profile object](https://docs.ada.cx/generative/reference/end-users/overview):

- `avatar`: A URL to the end user’s avatar image
- `display_name`: The end user’s display name

[May 6, 2025](https://docs.ada.cx/changelog/new-chat-window-events)

## [New chat window events in Embed2](https://docs.ada.cx/changelog/new-chat-window-events)

We’ve added new events to the [`subscribeEvent`](https://docs.ada.cx/reference/embed2-reference#subscribeevent) action in Embed2 to help you better track user interactions within the chat window:

| Event key | Trigger | Payload |
| --- | --- | --- |
| `ada:minimize_chat` | Triggered when a user minimizes the chat window | `{ conversation_id: string, is_engaged: boolean }` |
| `ada:close_chat` | Triggered when a user closes the chat window | `{ conversation_id: string, is_engaged: boolean }` |

If you’re using the Embed2 script, these events are immediately available. For the [NPM package](https://www.npmjs.com/package/@ada-support/embed2), update to the latest version (1.9.0) to start using them.

[April 14, 2025](https://docs.ada.cx/changelog/bcp47-support-in-article-upserts)

## [BCP 47 support in article upserts](https://docs.ada.cx/changelog/bcp47-support-in-article-upserts)

The `language` field on the article object in the upsert API now supports BCP 47 language tags (e.g., `en-CA`, `fr-FR`). The previously supported `locale` field is deprecated but still accepted for backwards compatibility if `language` is not provided.

API responses from `GET /v2/knowledge/articles` and `GET /v2/knowledge/articles/{id}` will continue to return `locale`, but it is no longer documented. In these responses, the `language` field contains the ISO 639-1 two-character language code, not the full BCP 47 tag.

This is part of a gradual migration. Eventually, `locale` will be removed from both persisted records and API responses, and `language` will consistently use BCP 47 tags across all endpoints.

[March 11, 2025](https://docs.ada.cx/changelog/new-callback-event-in-embed2)

## [New callback event in Embed2](https://docs.ada.cx/changelog/new-callback-event-in-embed2)

We’ve added a new event to the [`subscribeEvent`](https://docs.ada.cx/reference/embed2-reference#subscribeevent) action in Embed2. With this event, you can receive a callback when an end user submits a CSAT. The event returns a numeric CSAT score:

| Event key | Trigger |
| --- | --- |
| `ada:csat_submitted` | Triggered when the full screen CSAT is submitted. |

If you’re using the Embed2 script, these events are immediately available. For the [NPM package](https://www.npmjs.com/package/@ada-support/embed2), update it to the latest version (1.8.16) to start using them.

[February 26, 2025](https://docs.ada.cx/changelog/reply-to-validation-in-conversation-email-api)

## [Validation added to reply\_to field in Email Conversation API](https://docs.ada.cx/changelog/reply-to-validation-in-conversation-email-api)

Validation for the `reply_to` field in the Email Conversation API will be introduced in the coming weeks. Once implemented, requests with an invalid email address will fail with a validation error.

[November 25, 2024](https://docs.ada.cx/changelog/v2-api-release)

## [v2 API release](https://docs.ada.cx/changelog/v2-api-release)

Ada is releasing a new version (v2) of our platform APIs. For detailed instructions on how to migrate your integrations, please see our [Migration Guide](https://developers.ada.cx/reference/introduction/migrate-to-v-2).

In addition to an updated developer documentation site, we’re adding the following capabilities to our platform in this release:

**API Endpoints Consolidation**

Several legacy endpoints have been merged and restructured by resource and action. This makes integrations simpler and reduces redundancy. For example:

- v1: `https://example.ada.support/api/end-users/v1/`
- v2: `https://example.ada.support/api/v2/end-users/`

**Streamlined API Tokens**

A single API token now works across all endpoints. Previously, separate tokens were required per API. This change simplifies token management and authentication.

**Uniform Response Structures**

Responses (including error messages) are now standardized. This reduces the complexity of handling different response formats and improves overall consistency.

**Standardized Pagination**

Pagination parameters and response metadata are now consistent, enhancing the developer experience when handling large data sets.

**Improved Rate & Data Limits**

More transparent rate and data limit policies have been introduced. This ensures better reliability, prevents unexpected throttling, and makes it easier to plan request volumes.

**Data Export API Updates**

The Data Export API endpoints have been updated to follow the new v2 naming convention:

- `/api/data_api/v1.4/conversations` → `/api/v2/export/conversations`
- `/api/data_api/v1.4/messages` → `/api/v2/export/messages`

**Backward-Incompatible Changes**

Some v1 functionality has been deprecated or altered. Review your current integrations and ensure you’re using the appropriate v2 endpoints and parameters.

[November 14, 2024](https://docs.ada.cx/changelog/embed2-security-improvements-1)

## [Embed2 security improvements](https://docs.ada.cx/changelog/embed2-security-improvements-1)

We’ve released some security improvements to Embed2.

- If you’re using the Embed2 [NPM package](https://www.npmjs.com/package/@ada-support/embed2) , upgrade it to version **1.7.27 or newer**.
- The Embed2 script is versionless and gets automatic updates, so if you’re using it, you can already access the upgrades.

[October 9, 2024](https://docs.ada.cx/changelog/setsensitivemetafields-embed2-action-now-supported-in-generative)

## [setSensitiveMetaFields Embed2 Action now supported in Generative](https://docs.ada.cx/changelog/setsensitivemetafields-embed2-action-now-supported-in-generative)

Previously the [setSensitiveMetaFields action in Embed2](https://developers.ada.cx/reference/embed2-reference#setsensitivemetafields) action and [sensitiveMetaFields](https://developers.ada.cx/reference/embed2-reference#sensitivemetafields) setting were only supported in scripted bots, now it is supported in Generative AI Agents.

[August 16, 2024](https://docs.ada.cx/changelog/embed2-security-improvements)

## [Embed2 security improvements](https://docs.ada.cx/changelog/embed2-security-improvements)

We’ve released some security improvements to Embed2.

- If you’re using the Embed2 [NPM package](https://www.npmjs.com/package/@ada-support/embed2) , upgrade it to version **1.7.18 or newer**.
- The Embed2 script is versionless and gets automatic updates, so if you’re using it, you can already access the upgrades.

[August 12, 2024](https://docs.ada.cx/changelog/new-callback-events-in-embed2)

## [New callback events in Embed2](https://docs.ada.cx/changelog/new-callback-events-in-embed2)

We’ve added three new events to the [`subscribeEvent`](https://docs.ada.cx/reference/embed2-reference#subscribeevent) action in Embed2. With these events, you can provide your clients with a better experience after a bot or AI Agent has handed the conversation off to a human agent:

| Event key | Trigger |
| --- | --- |
| `ada:agent:joined` | Agent joined the conversation |
| `ada:agent:left` | Agent left the conversation |
| `ada:conversation:message` | Customer received a message |

If you’re using the Embed2 script, these events are immediately available. If you’re using the [NPM package](https://www.npmjs.com/package/@ada-support/embed2), update it to the latest version (1.7.17) to start using them.