---
url: "https://docs.ada.cx/generative/reference/introduction/limits"
title: "Limits | Ada | Documentation"
---

Ada’s API enforces rate and data limits to ensure stability and prevent abuse. These limits are applied per Ada instance.

## Rate Limits

Global rate limits apply across all endpoints:

- Requests per day: 10,000
- Requests per minute: 100
- Requests per second: 10

Exceeding these limits will result in a `429 Too Many Requests` error. Implement retry logic with exponential backoff and jitter to handle these responses and minimize disruptions.

Some endpoints may also enforce **local rate limits**. Refer to the documentation for each API endpoint for details on additional restrictions.

## Data Limits

- Max request body size: 10MB

Exceeding this size will result in a `413 Content Too Large` error.

Some endpoints may also enforce **local data limits**. Refer to the documentation for each API endpoint for details on additional restrictions.