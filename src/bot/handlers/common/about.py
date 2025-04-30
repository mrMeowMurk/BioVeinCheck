from aiogram import types
from ...utils import logger, language
from ...messages import ru, en


async def about_handler(message: types.Message):
    """
        Обработчик команды /about.
    """
    logger.info(f"Received about command from {message.from_user.id}")

    lang = language.get_user_language(message.from_user)
    texts = en if lang == 'en' else ru
    
    await message.answer(texts.ABOUT_TEXT)
