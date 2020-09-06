from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import config


def start(update, context):
    greetings = 'Бот обратной связи. Все следующие твои сообщения будут отправлены, но по одиночке. ' \
                'Умести мысль в одно сообщение.'
    update.message.reply_text(greetings)


def get_and_forward_message(update, context):

    if str(update.message.chat.id) != '-432964642':
        text = update.message.text
        user_id = update.message.chat.id
        user_name = update.message.from_user.first_name
        message_id = update.message.message_id

        update.message.reply_text('Сообщение отправлено.\n')

        sended_message = 'Сообщение от: ' + user_name + '\n'
        sended_message += str(user_id) + '\n'
        sended_message += str(message_id) + '\n\n' + text

        update.message.bot.send_message(text=sended_message, chat_id='-432964642')
    else:
        try:
            id_to_reply = update.message.reply_to_message.message_id - 2

            text = update.message.text
            data = update.message.reply_to_message.text
            chat_id_to_reply = data.split('\n')[1]
            message_id_to_reply = data.split('\n')[2]

            if id_to_reply == int(message_id_to_reply):
                update.message.bot.send_message(chat_id=chat_id_to_reply, text=text)
        except (AttributeError, IndexError):
            pass


def main():
    mybot = Updater(config.TOKEN, use_context=True)
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', start, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, get_and_forward_message))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
