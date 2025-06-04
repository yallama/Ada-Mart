---
url: "https://docs.ada.cx/generative/reference/introduction/webhooks"
title: "Webhooks | Ada | Documentation"
---

Webhooks are a powerful mechanism that Ada uses to notify your systems in real-time about specific events occurring within the platform. By configuring webhook endpoints, you can integrate Ada with your existing systems to automate workflows and enhance operational efficiency.

**Key Features:**

- Secure communication using HTTPS.
- Automatic [retries](https://docs.ada.cx/generative/reference/introduction/webhooks#retry-policy) up to a week.
- Comprehensive logging for monitoring delivery and failures.
- Message [replay](https://docs.ada.cx/generative/reference/introduction/webhooks#message-replay) to recover from downtime or missed events.

To ensure reliable delivery, webhooks require a 2xx HTTP status response within 15 seconds. If no response is received, retries are automatically initiated based on an exponential backoff [retry policy](https://docs.ada.cx/generative/reference/introduction/webhooks#retry-policy).

To create a webhook, navigate to **Platform > Webhooks** in your dashboard. See [Adding an Endpoint](https://docs.ada.cx/generative/reference/introduction/webhooks#adding-an-endpoint) for more details.

## Supported Events

Ada supports event notifications that enable you to track specific user actions and updates. The following events are currently supported:

- [`v1.end_user.created`](https://docs.ada.cx/generative/reference/end-users/end-user-created-webhook): Triggered when a new user is created through any of Ada’s supported channels.
- [`v1.end_user.updated`](https://docs.ada.cx/generative/reference/end-users/end-user-updated-webhook): Triggered when a value on the end user’s profile changes.
- `v1.conversation.created`: triggered when a new conversation is created over a custom channel
- `v1.conversation.ended`: triggered when `POST /v2/conversations/{conversation_id}/end/` is called from the Conversations API
- `v1.conversation.message`: triggered when a new message is added to a custom channel conversation

## Retry Policy

Ada employs an exponential backoff retry mechanism to ensure reliable webhook delivery. This mechanism is triggered when an endpoint fails to respond with a 2xx HTTP status code. Below is the retry schedule:

**Retry Schedule:**

1. Immediate retry after failure.
2. 5 seconds later.
3. 5 minutes later.
4. 30 minutes later.
5. 2 hours later.
6. 5 hours later.
7. 10 hours later (repeated for up to 2 attempts).

**Failure Handling:**

- If all attempts to deliver to an endpoint fail for **one week**, the endpoint will be automatically disabled.
- Manually re-enable endpoints through the Webhooks UI when they are ready to resume operations.

## Adding an Endpoint

To begin receiving webhooks, you must configure an endpoint:

1. Navigate to **Platform > Webhooks** in your dashboard.
2. Click **Add Endpoint**.
3. Provide a URL: Specify a URL that your system controls.
4. Select Event Types: Choose the events you wish to subscribe to.
5. Click **Create**.

Best Practice: Start with all event types enabled for initial testing and narrow down to relevant types for production to minimize extraneous messages.

## Testing Webhooks

Testing ensures that your webhook endpoints are functioning as intended. Tools such as [ngrok](https://ngrok.com/) or [localtunnel](https://github.com/localtunnel/localtunnel) can simulate real-world scenarios by exposing a local server for testing. Alternatively, you can use Ada’s webhooks UI with [Svix Play](https://play.svix.com/) for a quick and easy setup.

### Svix Play

If you don’t have a URL ready or your service isn’t prepared to receive events, simply press the Use Svix Play button in the webhooks UI. This will generate a unique URL for testing purposes.

- Events will be sent to your Svix Play URL and automatically logged in Message Attempts section of the webhooks UI.

Svix Play is strictly for testing and should not be used in production environments.

## Message Replay

Replaying messages can be crucial in several scenarios:

- **Service Downtime**: If your service experiences downtime, you can recover missed messages.
- **Misconfigured Endpoint**: If your endpoint was misconfigured, replaying ensures no data is lost.
- **Single Event Replay**: To replay a single event, go to the log section, use the menu next to the message, and select the “resend” option to send the message to your endpoint again.

### Resend Message

To resend a single event, simply click “resend” in the options menu from the log section, and the message will be sent to your endpoint once more.

### Recovering from Service Outage

If you need to recover from a service outage and replay all events since a specific time, navigate to the Endpoint page. On an endpoint’s details page, click Options > Recover Failed Messages. From there, you can choose a time window to recover from.

## Troubleshooting Common Issues

• Response Timeout: Ensure your endpoint processes messages within the allotted 15-second window. Offload complex workflows to asynchronous processes to avoid timeouts.
• Incorrect Response Codes: Always respond with a 2xx HTTP status code to indicate successful processing.