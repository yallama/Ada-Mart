---
url: "https://docs.ada.cx/generative/reference/knowledge/overview"
title: "Overview | Ada | Documentation"
---

The Knowledge API allows you to manage and expand your AI Agent’s knowledge sources, extending beyond Ada’s out-of-the-box integrations. It provides methods to create, organize, and maintain multiple knowledge sources, enabling seamless integration of custom or external knowledge into your AI Agent.

The API exposes three main resources: Sources, Articles, and Tags. These resources are designed to help you organize and manage the knowledge available to your AI Agent effectively:

- [Sources](https://docs.ada.cx/generative/reference/knowledge/sources): Represent external knowledge sources, such as knowledge bases or documents. They help you organize and name the sources of information your AI Agent accesses. In Ada, every article must be associated with a source.
- [Articles](https://docs.ada.cx/generative/reference/knowledge/articles): Represent individual units of content within a knowledge source. These articles contain the information your AI Agent uses to resolve end-user inquiries.
- [Tags](https://docs.ada.cx/generative/reference/knowledge/tags): Serve as labels assigned to articles within a knowledge source. Tags make it easier to organize and retrieve content efficiently.

## Supported languages

Your AI Agent can have conversations in [multiple different languages](https://docs.ada.cx/docs/setup/languages/about-multilingual-support). However, knowledge content must be written in the following languages:

- English
- Arabic
- Chinese
- Dutch
- French
- German
- Italian
- Portuguese
- Spanish

* * *

## Rate limits

The Knowledge API adheres to our [global rate limits](https://docs.ada.cx/generative/reference/introduction/limits).

## Data limits

Along with rate limits, we’ve introduced restrictions on the number of articles that can be added, the size of individual articles, and the overall data size per request:

- Maximum number of articles: 50,000
- Maximum article size: 100KB
- Maximum request size: 10MB

## Request limits

Request URLs must be smaller than 2,048 bytes.