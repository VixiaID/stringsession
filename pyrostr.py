from pyrogram import Client

template = """
<i><b>Please don't share with anyone</b></i>

<code>{}</code>

By: <a href='tg://user?id=1285496612'>『ᴏᴛsᴇᴇ』</a>"""
with Client(
"UserBot",
api_id=int(input("Enter API ID: ")),
api_hash=input("Enter API HASH: ")) as pyrogram:
    saved_messages_template = template.format(pyrogram.export_session_string())
    print("\nGeneratimg String Session...\n")
    pyrogram.send_message("me", saved_messages_template, parse_mode="html")
    print("Your String Session have been send to your Telgram Saved Messages")
