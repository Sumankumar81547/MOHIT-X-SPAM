from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
    ],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/JARVIS_V_SUPPORT/5"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/R_I_S_I_NG")
    ],
    [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/Sumankumar81547/MOHIT-X-SPAM")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        ANNIE = await event.client.get_me()
        bot_name = ANNIE.first_name
        bot_id = ANNIE.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [MOHIT](https://t.me/Mohitkumar076)**\n\n"
        TEXT += f"» **ᴊᴀʀᴠɪs V2 :** `M 1.8.31`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
              event.chat_id,
                    "https://github.com/Sumankumar81547/MOHIT-X-SPAM/assets/155803358/f30a5777-9823-45d0-9860-342eceadb774",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
