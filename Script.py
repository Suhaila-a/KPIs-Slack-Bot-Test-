import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Set the SLACK_APP_TOKEN and SLACK_BOT_TOKEN environment variables
# These are found on the Slack API page for your app
app_token = os.environ["SLACK_APP_TOKEN"]
bot_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=bot_token)

# Set the user IDs of the users you want to send the message to
user_ids = ["USER_ID_1", "USER_ID_2"]

try:
    # Call the chat.postMessage method using the WebClient
    for user_id in user_ids:
        response = client.chat_postMessage(
            channel=user_id,
            text="Hello!"
        )
        print(response)
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    # (caused by an error returned by the Slack API)
    print("Error sending message: {}".format(e))
