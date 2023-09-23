import asyncio
import logging
import sys
from os import getenv

import aioschedule
import requests
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bs4 import BeautifulSoup

TOKEN = getenv("6500455580:AAHVSXBNh1J8UZOn_p0lfDQc2h3ZjZz8qAg")
url = "https://www.meteoblue.com/ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0/%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F/%d0%a3%d0%bb%d1%8c%d1%8f%d0%bd%d0%be%d0%b2%d1%81%d0%ba_%d0%a0%d0%be%d1%81%d1%81%d0%b8%d1%8f_479123"
menu_photo = open("pictures/weat.png", 'rb')

# All handlers should be attached to the Router (or Dispatcher)
bot = Bot(token='6500455580:AAHVSXBNh1J8UZOn_p0lfDQc2h3ZjZz8qAg')
dp = Dispatcher()

main_buttons = [
    [
        types.KeyboardButton(text="Меню🌤"),
        types.KeyboardButton(text="FAQ⁉️")
    ],
    [
        types.KeyboardButton(text="Отзывы🗣"),
    ]
]
main_keyboard = types.ReplyKeyboardMarkup(keyboard=main_buttons)


inline_main_buttons = InlineKeyboardBuilder()
inline_main_buttons.button(text="Меню🌤", callback_data='main_menu')
inline_main_buttons.button(text="FAQ⁉️", callback_data='faq')
inline_main_buttons.button(text="Отзывы🗣", callback_data='feedback')
inline_main_buttons.adjust(2)


inline_menu_buttons = InlineKeyboardBuilder()
inline_menu_buttons.button(text='Выбрать свой город', callback_data='change_city')
inline_menu_buttons.button(text='Создать оповещение', callback_data='weather_warning')
inline_menu_buttons.button(text='Назад', callback_data='back_main')
inline_menu_buttons.adjust(2)


async def FindWeather():
    bs = BeautifulSoup(response.text, "html.parser")
    temp = bs.find('div', 'cell hide-desktop')
    await bot.send_message(734313964, temp.text)


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer_photo(photo='https://is1-ssl.mzstatic.com/image/thumb/Purple125/v4/6a/78/83/6a78830f-9b5f-9315-d42a-89bd317a980e/WeatherAppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/1200x630wa.png',
                               caption="Добро пожаловать в WeatBot!",
                               reply_markup=inline_main_buttons.as_markup())
    await scheduler()


@dp.message(Command('menu'))
async def command_menu(message: Message):
    await message.answer(f"Добро пожаловать!", reply_markup=main_keyboard)


@dp.message()
async def handle_text(message: types.Message):
    a = "pictures/pogoda.jpeg"
    await bot.send_photo(message.chat.id,
                         photo="https://is1-ssl.mzstatic.com/image/thumb/Purple125/v4/6a/78/83/6a78830f-9b5f-9315-d42a-89bd317a980e/WeatherAppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/1200x630wa.png",
                         caption="Ваш текст здесь.")
    await message.answer(f"Вы написали: {message.text}")


async def scheduler():
    aioschedule.every().day.at("03:21").do(FindWeather)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


@dp.callback_query(F.data.startswitch())


@dp.callback_query(F.data == 'main_menu')
async def main_keyboard_menu(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=inline_menu_buttons.as_markup())


@dp.callback_query(F.data == 'faq')
async def faq_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("Кнопка изменена на FAQ")


@dp.callback_query(F.data == 'feedback')
async def feedback_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("Кнопка изменена на Отзывы")


async def main():
    bot = Bot(token='6500455580:AAHVSXBNh1J8UZOn_p0lfDQc2h3ZjZz8qAg', parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


try:
    response = requests.get(url)
    print(response)

    while True:
        if __name__ == "__main__":
            logging.basicConfig(level=logging.INFO, stream=sys.stdout)
            asyncio.run(main())

except Exception:
    print('Error, url didnt exists.')
    exit(0)
