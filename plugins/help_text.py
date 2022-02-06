#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config
# the Strings used for this "thing"
from translation import Translation

from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as Clinton
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Clinton.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Clinton.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Help", callback_data="help"),
                    InlineKeyboardButton("About", callback_data="donate"),
                ],
                [   InlineKeyboardButton("Close", callback_data="close")],
            ]
        ),
        reply_to_message_id=update.message_id
   )

@Clinton.on_callback_query()
async def callback(bot, update):
    if update.data == "start":
        await update.message.edit(
            text=Translation.START_TEXT.format(update.from_user.mention)
        )
   
    elif update.data == "help":
          await update.message.edit(
              text=Translation.HELP_USER
          )
    elif update.data == "about":
          await update.message.edit(
              text=Translation.ABOUT_TEXT
          )

@Clinton.on_callback_query(filters.regex('^close$'))
async def close_cb(c, m):
    await m.message.delete()
    await m.message.reply_to_message.delete()

@RenamerNs.on_callback_query(filters.regex('^donate$'))
async def donate(c, m):
    button = [[
        InlineKeyboardButton('Home', callback_data='back'),
        InlineKeyboardButton('About', callback_data='about')
        ],[
        InlineKeyboardButton('Close', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(button)
    await m.answer()
    await m.message.edit(
        text=Translation.HELP_USER,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

