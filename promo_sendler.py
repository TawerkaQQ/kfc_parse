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
TEST_M = getenv("TEST_M")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def send_promo(bot: types.Message):
    promo_photo = FSInputFile('kupon-kfc-5050-1.jpg')
    await bot.send_message(TEST_M, 'PROMO')
    # await message.answer(f'{promo}'
    #     )


async def main():
    await send_promo(bot)

if __name__ == "__main__":

    # promo, url = parse_html()
    # print(promo)
    # print(url)

    #promo_photo = FSInputFile(out)

    asyncio.run(main())

