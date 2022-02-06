#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modified By > @DC4_WARRIOR

from pyrogram import filters
from pyrogram import Client as Clinton
from plugins.youtube_dl_button import youtube_dl_call_back
from plugins.dl_button import ddl_call_back
from translation import Translation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.help_text import update

@Clinton.on_callback_query()
async def callback(bot, msg):
    if msg.data == "start":
        await msg.message.edit(
            text=f"""Hᴇʟʟᴏ 👋 , {update.from_user.mention} ♡
Tʜɪꜱ Iꜱ A Pᴏᴡᴇʀꜰᴜʟ Uʀʟ Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ.
Yᴏᴜ Cᴀɴ Uᴘʟᴏᴀᴅ Fɪʟᴇs/Vɪᴅᴇᴏ Fʀᴏᴍ Dɪʀᴇᴄᴛ Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ
Cʟɪᴄᴋ Oɴ Hᴇʟᴩ Bᴜᴛᴛᴏɴ Fᴏʀ Mᴏʀᴇ Iɴꜰᴏ...
Pᴏᴡᴇʀᴇᴅ ʙʏ : @AIOM_BOTS""",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Hᴇʟᴘ", callback_data="start"),
                    InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
                ],
                [   InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")],
            ]
        )
        )
    elif msg.data == "help":
        await msg.message.edit(
            text=Translation.HELP_USER,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Hᴏᴍᴇ", callback_data="start"),
                    InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
                ],
                [   InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")],
            ]
        )
        )
    elif msg.data == "about":
        await msg.message.edit(
            text=Translation.ABOUT_TEXT,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Hᴏᴍᴇ", callback_data="help"),
                    InlineKeyboardButton("Hᴏᴍᴇ", callback_data="start"),
                ],
                [   InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")],
            ]
        )
        )

@Clinton.on_callback_query(filters.regex('^X0$'))
async def delt(bot, update):
          await update.message.delete(True)


@Clinton.on_callback_query()
async def button(bot, update):

    cb_data = update.data
    if "|" in cb_data:
        await youtube_dl_call_back(bot, update)
    elif "=" in cb_data:
        await ddl_call_back(bot, update)
