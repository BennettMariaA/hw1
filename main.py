from aiogram import Bot, Dispatcher, types
from decouple import config

API_TOKEN = config("API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['meme'])
async def meme(message: types.Message):
    photo = open('media/meoww.jpg', 'rb')
    await message.answer_photo(photo=photo)

@dp.message_handler()
async def echo_messages(message: types.Message):
    try:
        number = float(message.text)
        squared = number ** 2
        await message.reply(str(squared))
    except ValueError:
        await message.reply(message.text)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)

