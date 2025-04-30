from aiogram              import types
from ...utils             import logger, language
from ...messages          import ru, en


async def verification_handler(message: types.Message):
    """
        Обработчик команды /verification.
    """
    logger.info(f"Received verification command from {message.from_user.id}")
    
    lang = language.get_user_language(message.from_user)
    texts = en if lang == 'en' else ru
    
    verification_text = texts.VERIFICATION_TEXT.format(username=message.from_user.username)
    await message.answer(verification_text)
