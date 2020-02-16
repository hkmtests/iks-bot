import telebot

bot = telebot.TeleBot('942365550:AAECkeR06tfzlfzNiqnWikRx_hvbuQafEow')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, ')))')


@bot.message_handler(commands=['everyone'])
def start_message(message):
    msg = '❗️Вы были вызваны для привлечения внимания❗️'
    msg = msg + '\n' + '@o_may_gad_ya_chto_crazy' + '\n' + '@morkov_gryadochkin'
    msg = msg + '\n' + '@vlalub' + '\n' + '@jetsupertesla'
    msg = msg + '\n' + '@thehakama' + '\n' + '@varya_ko' '\n' + '@Pryalsw'

    bot.send_message(message.chat.id, + '\n' + '@o_may_gad_ya_chto_crazy' + '\n' + '@morkov_gryadochkin')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока')


bot.polling()
