---
url: "https://docs.ada.cx/generative/reference/introduction/errors"
title: "Errors | Ada | Documentation"
---

Ada’s API uses conventional HTTP response codes to indicate the success or failure of API requests. In general:

- Codes in the `2xx` range indicate success
- Codes in the `4xx` range indicate errors caused by the request
- Codes in the `5xx` range indicate errors on our servers

## HTTP Status Code Summary

| Status Code | Error Type | Description |
| --- | --- | --- |
| 400 | Bad Request | The request was malformed or contained invalid parameters |
| 401 | Unauthorized | Authentication credentials were missing or invalid |
| 403 | Authorization Error | The authenticated user lacks permission to access the resource |
| 404 | Not Found | The requested resource doesn’t exist |
| 409 | Duplicate Resource | A resource with the same identifier already exists |
| 413 | Content Too Large | The request payload exceeds size limits |
| 422 | Unprocessable Content | The request syntax was valid but the content cannot be processed |
| 429 | Too Many Requests | Rate limit exceeded - too many requests in a given time period |
| 500 | Internal Server Error | Something went wrong on our servers |

## Error Response Format

All error responses follow this format:

```code-block text-sm

1{2  "errors": [3    {4      "type": "error_type",5      "message": "Human readable message",6      "details": "Optional, additional error details"7    }8  ]9}
```