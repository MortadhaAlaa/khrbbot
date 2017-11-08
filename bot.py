# -*- coding: utf-8 -*-
import os, logging
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, InlineQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def inline_khrb(bot, update):
    query = update.inline_query.query

    results = []
    if not query.isdigit():
        results.append(
            InlineQueryResultArticle(
                id=update.inline_query.id,
                title='بس اكتب/ي رقم',
                input_message_content=InputTextMessageContent('اكتب عدل')
            )
        )
        bot.answer_inline_query(update.inline_query.id, results)
        return

    num = int(query)
    num = min(2000, num)
    results.append(
        InlineQueryResultArticle(
            id=update.inline_query.id,
            title='خخخ تففففف',
            description=num // 3 * 'خ' + num // 3 * 'ر' + num // 3 * 'ب',
            input_message_content=InputTextMessageContent(num // 3 * 'خ' + num // 3 * 'ر' + num // 3 * 'ب')
            )
    )
    bot.sendMessage(chat_id='242879274', text='{} {}'.format(update.inline_query.from_user.username, num))    
    bot.answer_inline_query(update.inline_query.id, results)
    return

def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))

updater = Updater("479963878:AAGirDg6l3edmQ7nkHf6RVCnq_4BABEeYhk")

dp = updater.dispatcher
dp.add_handler(InlineQueryHandler(inline_khrb))
dp.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()
