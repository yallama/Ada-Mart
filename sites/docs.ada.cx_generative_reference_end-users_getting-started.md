---
url: "https://docs.ada.cx/generative/reference/end-users/getting-started"
title: "Getting started | Ada | Documentation"
---

## Change conversation language based on end user’s selection on any channel

### Before you begin

Before you start, make sure you have everything you need:

- An [API token](https://docs.ada.cx/generative/reference/introduction/authentication) stored securely in Ada’s [Token\\
Vault](https://docs.ada.cx/docs/scripted/integrate-ada-with-other-tools/securely-store-api-tokens-using-the-token-vault/)

### Configure languages in your bot

1. In your bot’s language settings, configure the following:
   - Ensure [multilingual and auto-translation](https://docs.ada.cx/docs/scripted/build-and-maintain-your-bot/personalize-conversations/support-multiple-languages-in-the-same-bot/#UUID-8604b076-6ac5-26e7-2da3-c5c5bd8af5e6_id_360018374134_id_h_01G05GVYQ2GDTPR020ET8K25T8) are enabled in your bot.
   - [Enable language support](https://docs.ada.cx/docs/scripted/build-and-maintain-your-bot/personalize-conversations/support-multiple-languages-in-the-same-bot/#UUID-8604b076-6ac5-26e7-2da3-c5c5bd8af5e6_id_360018374134_id_h_01G05GVYQ2GDTPR020ET8K25T8) in your dashboard for one or two additional languages. We’ll use French and Portuguese in this example.
2. In your bot’s greeting, use a List Option block to present the language options you selected to your user.
3. Use a Request block to set the end user’s language to their list selection.
![](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Fconfigure-languages.png&w=3840&q=75)










Language codes must be in BCP 47 4-digit format, per the [End Users API schema](https://example.ada.support/api/end-users/v1/docs#/End-Users/updateEndUserById).

4. Save your greeting.
5. Test the greeting in your Test Bot, embed, or any other channel. The conversation language should change immediately based on the end user’s selection, and the bot should immediately respond using the appropriate translation.

## Get notified at your webhook when an Ada end user is created or updated

### Before you begin

Before you set up your webhook, make sure you have everything you need:

- An Ada dashboard with the [Test Bot](https://docs.ada.cx/docs/scripted/build-and-maintain-your-bot/test-your-bot/) enabled (or any other supported channel where your bot is active)
- An [API token](https://docs.ada.cx/generative/reference/introduction/authentication)

### Set up your webhook

1. Set up a test webhook, or bring your own, with Ada’s webhooks manager.
1. On the Ada dashboard, find your webhook settings.
      - If you’re using a **generative AI Agent**, go to **Platform** \> **Webhooks**.
      - If you’re using a **scripted bot**, go to **Settings** \> **Integrations** \> **Webhooks**.
2. Click **Add Endpoint** to get started. If you don’t have your own endpoint, [configure a test endpoint using Svix Play](https://docs.svix.com/receiving/using-app-portal/adding-endpoints).
3. In the Message Filtering section, subscribe to both `v1.end_user.updated` and `v1.end_user.created` events.
4. Click **Create** to save your endpoint.
2. Open your Test Bot in a new tab or window and start a conversation.
3. In a separate tab, open the Webhooks Logs to monitor new events. You’ll see the conversation with your Test Bot has created an end user! There will be a corresponding log entry called `v1.end_user.created`.
4. Click on the log to see the webhook event payload and copy the `end_user_id` value.
5. Make a [PATCH request](https://docs.ada.cx/reference/end-user/patch-end-user-by-id) with the following payload:









JSON









```code-block text-sm




1{2   "profile": {3      "first_name": "Ada",4      "last_name": "Lovelace",5      "display_name": "Ada Lovelace",6      "avatar": "https://example.com/avatars/ada.png",7      "email": "ada.lovelace@ada.cx",8      "language": "en-US",9      "metadata": {10         "end_user_api_test": true11      }12   }13}
```

6. Check the Webhooks Logs tab. A successful PATCH request will generate a `v1.end_user.updated` log.
7. You can continue to chat with Test Bot while making these changes to the end user. The End Users API can update records at any point whether a conversation is active or not. Go ahead and send a few messages to your bot!
8. Finally, go the Conversations View and find your conversation. You’ll see that the metavariables are updated from the PATCH request.

That’s it! You have the building blocks to create an integration between your customer data platform and Ada’s End Users API. Your integration can ingest webhook events and use the PATCH endpoint to send user details to Ada so that features such as [Article Rules](https://docs.ada.cx/docs/generative/set-up-your-ai-agent-s-knowledge-and-behavior/manage-your-knowledge-content#article-rules) can be applied automatically for your end users.

![](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Fconfigure-languages.png&w=3840&q=75)