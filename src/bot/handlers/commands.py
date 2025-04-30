
"""
     ╔════════════════════════════════════════════════════════════╗
     ║                     ИМПОРТЫ МОДУЛЕЙ                        ║
     ╚════════════════════════════════════════════════════════════╝
"""

# Базовые импорты Aiogram
from aiogram         import Dispatcher
from aiogram.filters import Command
from aiogram         import F

# Обработчики команд общего доступа
from .common.start import start_handler
from .common.help  import help_handler
from .common.about import about_handler

# Обработчики команд пользователя   
from .user.verification import verification_handler

"""
    ╔════════════════════════════════════════════════════════════╗
    ║                РЕГИСТРАЦИИ ХЕНДЛЕРОВ                       ║
    ║                           И                                ║
    ║                 CALLBACK-ОБРАБОТЧИКОВ                      ║
    ╚════════════════════════════════════════════════════════════╝
"""


"""
    Регистрирует все обработчики команд и callback-запросов для бота
"""
def register_handlers(dp: Dispatcher):


    # Команды общего доступа
    dp.message.register(start_handler,    Command(commands=["start"]))
    dp.message.register(help_handler,     Command(commands=["help"]))
    dp.message.register(about_handler,    Command(commands=["about"]))

    # Команды пользователя
    dp.message.register(verification_handler, Command(commands=["verification"]))

