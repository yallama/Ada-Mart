---
url: "https://docs.ada.cx/generative/reference/introduction/pagination"
title: "Pagination | Ada | Documentation"
---

Ada’s APIs use cursor-based pagination when retrieving large lists.
API calls can include an optional `limit` query parameter to specify the number of records returned per request.

## Request example

GET

/api/v2/end-users/

```code-block text-xs

$curl https://example.ada.support/api/v2/end-users/ \>     -H "Authorization: Bearer <token>"
```

### Query parameters

- `limit`: The number of records to return.
- `cursor`: The id that marks the start or beginning of the returned records. This is also provided in the `next_page_url` from the previous response.

## Response example

Response

```code-block text-xs

1{2  "data": [3    {4      "end_user_id": "5f7e0e2c1e7c7e000f0f9c3a",5      "profile": {6        "first_name": "Ada",7        "last_name": "Lovelace",8        "display_name": "Ada Lovelace",9        "avatar": "https://example.com/avatars/ada.png",10        "email": "ada.lovelace@ada.cx",11        "language": "en-US",12        "metadata": {},13        "system_properties": {14          "sunshine_user_id": "5f7e0e2c1e7c7e000f0f9c3a"15        }16      },17      "created_at": "2020-09-20T00:00:00+00:00",18      "updated_at": "2020-09-20T00:00:00+00:00"19    }20  ],21  "meta": {22    "next_page_url": "https://example.ada.support/api/v2/end-users/?cursor=65a17e3f43bec88e2792d0eb"23  }24}
```

Use the `next_page_url` to continue fetching additional data with subsequent requests.