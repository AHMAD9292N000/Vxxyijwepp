import asyncio
import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import app
from random import  choice, randint
import os, webbrowser
import asyncio
import requests
from pyrogram import Client
import aiohttp
import aiofiles
from pyrogram import enums
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus , ChatType
from pyrogram.types import ChatPermissions, ChatPrivileges
import yt_dlp
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InputTextMessageContent
from youtube_search import YoutubeSearch
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from MatrixMusic import app
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup as Markup,
    InlineKeyboardButton as Button
)

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

import asyncio
from strings.filters import command
from MatrixMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import OWNER_ID


@app.on_callback_query(filters.regex("devatari"))
async def zzzback(_, query: CallbackQuery):

    
    usm = await client.get_users(OWNER_ID)
    mname = usm.first_name
    musrnam = usm.username
    
    chat = message.chat.id
    gti = message.chat.title
    chatusername = f"@{message.chat.username}"
    link = await app.export_chat_invite_link(chat)
    usr = await client.get_users(message.from_user.id)
    user_id = message.from_user.id
    user_ab = message.from_user.username
    user_name = message.from_user.first_name
    buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await app.send_message(OWNER_ID, f"<b>↯︙قام {message.from_user.mention}\n</b>"
                                     f"<b>↯︙بمناداتك عزيزي المطور\n</b>"
                                     f"<b>↯︙الأيدي {user_id}\n</b>"
                                     f"<b>↯︙اليوزر @{user_ab}\n</b>"
                                     f"<b>ايدي المجموعة {message.chat.id}\n</b>",
                                     reply_markup=reply_markup)

    # إنشاء زر "اونلاين"
    online_button = InlineKeyboardButton(mname, url=f"https://t.me/{musrnam}")
    
    await message.reply_text(f"<b>↯︙تم إرسال النداء إلى مطور البوت\n\n↯︙Dᥱꪜ - @{musrnam} .</b>",
                             disable_web_page_preview=True,
                             reply_markup=InlineKeyboardMarkup([[online_button]]))

@app.on_message(
    command(["المطور اتاري"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("A1RTR")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"– – – – – – – – – – – – – – – – – –\n↯︙𝖣𝖾𝗏 ↬ ⦗ {name} ⦘\n↯︙𝖴𝗌𝖤𝗋 ↬ ⦗ @{usr.username} ⦘\n↯︙𝖨𝖣 ↬ ⦗ {usr.id} ⦘\n↯︙𝖡𝗂𝖮 ↬ ⦗ {usr.bio} ⦘\n– – – – – – – – – – – – – – – – – –",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}"),
                  ],[
                    
                ],
            ]
        ),
     )
    
@app.on_message(command(["مطورين","مطورين السورس","المطورين"]))
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f98c8fd479b206648d6c8.jpg",
        caption=f"""↯︙اهلا بك عزيزي {message.from_user.mention}\n↯︙مطورين سورس ماتركس ميوزك""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ : 𝖣𝖾𝗏 : ›", url=f"https://t.me/A1RTR"), 
                 ],[
                    InlineKeyboardButton(
                        "‹ : 𝖣𝖾𝗏 : ›", url=f"https://t.me/NUNUU"),
                ],[
                    InlineKeyboardButton(
                        "‹ : 𝖬𝖺𝖳𝗋𝗂x 𝖳𝖾𝖠𝗆 : ›", url=f"https://t.me/KKKK5Z"),
                ],

            ]

        ),

    )
