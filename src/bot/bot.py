"""
    ╔════════════════════════════════════════════╗
    ║                main.py                     ║
    ╚════════════════════════════════════════════╝
    
    Описание:
        Основной модуль приложения, отвечающий за:
        • Инициализацию всех необходимых компонентов системы
        • Настройку и конфигурацию телеграм-бота
        • Управление жизненным циклом бота
        
    Зависимости:
        • aiogram    - библиотека для создания телеграм-ботов
        • asyncio    - библиотека для асинхронной работы
"""



import asyncio

from aiogram                    import Bot, Dispatcher
from aiogram.enums              import ParseMode
from aiogram.client.default     import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from .handlers                   import register_handlers
from .utils                      import logger
from ..config                    import config
from ..managers                  import EmbeddingManager, UserManager



async def run_bot():
    """
        Основная функция инициализации и запуска бота
    """
    
    # Инициализация менеджеров
    user_manager = UserManager()
    emb_manager = EmbeddingManager()
    
    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        )
    )
    
    # Привязка менеджеров к боту
    bot.user_manager = user_manager
    bot.emb_manager = emb_manager
    
    dp = Dispatcher(storage=MemoryStorage())
    register_handlers(dp)

    try:
        logger.info("Starting polling")
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except asyncio.CancelledError:
        logger.info("Polling was cancelled")
    finally:
        await bot.close()
        logger.info("Bot session closed")
