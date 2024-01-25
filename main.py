import telebot

token = "6835030873:AAE7ys3xTvrpbhQOibZncsneXJJb4dStJcM"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, 'Hello')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
