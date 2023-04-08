import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from aggregation import Aggregator, read, check_curent_fields
from constants import correct_format
from dotenv import load_dotenv

load_dotenv()


token = os.getenv('API_TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start_and_greet(message: types.Message):
    if message.from_user.first_name:
        name = message.from_user.first_name
    else:
        name = ''

    await message.reply(
        (
        f'Привет! {name}\nЯ дикий бот который считает деньги своих коллег.\n'
        'Мне бугалтер, слила все зароботки сотрудников, и я готов тебе '
        'рассказать, сколько им нужно работать на пирожок в McDonalds.\n'
        f'{correct_format}'
        )
    )

@dp.message_handler()
async def reciver(message: types.Message):
    try:
        if check_curent_fields(read(message.text)) is False:
            await message.answer(f'Невалидный запос. {correct_format}')
        else:
            aggregator = Aggregator(**read(message.text))
            await message.answer(aggregator.get_result())
    except ValueError:
        await message.answer(f'Невалидный запос. {correct_format}')
    except SyntaxError:
        await message.answer(f'Невалидный запос. {correct_format}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)