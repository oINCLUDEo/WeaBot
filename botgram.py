import asyncio
import logging
import sys
from os import getenv

import requests, schedule
from bs4 import BeautifulSoup

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
import aioschedule

TOKEN = getenv("6500455580:AAHVSXBNh1J8UZOn_p0lfDQc2h3ZjZz8qAg")
url = "https://www.meteoblue.com/ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0/%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F/%d0%a3%d0%bb%d1%8c%d1%8f%d0%bd%d0%be%d0%b2%d1%81%d0%ba_%d0%a0%d0%be%d1%81%d1%81%d0%b8%d1%8f_479123"

# All handlers should be attached to the Router (or Dispatcher)
bot = Bot(token='6500455580:AAHVSXBNh1J8UZOn_p0lfDQc2h3ZjZz8qAg')
dp = Dispatcher()


async def FindWeather():
    bs = BeautifulSoup(response.text, "html.parser")
    temp = bs.find('div', 'cell hide-desktop')
    await bot.send_message(734313964, temp.text)


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    await scheduler()


@dp.message()
async def handle_text(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")


async def scheduler():
    aioschedule.every().day.at("12:00").do(FindWeather)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def main() -> None:
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
