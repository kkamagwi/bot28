import telebot
import os

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['121'])
def gulliver(message):
    bot.send_message(message.chat.id, 'Я могу умножить любое число на 121')
    bot.send_message(message.chat.id, 'введите, пожалуйста, любое число')

@bot.message_handler(content_types=['text'])
def number(message):
    number = int(message.text) * 121
    text = 'Ваше число умножимое на 121 равно ' + str(number)
    bot.send_message(message.chat.id, text)

bot.polling()