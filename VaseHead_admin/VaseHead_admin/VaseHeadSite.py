from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler, CallbackQueryHandler)
import logging
import time
from VaseHead_admin.bot_settings import *
from VaseHead_admin.conversation import Conversation
from VaseHead_admin.response_maker import GiveBot
from itertools import filterfalse
import datetime, threading

conversations = []

def isTimeoured(c:Conversation):
    if ( datetime.datetime.now() - c.datetime).total_seconds() > 600:
        return True
    return False
def session_watchdog():
    threading.Timer(60.0, session_watchdog).start()
    conversations[:] = filterfalse(isTimeoured, conversations)
    print('Total sessions:' + str(len(conversations)))

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def catch_message(bot, update):
    conversation = next((x for x in conversations if x.id == update.message.chat_id), None)
    if conversation != None:
        conversation.ProcessMessage(bot, update)
    else:
        newconversation = Conversation(update.message.chat_id)
        newconversation.ProcessMessage(bot, update)
        conversations.append(newconversation)

def catch_inline(bot, update):
    conversation = next((x for x in conversations if x.id == update.callback_query.message.chat_id), None)
    if conversation != None:
        conversation.ProcessInline(bot, update)
    else:
        newconversation = Conversation(update.callback_query.message.chat_id)
        newconversation.ProcessInline(bot, update)
        conversations.append(newconversation)

class Bot():
    bot_instance = "nello"
    def __init__(self):
        conversations = []
        print('bot created')

    def Start(self):
        session_watchdog();
        updater = Updater(GetSettingsValue(bot_token))
        dp = updater.dispatcher
        GiveBot(updater)
        dp.add_handler(MessageHandler(Filters.all, catch_message))
        dp.add_handler(CallbackQueryHandler(catch_inline))
        dp.add_error_handler(error)
        updater.start_polling()
        updater.idle()

            
