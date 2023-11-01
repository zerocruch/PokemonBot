import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import os

api = "https://pokeapi.co/api/v2/pokemon/"

botToken = "Your Bot Token"

bot = telebot.TeleBot(botToken)

@bot.message_handler(func=lambda message: True)
def start(message):
    try:
        photo = open('photo.jpg', 'wb')
        req = requests.get(
            f'{api}{message.text.lower()}'
            ).json()['sprites']["other"]["home"]["front_default"]
        photo.write(requests.get(req).content)
        photo.close()
        # Send the downloaded photo to the chat
        with open('photo.jpg', 'rb') as photo_file:
            bot.send_photo(message.chat.id,
             photo_file)
        os.remove('photo.jpg')
    except Exception:
        bot.send_message(message.chat.id,
         f"Unable To Generate Image")



bot.infinity_polling()

#https://www.facebook.com/zerocruch/
#https://tiktok.com/@zerocruch
#https://www.youtube.com/@zerocruch
#https://www.instagram.com/zerocruch_
