from pyrogram import Client, filters
from random import  choice, randint
from MatrixMusic import app
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)

@app.on_message(filters.command(["تخ"]) & filters.group)
async def huhh(client, message):
    user = message.from_user
    await message.reply_animation(
        animation="https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
        caption=f"""≭︰قتل ↫ ⦗ {message.from_user.mention} ⦘\n≭︰الضحيه دا 😢 ↫ ⦗ [{user.first_name}](tg://user?id={user.id}) ⦘\nانا لله وانـا اليـه راجعـون 😢😢""",
        reply_markup=InlineKeyboardMarkup(
            [
               [
                   InlineKeyboardButton(
                       "‹ 𝐁𝐥𝐚𝐜𝐤 𝐓𝐞𝐀𝐦 ›", url="https://t.me/vvizinn"),
               ],
           ]
        )
    )
