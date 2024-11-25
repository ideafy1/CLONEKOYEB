import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    ADMIN_IDS = [int(id) for id in os.getenv("ADMIN_ID").split()]
    MONGODB_URI = os.getenv("MONGODB_URI")
    DB_NAME = os.getenv("DB_NAME")
    DATABASE_CHANNEL = int(os.getenv("DATABASE_CHANNEL"))
    
    # Constants
    START_TEXT = """🚀 Build Your Own File Store Bot with @juststoreitbot

No coding needed! Get a powerful, feature-packed bot to store, share, and manage your files with ease. From custom access controls and batch uploads to real-time stats and 24/7 availability—this bot has it all.

Need more? You can even request additional features to make it truly your own!

👉 Click here to read the full list of features and get started!"""

    HELP_TEXT = """✨ Help Menu

I am a permanent file store bot. You can store files from your public channel without me being admin in there. If your channel or group is private, first make me admin in there. Then you can store your files using the commands below and access stored files using shareable links.

📚 Available Commands:
➛ /start - Check if I am alive.
➛ /genlink - To store a single message or file.
➛ /batch - To store multiple messages from a channel.
➛ /custom_batch - To store multiple random messages.
➛ /shortener - To shorten any shareable links.
➛ /settings - Customize your settings as needed.
➛ /broadcast - Broadcast messages to users (moderators only).
➛ /ban - Ban a user (moderators only).
➛ /unban - Unban a user (moderators only)."""

    ABOUT_TEXT = """✨ ᴀʙᴏᴜᴛ ᴍᴇ

✰ ᴍʏ ɴᴀᴍᴇ: ꜰɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ
✰ ᴍʏ ᴏᴡɴᴇʀ: Crazy Developer
✰ ᴜᴘᴅᴀᴛᴇs: Crazy
✰ sᴜᴘᴘᴏʀᴛ: Crazy
✰ ᴠᴇʀsɪᴏɴ: 0.7.9"""