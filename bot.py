# -*- coding: utf-8 -*-
import os, logging
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, InlineQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

token = os.environ['TELEGRAM_TOKEN']

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
        bot.sendMessage(chat_id='242879274', text='{} {}'.format(update.inline_query.from_user.username, query))    
        return

    num = int(query)
    num = min(2000, num)
    num = max(3, num)
    
    if num == 69:
        results.extend([
            InlineQueryResultArticle(
                id=update.inline_query.id + 'k',
                title='خخخ تففففف',
                description=num // 3 * 'خ' + num // 3 * 'ر' + num // 3 * 'ب',
                input_message_content=InputTextMessageContent('شفتك سمير')
            ),
            InlineQueryResultArticle(
                id=update.inline_query.id + 't',
                title='خخخ تففففف',
                description=num // 4 * 'ت' + num // 4 * 'ف' + num // 4 * 'ل' + num // 4 * 'ت',
                input_message_content=InputTextMessageContent('شفتك سمير')
            ),
            InlineQueryResultArticle(
                id=update.inline_query.id + 'f',
                title='خخخ تففففف',
                description=num // 4 * 'ف' + num // 4 * 'ط' + num // 4 * 'س' + num // 4 * 'ت',
                input_message_content=InputTextMessageContent('شفتك سمير')
            ),
            InlineQueryResultArticle(
                id=update.inline_query.id + 'm',
                title='خخخ تففففف',
                description='م' + (num-1) * 'ت',
                input_message_content=InputTextMessageContent('شفتك سمير')
            ),
            InlineQueryResultArticle(
                id=update.inline_query.id + 'r',
                title='حقوق الطبع محفوظة لمكتب السيد @MortadhaAlaa',
                input_message_content=InputTextMessageContent('تاجراسكم صاحب البوت')
            )
        ])
        bot.answer_inline_query(update.inline_query.id, results)
        bot.sendMessage(chat_id='242879274', text='{} {}'.format(update.inline_query.from_user.username, num))    
        return
    
    results.extend([
        InlineQueryResultArticle(
            id=update.inline_query.id + 'k',
            title='خخخ تففففف',
            description=num // 3 * 'خ' + num // 3 * 'ر' + num // 3 * 'ب',
            input_message_content=InputTextMessageContent(num // 3 * 'خ' + num // 3 * 'ر' + num // 3 * 'ب')
        ),
        InlineQueryResultArticle(
            id=update.inline_query.id + 't',
            title='خخخ تففففف',
            description=num // 4 * 'ت' + num // 4 * 'ف' + num // 4 * 'ل' + num // 4 * 'ت',
            input_message_content=InputTextMessageContent(num // 4 * 'ت' + num // 4 * 'ف' + num // 4 * 'ل' + num // 4 * 'ت')
        ),
        InlineQueryResultArticle(
            id=update.inline_query.id + 'f',
            title='خخخ تففففف',
            description=num // 4 * 'ف' + num // 4 * 'ط' + num // 4 * 'س' + num // 4 * 'ت',
            input_message_content=InputTextMessageContent(num // 4 * 'ف' + num // 4 * 'ط' + num // 4 * 'س' + num // 4 * 'ت')
        ),
        InlineQueryResultArticle(
            id=update.inline_query.id + 'm',
            title='خخخ تففففف',
            description='م' + (num-1) * 'ت',
            input_message_content=InputTextMessageContent('م' + (num-1) * 'ت')
        ),
        InlineQueryResultArticle(
            id=update.inline_query.id + 'r',
            title='حقوق الطبع محفوظة لمكتب السيد @MortadhaAlaa',
            input_message_content=InputTextMessageContent('تاجراسكم صاحب البوت')
        )
    ])
    bot.sendMessage(chat_id='242879274', text='{} {}'.format(update.inline_query.from_user.username, num))    
    bot.answer_inline_query(update.inline_query.id, results)
    return

def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))

updater = Updater(token)

dp = updater.dispatcher
dp.add_handler(InlineQueryHandler(inline_khrb))
dp.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()
