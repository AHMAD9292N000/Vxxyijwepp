import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from MatrixMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["ميوزك", "الميوزك", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d893816c7a714f06b8a25.mp4",
        caption=f"""» مرحبـاً بك عـزيـزي\n» استخـدم الازرار بالاسفـل 𝄞\n» لـ تصفـح اوامـر الميـوزك 🥁</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامر التشغيل •", callback_data="zzzll"),
                    InlineKeyboardButton(
                        "• اوامر القنوات •", callback_data="zzzch"),
                ],[
                    
                    InlineKeyboardButton(
                        "• اوامــر الادمــن •", callback_data="zzzad"),

                    InlineKeyboardButton(
                        "• اوامــر المطــور •", callback_data="zzzdv"),
                ],[ 
                    InlineKeyboardButton(
                        "• مطور السورس •", url="https://t.me/A1RTR") 
                ],[
                    InlineKeyboardButton(
                        "• سورس بلاك •", url="https://t.me/vvizinn"),
                ],
            ]
        ),
    )
