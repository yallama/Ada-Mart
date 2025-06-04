---
url: "https://docs.ada.cx/generative/reference/introduction/migrate-to-v-2"
title: "Migrate to v2 APIs | Ada | Documentation"
---

We’re excited to introduce you to Ada’s v2 APIs and the new capabilities they offer our platform. In this guide, we’ll walk you through the key changes and provide actionable steps to help you transition from v1 to v2 smoothly.

## Key Improvements and Changes

### Updated Endpoints

The v2 API consolidates several legacy endpoints, reducing redundancy and making integration simpler. Endpoints are organized by resource and action, allowing you to find exactly what you need more quickly.

Reference the v2 documentation to see which endpoints map to your existing v1 calls. Here’s an example mapping for the End Users API:

- **v1**: `https://example.ada.support/api/end-users/v1/`
- **v2**: `https://example.ada.support/api/v2/end-users/`

### Streamlined API Tokens

The v2 API consolidates API tokens so they work across all endpoints. In v1, it was necessary to create an API token for each API. In v2, you can create a single token that works with all endpoints across APIs. Learn more about [creating new API tokens](https://docs.ada.cx/generative/reference/introduction/authentication).

Legacy API keys are not compatible with v2 endpoints.

### Uniform Response Structures

In v1, responses could vary significantly from endpoint to endpoint. In v2, responses (including errors) follow a consistent JSON structure, making it easier for you to parse data and handle errors uniformly across different API calls.

### Standardized Pagination

v2 API also introduces standardized cursor-based pagination across all endpoints, ensuring a consistent experience when retrieving large sets of data. Pagination parameters such as `page`, `limit`, and `cursor` are uniformly applied, and responses include clear metadata about the pagination state. For more details, refer to the [pagination guide](https://docs.ada.cx/generative/reference/introduction/pagination).

### Improved Rate and Data Limits

The v2 API introduces more transparent rate limit and data limit policies. This helps you plan your requests, ensures better reliability, and prevents service degradation from unexpected traffic spikes.

## Backward-Incompatible Changes

Some functionality has been deprecated or updated in a backward-incompatible way. Be sure to review any endpoints or parameters you currently rely on and confirm their v2 equivalents. When in doubt, [check the v2 documentation](https://docs.ada.cx/generative/reference/introduction/overview).

## Migration Steps

[1](https://docs.ada.cx/generative/reference/introduction/migrate-to-v-2#review-the-v2-documentation)

### Review the v2 documentation

Start by familiarizing yourself with the [v2 API overview](https://docs.ada.cx/generative/reference/introduction/overview). Identify endpoints and parameters equivalent to those you use in v1.

[2](https://docs.ada.cx/generative/reference/introduction/migrate-to-v-2#update-authentication)

### Update authentication

Replace legacy tokens with new shared platform API tokens. Review our [authentication guide](https://docs.ada.cx/generative/reference/introduction/authentication) in the v2 docs for setup instructions and example code.

[3](https://docs.ada.cx/generative/reference/introduction/migrate-to-v-2#test-in-a-staging-environment)

### Test in a staging environment

Before switching over in production, test your updated requests in a staging or sandbox environment. This helps you catch and fix integration issues early.

[4](https://docs.ada.cx/generative/reference/introduction/migrate-to-v-2#monitor-and-optimize)

### Monitor and optimize

After you roll out v2 in production, keep an eye on your logs, response times, and error rates. Adjust your usage if you encounter unexpected behavior or require further optimization.