from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch


@app.on_message(filters.command(["بحث","يوت"], ""), group=4458890044)
async def ytsearch(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) < 2:
            return await message.reply_text("جار البحث في سيرفرات سورس بلاك")
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("يتم البحث الان ...")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"≭︰العنوان : {results[i]['title']}\n"
            text += f"≭︰المدة : {results[i]['duration']}\n"
            text += f"≭︰المشاهدات : {results[i]['views']}\n"
            text += f"≭︰القناة : {results[i]['channel']}\n"
            text += f"≭︰الرابط : https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        key = InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                        "‹ 𝐁𝐥𝐚𝐜𝐤 𝐓𝐞𝐀𝐦 ›", url=f"https://t.me/vvizinn"),
                ],[
                    InlineKeyboardButton(
                        text="‹ اغلاق ›",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        )
        await m.edit_text(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply_text(str(e))
