from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = input("Enter API ID: ")
API_HASH = input("Enter API HASH: ")

template = """
<i><b>Please don't share with anyone</b></i>

<code>{}</code>

By: <a href='tg://user?id=1285496612'>『ᴏᴛsᴇᴇ』</a>"""

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    str = client.session.save()
    saved_messages_template = template.format(str)
    print("\nGeneratimg Strung Session...\n")
    client.send_message("me", saved_messages_template, parse_mode="html")
    print("Your String Session have been send to your Telgram Saved Messages")

