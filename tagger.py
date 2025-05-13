from pyrogram import Client, filters
from pyrogram.types import Message
from database import load_admins, save_admins
from utils import is_admin, get_flag, get_emoji

admins = load_admins()

@Client.on_message(filters.command("reload") & filters.group)
async def reload_admins(client, message: Message):
    global admins
    chat_admins = await client.get_chat_members(message.chat.id, filter="administrators")
    admins = [member.user.id for member in chat_admins]
    save_admins(admins)
    await message.reply_text("✅ Yönetici listesi güncellendi.")

async def tag_users(client, message: Message, symbol: str):
    if not is_admin(message.from_user.id, admins):
        return await message.reply_text("❌ Bu komutu sadece yöneticiler kullanabilir.")
    if len(message.command) < 2:
        return await message.reply_text("ℹ️ Etiket mesajı girin. Örnek: `/utag Merhaba!`")
    text = message.text.split(None, 1)[1]
    chat_members = [m async for m in client.get_chat_members(message.chat.id)]
    tagged = ""
    for user in chat_members:
        if user.user.is_bot: continue
        mention = user.user.mention(symbol)
        tagged += f"{mention} "
    await message.reply_text(f"{text}\n\n{tagged}")

@Client.on_message(filters.command("utag") & filters.group)
async def utag_handler(client, message):
    await tag_users(client, message, "@")

@Client.on_message(filters.command("atag") & filters.group)
async def atag_handler(client, message):
    await tag_users(client, message, "")

@Client.on_message(filters.command("btag") & filters.group)
async def btag_handler(client, message):
    await tag_users(client, message, get_flag())

@Client.on_message(filters.command("etag") & filters.group)
async def etag_handler(client, message):
    await tag_users(client, message, get_emoji())

