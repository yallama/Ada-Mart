---
url: "https://docs.ada.cx/generative/reference/email-conversations/getting-started"
title: "Getting started | Ada | Documentation"
---

To use the Email Converations API, you’ll have to use a form provider (such as Zendesk) or set up your own system that can make a POST API call when you receive an email inquiry that should be sent to Ada for email automation. This call sends form submission or email content to your AI Agent via Ada’s Email Conversations API.

## Implementation flow

1. Choose the email address you want the AI Agent to use when replying to end users.
   - If you haven’t already, configure this in the **Bring your own domain** section of the **Email** configuration page.
2. [Generate an Email Conversations API key](https://docs.ada.cx/generative/reference/introduction/authentication#generate-an-ada-api-key) in the Ada Dashboard.

3. Set up your API call with the required fields:


   - **Endpoint URL**: Make POST calls to this endpoint, replacing `{bothandle}` with your AI Agent’s handle.
     `https://{bothandle}.ada.support/api/v2/conversations/email`








     Your AI Agent handle can be found in the upper left corner of your dashboard, above the left navigation bar.

   - **Authentication key**: The key you generated in the Ada Dashboard.
   - **Payload for the call**: The payload for the call is the email content or form submission that should be sent to Ada for email automation. For example:

```code-block text-sm

1{2        "name": "FirstName LastName",3        "text": "Email body",4        "subject": "Email subject",5        "reply_as" : "help@company.com",6        "reply_to": "user@mail.com",7        "metadata": {8            "ticket_id": "1001"9        }10    }
```

For details, review this [section](https://docs.ada.cx/generative/reference/email-conversations/create-email-conversation#request).

4. Set up the required automations to route inquiries to Ada (e.g., Webhook, Triggers in Zendesk).

5. Test your flow.

6. When you’re ready to route live inquiries to Ada via Email API, set up forwarding for your **Bring your own domain** email address. This ensures end-user replies to the AI Agent are correctly routed to the AI Agent for conversation continuity.


## Understanding response codes

You may receive the following responses after your call is sent. To troubleshoot errors, first review the returned response.

| Response Code | Details | Additional Troubleshooting Checks |
| :-- | :-- | :-- |
| `200` | Success | Conversation ID is returned |
| `400` | Invalid request, body or headers | Check your payload to troubleshoot- your field should be one of the supported fields and types |
| `401` | Unauthorized request | Check that you’ve provided an auth header and that your API key is correct |
| `422` | Unprocessable content | Check that your `reply_as` and `reply_to` is not the same email address. If it is, we consider it a forwarding loop and reject the request |
| `429` | Too many requests | Rate limit exceeded |
| `500` | Server error | Indicates that something went wrong on Ada’s end |

* * *

## Examples

That’s all you need to know to get started. Next, explore these sample workflows. Each one outlines the key steps for its respective integration. Use these examples as a guide to assist with your setup.

###### Example: Set up Zendesk ticket forms

You can configure a Zendesk ticket form, and create a webhook and trigger to automatically forward content your customers submit to your AI Agent.

1. **Create a webhook**

Follow Zendesk’s instructions on [creating a webhook](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks-to-interact-with-third-party-systems#topic_bwm_1tv_dpb), so you can use Zendesk to point to Ada’s API.


   - When you’re configuring your endpoint URL, use `https://{bothandle}.ada.support/api/v2/conversations/email`, replacing `{bothandle}` with your own bot handle.
   - When you’re adding your API key, select the “Bearer Token” option. Paste your API key as the value for the “Token” field. You will have generated your token on the API page in the Platform section of the Dashboard.

When the webhook is configured, it should look like this:
![Zendesk: Email API authentication](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Femail-api-zd-auth.png&w=3840&q=75)
2. **Create a trigger**

Follow Zendesk’s instructions on [creating ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466-Creating-triggers-for-automatic-ticket-updates-and-notifications#topic_qfk_s23_vsb), so Zendesk can automatically call your webhook as soon as it receives a response to your form.


   - We recommend these conditions:
     - Ticket > Ticket **Is** Created
     - Ticket > Attachment **Is not** Present
     - Ticket > Form **Is** \[Name of Your Webform Submission Form\]

![Zendesk: Trigger conditions](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Femail-zendesk-trigger-conditions-example.png&w=3840&q=75)

If your Ticket > Form condition uses the Default Form, and this form is also shared with other channels (e.g., calls or chats), create a new basic form and set it as the new default. This will ensure you have a dedicated form for Webform Submissions. Otherwise, inquiries from other channels may be routed to Ada via the Email API.

   - For your trigger actions, you can have any combination of actions, but we recommend using these two:
     - **Call your webhook**
       1. Choose **Add action** \> **Notify by** \> **Active webhook**.

       2. Select the webhook you created.

       3. For the JSON body, use the following. Make sure to replace the `reply_as` address with either your AI Agent’s Ada-provided email address ( `help@{bothandle}.email.ada.support`) or the address you’ve set up in your **Bring your own domain** settings.



          ```code-block text-sm




          {"name":"{{ticket.requester.name}}","reply_to":"{{ticket.requester.email}}","reply_as":"help@example.ada.support","subject":"{{ticket.title}}","text":"{{ticket.latest_public_comment}}","metadata": {    "ticket_id": "{{ticket.id}}"}}
          ```
     - **Close your ticket**
       1. Click **Add action** \> **Status category**.
       2. Select **Closed**.

With the two above actions, your configuration should look like this:
![Zendesk actions example](https://prod.ferndocs.com/_next/image?url=https%3A%2F%2Ffiles.buildwithfern.com%2Fhttps%3A%2F%2Fada.docs.buildwithfern.com%2F2025-06-03T20%3A37%3A42.166Z%2Fversions%2Fassets%2Fimages%2Femail-zendesk-actions-example-ada.png&w=3840&q=75)

###### Example: Set up Salesforce contact forms

You can create a Salesforce case form, and create an automated process to automatically forward content your customers submit to your AI Agent. You, or someone with Salesforce Admin permissions, can

1. **Set up your Salesforce case fields**
1. Add your Ada email as a case origin you can track in Salesforce, so you can track which cases were passed to your AI Agent. Follow Salesforce’s instructions in [Add Picklist Values](https://help.salesforce.com/s/articleView?id=sf.fields_picklist_add_values.htm&type=5). For your **Cases**, in the **Case Origin** field, add a picklist value with your Ada-provided email address ( `help@{bothandle}.email.ada.support`) as the value.
2. Create a new checkbox, so your automation flow can track which cases it’s already sent to Ada and doesn’t send duplicates. Follow Salesforce’s instructions in [Create Custom Fields](https://help.salesforce.com/s/articleView?id=sf.adding_fields.htm&type=5), and create a checkbox with the following attributes:

      - Type: Checkbox; default unchecked
      - Name: Sent to Ada
      - Visible to all users
      - Read-only for all users except System Administrators profile
      - Do not add to layout
3. Click **Save**.
2. **Set up a flow to send case data to Ada**
1. Add your API credentials to Salesforce so it can use Ada’s API to send over email data. Follow Salesforce’s instructions to [Create or Edit a Basic Authentication External Credential](https://help.salesforce.com/s/articleView?id=sf.nc_create_edit_basic_auth_ext_cred.htm&type=5), and enter the following information:


      - **Label**: `Ada Email API External Credential`
      - **Name**: `AdaEmailAPIExternalCredential`
      - **Authentication Protocol**: `No Authentication`

Additionally, follow the instructions in the above link to create a principal, to act as a user for the credentials you just made. Use the following information:
      - **Parameter Name**: `User`
      - **Sequence Number**: `1`
      - **Identity Type**: `Named Principal`
2. Instead of putting your authentication in the credentials, add a custom header. Follow Salesforce’s instructions to [Create and Edit Custom Headers](https://help.salesforce.com/s/articleView?id=sf.nc_create_custom_headers.htm&type=5), and enter the following information:
      - **Name**: Authorization
      - **Value**: Bearer <YOUR-API-KEY>. Paste in the API key you generated from the API page in the Ada Dashboard.
      - **Sequence Number**: `1`
3. Create a permission set, so you can share the credentials you just made with other admins. Follow Salesforce’s instructions to [Create Permission Sets](https://help.salesforce.com/s/articleView?id=sf.perm_sets_create.htm&type=5), and do the following:
      - **Name**: `Ada Email Http Callout`
      - Click **External Credential Principal Access**, then add the `Ada Email API External Credential` you created
      - Follow Salesforce’s instructions to [Manage Permission Set Assignments](https://help.salesforce.com/s/articleView?id=sf.perm_sets_manage_assignments.htm&type=5) to assign the new permission set to yourself and any other admins
4. Create a named credential. Follow Salesforce’s instructions to [Create or Edit a Named Credential](https://help.salesforce.com/s/articleView?id=sf.nc_create_edit_named_credential.htm&type=5), and enter the following information:
      - **Label**: `Ada Email API Named Credential`
      - **Name**: `AdaEmailAPINamedCredential`
      - **URL**: `https://{bothandle}.ada.support/api/v2/conversations/email`, replacing `{bothandle}` with your AI Agent’s handle
      - Under **Authentication**, under **External Credential**, select the `Ada Email API External Credential` you created earlier
3. **Create a flow to automate closing cases**
1. Create a flow to update the case’s status to Closed. Follow Salesforce’s instructions to [Build a Flow](https://help.salesforce.com/s/articleView?id=sf.flow_build.htm&type=5), and do the following:

      - Create a **Record-Triggered Flow**
      - **Object**: `Case`
      - **Trigger the Flow When**: `A record is created or updated`
      - **Condition Requirements**: `All Conditions are Met (AND)`
      - `Origin` `Equals` `Ada Email`
      - `Status` `Does Not Equal` `Closed`
      - **When to Run the Flow for Updated Records**: `Every time a record is updated and meets the condition requirements`
      - **Optimize the Flow for**: `Fast Field Updates`
2. Add an Update Triggering Record element to the flow. In the **New Update Records** window, enter the following information:

      - **Label**: `Update Status`
      - **API Name**: `Update_Status`
      - **How to Find Records to Update and Set Their Values**: `Use the case record that triggered the flow`
      - **Condition Requirements to Update Record**: `None - Always Update Record`
      - **Field**: `Status`
      - **Value**: `Closed`
3. Save and activate your flow, giving it a name like `CASE: Update Ada Email Status to Closed`.
4. **Create a flow to automate sending cases to Ada, using an HTTP callout**
1. Create a new flow to automatically send cases to Ada. Follow Salesforce’s instructions to [Build a Flow](https://help.salesforce.com/s/articleView?id=sf.flow_build.htm&type=5), and do the following:
      - Create a **Record-Triggered Flow**
      - **Object**: `Case`
      - **Trigger the Flow When**: `A record is created or updated`
      - **Condition Requirements**: `All Conditions are Met (AND)`
      - `Origin` `Equals` `Ada Email`
      - `Status` `Does Not Equal` `Closed`
      - `Sent_to_ada__c` `Equals` `False`
      - **When to Run the Flow for Updated Records**: `Only when a record is updated to meet the condition requirements`
      - **Optimize the Flow for**: `Actions and Related Records`
2. Add a scheduled path to the flow. Follow Salesforce’s instructions to create [Scheduled Paths](https://help.salesforce.com/s/articleView?id=sf.flow_concepts_trigger_scheduled_path.htm&type=5), and add the following information:
      - **Path Label**: `API to Ada`
      - **API Name**: `API_to_Ada`
      - **Time Source**: `Case: Last Modified Date`
      - **Offset Number**: `1`
      - **Offset Options**: `Minutes After`
      - **Advanced** \> **Batch Size**: `1`
3. Add an HTTP callout to the flow. Follow Salesforce’s instructions to [Configure an HTTP Callout Action](https://help.salesforce.com/s/articleView?id=sf.flow_http_callout_configure.htm&type=5), and add the following information:


      1. External service configuration:
         - **Category**: `HTTP Callout`
         - **Named Credential**: `Ada Email API Named Credential`
      2. Invocable action:


         - **Label**: `Ada Email Invocable Action`
         - **Method**: `POST`
         - **Sample JSON request**:

```code-block text-sm

{    "name":"{{ticket.requester.name}}",    "reply_to":"{{ticket.requester.email}}",    "reply_as":"help@example.ada.support",    "subject":"{{ticket.title}}",    "text":"{{ticket.latest_public_comment}}",    "metadata": {    "ticket_id": "{{ticket.id}}"    }}
```

         - **Sample response body**: Not required

This creates an Apex class variable that you can use in step e, so you can specify individual dynamic fields to send.

4. Now that you’ve configured the action, add it to your flow, so you can use the API callout to send cases to Ada. Use the following information:
      - **Name**: `Send to Ada`
      - **API Name**: `SendtoAda`
      - **Body**: `Apex-Defined Variable`
      - **Value**: Create a variable called `AdaEmailBody`
5. In your flow, add an assignment element **before** the action element you just added. You can see an example at Salesforce’s [Flow Element: Assignment](https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_assignment.htm&type=5) topic. Enter the following information:


      - **Label**: `Set Body Variables`
      - **API Name**: `Set_Body_Variables`

Then, add each of the following variables by choosing the Apex-defined variable you created above, then the corresponding fields in your Salesforce case:

      - `AdaEmailBody > name` `Equals` `$Record > Name`
      - Optional: `AdaEmailBody > replyx5fas` `Equals` `help@company.com`
      - `AdaEmailBody > replyx5fto` `Equals` `$Record > Email Address`
      - `AdaEmailBody > subject` `Equals` `$Record > Subject`
      - `AdaEmailBody > text` `Equals` `$Record > Description`
      - `AdaEmailBody > metadata > ticket` `Equals` `$Record > Case ID`

Ensure that all of the above values are on your case creation form, with the exception of your reply-as email.

6. Add an Update Triggering Record element to the flow. In the **New Update Records** window, enter the following information:
      - **Label**: `Update Sent to Ada checkbox on Case`
      - **API Name**: `Update_Sent_to_Ada_checkbox_on_Case`
      - **How to Find Records to Update and Set Their Values**: `Use the case record that triggered the flow`
      - **Condition Requirements to Update Record**: `None - Always Update Record`
      - **Field**: `Sent_to_Ada__c`
      - **Value**: `True`
7. Save and activate your flow, giving it a name like `CASE: Send to Ada Email`.
5. Test your flow. Create a case with a `Case Origin` of `Ada Email`, and use a valid email address to test. You should be able to see the conversation appear in Ada, and get a reply at the email address you provided.