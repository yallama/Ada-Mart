---
url: "https://docs.ada.cx/generative/reference/conversations/eap-overview"
title: "Overview | Ada | Documentation"
---

## Conversations API EAP Guide

Capabilities available are subject to change during this EAP. This document will continue to be updated to reflect the latest information as functionality and operational procedures change during the EAP.

### **Disclaimer**

Customer agrees that the Conversations API features (the “ **Features**”) are being provided as “early access” features that are not ready for general commercial release and these features may contain bugs, errors, or defects. Accordingly, the Features are provided “as is.” Ada Support and our affiliates and licensors make no representations or warranties, or conditions of any kind, whether express, implied, statutory, or otherwise, regarding the Features, including any warranty or condition that the Features will become generally available and be uninterrupted or error-free. Ada Support may discontinue access to the Features at any time or for any reason.

**Use of the Conversations API is subject to any applicable [Service-Specific Terms](https://www.ada.cx/legal/service-specific-terms/) , as well as your Services Agreement with Ada (or Ada’s standard [Terms of Use](https://www.ada.cx/legal/website-terms/) if you do not have a signed Services [Agreement](https://www.ada.cx/legal/website-terms/))**

## Changelog

- 2025-04-11 - Initial publication

## Overview

The Conversations API lets you embed intelligent messaging or email AI Agents wherever your users are. This API also lets you programmatically manage conversations and messages between end users, AI Agents, and human agents.

Use this API to power your own messaging frontend, to integrate with your own email provider, or integrate your AI Agent in channels not otherwise supported out of the box by Ada.

### Capabilities

- Create a custom `email` or `messaging` channel where end users can reach your AI Agent
- Create a conversation between an end user and your AI Agent
- Send messages (text) to your AI Agent, and listen for webhook responses from your AI Agent
- End conversations on behalf of end users

### Limitations

The Conversations API is in Early Access. The following capabilities are **not yet supported**:

- Webhooks for messages sent by human agents
- Webhooks for conversation events taking place over Ada’s native Chat and Email channels
- Measuring CSAT via Ada’s Satisfaction Survey
- Sending message types other than `text`
- Reporting and analytics are not available for custom channels
- Managing custom channels in the Ada dashboard, including filtering on pages such as the Conversations View

### Known issues

- Channel `name` must be unique
- `author.display_name` and `author.avatar` values are not returned in webhook events. Integrators should save these values upon message creation in the interim.

### Providing Feedback / Reporting Issues

For questions or feedback, including reporting a bug, please contact your Ada representative. They will relay your feedback to the Product team. Ada’s Product team may contact you directly for further follow up.