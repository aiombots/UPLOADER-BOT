#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modified By > @DC4_WARRIOR

from pyrogram import filters
from pyrogram import Client as Clinton
from plugins.youtube_dl_button import youtube_dl_call_back
from plugins.dl_button import ddl_call_back
from translation import Translation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Clinton.on_callback_query()
async def callback(bot, msg):
    if msg.data == "start":
        await msg.message.edit(
            text=f"""Hᴇʟʟᴏ 👋 , ♡

Tʜɪꜱ Iꜱ A Pᴏᴡᴇʀꜰᴜʟ Uʀʟ Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ.

Yᴏᴜ Cᴀɴ Uᴘʟᴏᴀᴅ Fɪʟᴇs/Vɪᴅᴇᴏ Fʀᴏᴍ Dɪʀᴇᴄᴛ Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ

Cʟɪᴄᴋ Oɴ Hᴇʟᴩ Bᴜᴛᴛᴏɴ Fᴏʀ Mᴏʀᴇ Iɴꜰᴏ...

Pᴏᴡᴇʀᴇᴅ ʙʏ : @AIOM_BOTS""",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                    InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
                ],
                [   InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")],
            ]
        )
        )
    elif msg.data == "help":
        await msg.message.edit(
            text=Translation.HELP_USER,
            disable_web_page_preview=True,
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
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                    InlineKeyboardButton("Hᴏᴍᴇ", callback_data="start"),
                ],
                [   InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")],
            ]
        )
        )

    elif msg.data == "x0":
        await msg.message.delete(True)

    elif msg.data == "close":
        await msg.message.delete(True)

    elif cb_data == msg.data
    if "|" in cb_data:
        await youtube_dl_call_back(bot, msg)
    elif "=" in cb_data:
        await ddl_call_back(bot, msg)
