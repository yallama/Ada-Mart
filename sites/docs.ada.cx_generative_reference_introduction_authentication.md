---
url: "https://docs.ada.cx/generative/reference/introduction/authentication"
title: "Authentication | Ada | Documentation"
---

Ada APIs use API keys for authentication. An API key is required to authenticate requests and enable integration with Ada’s platform.

- **Support for Multiple Keys:** Maintain multiple active API keys to enable seamless key rotation when needed.
- **Non-Expiring:** API keys remain valid until manually revoked.
- **Access:** API keys grant both read and write permissions for all APIs available to your organization.

To create a new API key, follow the steps in [Generate an Ada API key](https://docs.ada.cx/generative/reference/introduction/authentication#generate-an-ada-api-key).

To use an API key, simply include it as a `Bearer` token in the `Authorization` header of your requests. See [Authenticate your requests](https://docs.ada.cx/generative/reference/introduction/authentication#authenticate-your-requests) for detailed instructions.

If you are already using API-specific keys, they will only work for the v1 version of the designated API. These keys are labeled with the API name followed by “(Legacy)”.

## Generate an Ada API key

You can generate a new Ada API key from the Ada dashboard, which works for all APIs your organization has access to.

1. On the Ada dashboard, go to your API settings.


   - If you’re using a **generative AI Agent**, go to **Platform** \> **APIs**.
     ![](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Fae394ec-api-auth-generative-dashboard.png&w=3840&q=75)
   - If you’re using a **scripted bot**, go to **Settings** \> **Integrations** \> **APIs**.
     ![](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2F8554873-api-auth-scripted-dashboard.png&w=3840&q=75)

The API keys page opens.

2. Create a new API key:


   - If your AI Agent doesn’t have any API keys, click **Get started**.
   - If your AI Agent has existing API keys, click **New API key**.

The New API key window opens.

3. In the New API key window, enter a **Name** for the key, then click **Generate key**.

You won’t be able to change the key’s name in the future.
![](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2F037a625-api-auth-generate-key.png&w=3840&q=75)
4. Click **Copy** to copy your API key, then save it in a secure place immediately.









For security reasons, the Ada dashboard only displays your API key once. If you lose this key, you’ll need to create a new one.

5. Click **Done** to close the New API Key window and protect your new API key.


## Delete an Ada API key

If you ever need to invalidate an old API key, click the **Delete** button beside it.

![](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Fc959293-api-auth-delete-key.png&w=3840&q=75)

## Authenticate your requests

To authenticate your requests, you have to send your API key in the Authorization header in all requests to the API. Without it, your requests will fail.

### Example of a request

JSON

```code-block text-sm

1curl --location '{BOT_URL}/api/knowledge/v1/articles' \2--header 'Authorization: Bearer {YOUR_API_TOKEN}'
```

### Example responses

JSON

```code-block text-sm

1// If the request is not authenticated2status: 4013{4	"message": "Unauthorized"5}67// If the request is authenticated8status: 2009{10	"data": []11}
```

![](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Fae394ec-api-auth-generative-dashboard.png&w=3840&q=75)

![](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2F8554873-api-auth-scripted-dashboard.png&w=3840&q=75)

![](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2F037a625-api-auth-generate-key.png&w=3840&q=75)

![](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Fc959293-api-auth-delete-key.png&w=3840&q=75)