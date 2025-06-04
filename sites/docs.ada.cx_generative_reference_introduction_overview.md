---
url: "https://docs.ada.cx/generative/reference/introduction/overview"
title: "API Overview | Ada | Documentation"
---

Ada’s suite of APIs opens up multiple integration paths to connect Ada with external systems, extending the capabilities of your AI agent.
Whether you’re looking to manage data stored in Ada or personalize conversations, Ada’s APIs supports numerous use cases, including:

- Syncing end user profile information in real time to enable your AI Agent to be knowledgable about your users and tailor responses.
- Managing and uploading business knowledge and policies from any source.
- Complying with data privacy regulations around data retention and deletion.
- Exporting conversation data for in-depth analysis or long term storage.

## Fundamentals

- Ada’s APIs adhere to REST standards and utilize JSON formatting for data exchange.

- Secure access is managed through [Authentication](https://docs.ada.cx/api-reference/knowledge/introduction/authentication) using rotatable keys.

- [Versioning](https://docs.ada.cx/api-reference/knowledge/introduction/versioning) allows to smoothly opt-in to breaking changes.

- Global [rate limits](https://docs.ada.cx/api-reference/knowledge/introduction/rate-limits) ensure high availability, with certain API families applying thier own local limits.

- [Cursor-based pagination](https://docs.ada.cx/api-reference/knowledge/introduction/pagination) supports efficient handling of large data sets.


## API Testing

Use the API Playground directly in these docs to test API calls.

[1](https://docs.ada.cx/generative/reference/introduction/overview#click-%EF%B8%8F-play)

### Click ▶️ Play

Next to every API call example, you’ll see a ▶️ Play button to open the playground. For example in [Knowledge Sources](https://docs.ada.cx/generative/reference/knowledge/sources/list):

![API Playground](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Fplay.png&w=3840&q=75)

[2](https://docs.ada.cx/generative/reference/introduction/overview#enter-your-api-key)

### Enter your API key

Click Login to enter your API key.

Your key is stored securely in your local browser session and will be cleared when the tab is closed.

[3](https://docs.ada.cx/generative/reference/introduction/overview#enter-your-subdomain)

### Enter your subdomain

Double-click the endpoint URL to replace `example` with your Ada instance’s subdomain. You can find your subdomain in the URL of your Ada dashboard.

[4](https://docs.ada.cx/generative/reference/introduction/overview#test-your-api-call)

### Test your API call

Send requests and review responses to validate your API calls.

## API Families

### Knowledge API

Use the [Knowledge API](https://docs.ada.cx/api-reference/knowledge/knowledge/introduction) to import and sync knowledge articles into Ada.

### End Users API

The [End Users API](https://docs.ada.cx/api-reference/end-users/introduction) offers allows for real-time updates and management of user profile information, including webhook events to track changes in user profiles.

### Export API

The [Data Export API](https://docs.ada.cx/api-reference/data-export/introduction) provides access to conversation and message records. You can use this API to export data into your own data warehouse for analysis and long-term storage.

### Compliance API

The [Data Compliance API](https://docs.ada.cx/api-reference/knowledge/compliance/introduction) allows for the deletion of personal data associated with a user’s email address from Ada’s databases.

### Integrations API

The [Integrations API](https://docs.ada.cx/api-reference/integrations/introduction) enables developers to connect external applications to Ada, such as Knowledge integrations that help AI agents generate responses, all managed from the Ada dashboard.

### Email Conversations API

The [Email Conversations API](https://docs.ada.cx/api-reference/email-conversations/introduction) allows developers to automate support by sending inquiries from sources like ticket backlogs or contact forms to Ada.

![API Playground](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Fplay.png&w=3840&q=75)