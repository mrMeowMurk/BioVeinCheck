from aiogram              import types
from ...utils             import logger, language
from ...messages          import ru, en


async def start_handler(message: types.Message):
    """
        Обработчик команды /start.
    """
    logger.info(f"Received start command from {message.from_user.id}")
    
    # Используем LanguageManager для определения языка
    lang = language.get_user_language(message.from_user)
    texts = en if lang == 'en' else ru
    
    start_text = texts.START_TEXT.format(username=message.from_user.username)
    await message.answer(start_text)
