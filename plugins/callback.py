#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modified By > @DC4_WARRIOR

from pyrogram import filters
from pyrogram import Client as Clinton
from plugins.youtube_dl_button import youtube_dl_call_back
from plugins.dl_button import ddl_call_back

@Clinton.on_callback_query()
async def callback(bot, msg):
    if msg.data == "start":
        await msg.message.edit(
            text=Translation.START_TEXT.format(update.from_user.mention)
        )
    elif msg.data == "help":
        await msg.message.edit(
            text="working"
        )
    elif msg.data == "about":
        await msg.message.edit(
            text=Translation.ABOUT_TEXT
        )
