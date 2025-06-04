---
url: "https://docs.ada.cx/generative/reference/integrations/overview"
title: "Overview | Ada | Documentation"
---

![Integration overview](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Fintegration-guide-overview-2.png&w=3840&q=75)

The **Integrations API** allows developers to extend Ada’s capabilities by creating integrations that connect external applications to Ada. These integrations can be installed and managed directly from the **Ada dashboard**.

An example of an integration is a Knowledge integration, which links an external Help Center or knowledge base and creates articles in Ada, enabling AI Agents to generate responses.

Partner developers can:

- Integrate any system with Ada’s suite of Platform APIs.
- Publish integrations to Ada’s Integrations Directory, available for anyone using Ada to install.
- Restrict installation access to specific organizations by keeping integrations private, if the integration is not intended to be discoverable by Ada customers.

Admins can:

- Discover available integrations in your Ada dashboard, where they appear as sources on the Knowledge page.
- Install and configure integrations for other applications in their stack.
- Augment their AI Agent’s capabilities through these integrations.

Integrations can be published or private. To build a private integration with Ada, follow steps 1-2. To publish an integration discoverable by any Ada customer, follow steps 1-4:

1. Build an integration server that Ada can communicate with when AI agent managers install your integration. This server will handle key tasks required for your integration to function.
2. Register your integration with your development bot. At this point, the integration is considered “private.” The integration may remain in this state if you wish for it to be accessible for specific organizations.
3. Before deployment, test the installation, configuration, and uninstallation processes thoroughly to ensure everything works as expected.
4. Once your integration is fully tested and ready, publish it by submitting it to [developer-partnerships@ada.support](mailto:developer-partnerships@ada.support). When an integration is published, any Ada customer can discover and install it from the Ada dashboard.

For more details about building and publishing an integration, see [Getting Started](https://docs.ada.cx/generative/reference/integrations/getting-started).

* * *

## OAuth

OAuth is a secure authorization framework that enables integrations to access Ada’s resources. It allows users to grant access to their data while maintaining applicable permissions and security. Implementing OAuth correctly ensures a seamless authentication experience, minimizes security risks, and enables smooth communication between Ada’s platform and external integrations.

The Integration Framework uses OAuth to install an integration to a given Ada AI Agent. The AI Agent Manager completes an OAuth flow from their Ada instance, and the integration server managed by the partner developer authorizes the installation.

* * *

## Becoming a Partner

To submit an integration and become a partner developer, please reach out to [developer-partnerships@ada.support](mailto:developer-partnerships@ada.support).

![Integration overview](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Fintegration-guide-overview-2.png&w=3840&q=75)