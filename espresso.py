import config
from text import esp_hello_inv, esp_hello_ing, esp_step_2, esp_step_3, esp_step_4, esp_step_5, esp_step_6
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


def esp_hello(message):
    bot.send_message(message.chat.id, "Давайте приготовим эспрессо!")
    bot.send_message(message.chat.id, esp_hello_inv)
    bot.send_message(message.chat.id, esp_hello_ing)
    """bot.send_message(message.chat.id, "")"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Всегда готов!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы?", reply_markup=keyboard)


def esp_step1(message):
    bot.send_message(message.chat.id, "Первый шаг:\nПеремолите зерна.")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Always ready - англ.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы?", reply_markup=keyboard)


def esp_step2(message):
    bot.send_message(message.chat.id, "Второй шаг:")
    bot.send_message(message.chat.id, esp_step_2)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Alltid klar - норв.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def esp_step3(message):
    bot.send_message(message.chat.id, "Третий шаг:")
    bot.send_message(message.chat.id, esp_step_3)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Alltid redo - швед.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def esp_step4(message):
    bot.send_message(message.chat.id, "Четвертый шаг:")
    bot.send_message(message.chat.id, esp_step_4)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Aina valmiina - фин.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def esp_step5(message):
    bot.send_message(message.chat.id, "Пятый шаг:")
    bot.send_message(message.chat.id, esp_step_5)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Altid klar - дат.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def esp_step6(message):
    bot.send_message(message.chat.id, esp_step_6)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Завершить работу.")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Завершить работу?", reply_markup=keyboard)
