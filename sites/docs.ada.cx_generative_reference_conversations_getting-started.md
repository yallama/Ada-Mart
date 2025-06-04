---
url: "https://docs.ada.cx/generative/reference/conversations/getting-started"
title: "Getting started | Ada | Documentation"
---

![Integration overview](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2FConversations-api.png&w=3840&q=75)

### Who is this for?

Use this API to power your own messaging frontend, to integrate with your own email provider, or integrate your AI Agent in channels not otherwise supported out of the box by Ada.

### Core concepts

**Channel:** A channel represents a communication pathway through which customers interact with your business for support. Custom channels created through the Conversations API are either `messaging` or `email` modality.

**Conversation:** A conversation is a sequence of messages exchanged between participants on a specific channel. Participants can be the end user, AI Agent, or human agents.

**Message:** Messages are authored by participants. The Conversations API supports text messages.

### Webhook support

The Conversations API supports event notifications that enable you to track conversations and messages. The following events are currently supported:

`v1.conversation.created` : triggered when a new conversation is created over a custom channel

`v1.conversation.ended` : triggered when `POST /v2/conversations/{conversation_id}/end/` is called from the Conversations API

`v1.conversation.message` : triggered when a new message is added to a custom channel conversation

For more details on how to implement and use webhooks, refer to the [**webhook documentation**](https://developers.ada.cx/reference/introduction/webhooks).

## Talk to your AI Agent over a custom channel

### **Setting up**

Generate API key, if you don’t already have one

[Create a webhook](https://developers.ada.cx/reference/introduction/webhooks#adding-an-endpoint) and [subscribe to conversation events](https://developers.ada.cx/reference/introduction/webhooks#supported-events)

### 1\. **Create a channel**

Make sure you declare a `modality` so that the AI Agent responds to users in the corresponding style.

###### Request example

Shell

```code-block text-sm

$    POST https://{bot-handle}.ada.support/api/v2/channels>    Authorization: Bearer <your-api-token>>    >        {>          "name": "My Custom Channel",>          "description": "A custom messaging channel for my AI Agent",>          "modality": "messaging",>          "metadata": {>            "webpage_host": "https://lovelace-chat.com">          }>        }
```

### 2\. **Create a conversation over your channel**

If you have an existing end user, include their End User ID in the payload.

Otherwise, the Conversations API will make a new end user automatically. Make sure you save the End User ID from the response so you can send messages from this End User in the next step.

When a conversation is successfully created, you’ll receive a `v1.conversation.created` webhook event if subscribed.

###### Request example

Shell

```code-block text-sm

$    POST https://{bot-handle}.ada.support/api/v2/conversations>    Authorization: Bearer <your-api-token>>    >        {>        "channel_id": "5df263b7db5a7e6ea03fae9b",>        "metadata": {>            "started_from_help_center": true>            }>        }
```

### 3\. **Send a message on behalf of the End User**

###### Request example

Shell

```code-block text-sm

$    POST https://{bot-handle}.ada.support/api/v2/conversations/{conversation_id}/messages>    Authorization: Bearer <your-api-token>>    >        {>        "author": {>            "id": "5f7e0e2c1e7c7e000f0f9c3a",>            "role": "end_user",>            "avatar": "https://www.gravatar.com",>            "display_name": "Ada Lovelace">            }>        },>        "content": {>            "body": "I need help with my order",>            "type": "text">            }>        }
```

When a message is successfully sent, you’ll receive a `v1.conversation.message` webhook event if subscribed. Note that the `author.role` will be `end_user`.

### 4\. **Listen for AI Agent response**

When the AI Agent responds to your end user’s inquiry, you’ll receive a `v1.conversation.message` webhook event if subscribed. Note that the `author.role` will be `ai_agent`.

### 5\. **End a conversation on behalf of an end user**

To end a conversation on behalf of the end user, call

```code-block text-sm

POST /v2/conversations/{conversation_id}/end/
```

![Integration overview](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2FConversations-api.png&w=3840&q=75)