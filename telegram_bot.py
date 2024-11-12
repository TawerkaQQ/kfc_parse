import urllib.request as req
from http.client import responses
import asyncio
import requests

from os import getenv
from aiogram import Bot, Dispatcher, types
from aiogram.types import URLInputFile, FSInputFile, InputFile
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from dotenv import load_dotenv
from urllib3 import request

from parse_html import parse_html

load_dotenv()
TOKEN = getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f'''Привет {message.from_user.first_name}! Данный бот присылает акцию 5050 в KFC каждую среду :) \n
                        Чтобы получить акцию нажми /promo
    '''
    )

@dp.message(Command("promo"))
async def send_promo(message: types.Message):
    promo_photo = FSInputFile('kupon-kfc-5050-1.jpg')
    await message.answer_photo(promo_photo)
    print(message.from_user.id)
    #await message.answer(f'{promo}')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":

    # promo, url = parse_html()
    # print(promo)
    # print(url)

    promo_photo = FSInputFile('kupon-kfc-5050-1.jpg')

    asyncio.run(main())

