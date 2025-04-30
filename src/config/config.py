"""
    ╔════════════════════════════════════════════╗
    ║                config.py                   ║
    ╚════════════════════════════════════════════╝
    
    Описание:
    ---------
    Центральный модуль конфигурации, содержащий:
    • Основные настройки Telegram-бота
    
    Конфигурации:
    -------------
    • Бот:
      - BOT_TOKEN  - токен для API Telegram
"""



import os
from pathlib     import Path
from dotenv      import load_dotenv
from typing      import List
from dataclasses import dataclass


# Загрузка переменных окружения
load_dotenv()


@dataclass
class BotConfig:
    """
        Конфигурация бота
    """
    token: str

    @classmethod
    def from_env(cls) -> 'BotConfig':
        return cls(
            token = os.getenv("BOT_TOKEN"),
        )

class Config:
    """
        Основной класс конфигурации
    """
    def __init__(self):
        self.bot      = BotConfig.from_env()
        
    def validate(self) -> bool:
        """
            Проверка валидности конфигурации
        """
        if not self.bot.token:
            raise ValueError("BOT_TOKEN not installed")
        return True


config = Config()
config.validate()
