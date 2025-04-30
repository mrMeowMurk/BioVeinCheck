"""
    ╔════════════════════════════════════════════════════════════╗
    ║                Модуль handlers/handler_help.py             ║
    ╚════════════════════════════════════════════════════════════╝

    Описание:
        Модуль содержит обработчик команды /help, который предоставляет
        пользователям справочную информацию о возможностях бота и доступных
        командах. Включает структурированное меню помощи с категориями команд.
"""


from aiogram     import types
from ...utils       import logger, language
from ...messages import ru, en


async def help_handler(message: types.Message):
    """
        Обработчик команды /help.
    """

    # Логируем получение команды /help от пользователя
    logger.info(f"Received help command from {message.from_user.id}")

    lang = language.get_user_language(message.from_user)
    texts = en if lang == 'en' else ru
    
    await message.answer(texts.HELP_TEXT)