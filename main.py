import asyncio

import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from weather import get_weather_text

# логи
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "7769208980:AAFt0muBqXAgfkMSdrvcHUbGF98_0XaGc8M" # токен телеграмм-бота
API_WEATHER_TOKEN = "c99cfaedfd084cf9859184232242210" # api погоды
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Введи команду /weather, чтобы получить погоду в Санкт-Петербурге.")

# Здесь должен быть хэндлер на команду /weather
@dp.message(Command("weather"))
async def get_weather(message: types.Message):
    await message.answer(get_weather_text(API_WEATHER_TOKEN))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())