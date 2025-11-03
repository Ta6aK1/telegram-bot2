import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiohttp import web

TOKEN = "8392127432:AAHPSqCf3r-AUMmhLhf1WKf8YIp0HEU5JK0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Главное меню
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Товары")]
    ],
    resize_keyboard=True
)

@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Выберите действие:", reply_markup=main_kb)

@dp.message(lambda msg: msg.text == "🛍 Товары")
async def show_products(message: types.Message):
    products_text = (
        "Наши товары:\n\n"
        "1️⃣ Товар A — 100₽\n"
        "2️⃣ Товар B — 200₽\n"
        "3️⃣ Товар C — 300₽"
    )
    await message.answer(products_text)

async def on_startup(_):
    print("Бот запущен!")

def setup_webhook():
    app = web.Application()
    return app

if __name__ == "__main__":
    dp.run_polling(bot)
