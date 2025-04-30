"""
    ╔════════════════════════════════════════════╗
    ║              utils_language.py             ║
    ╚════════════════════════════════════════════╝
    
    Модуль для работы с языковыми настройками пользователя
    
    Классы:
        • LanguageManager - Менеджер для работы с языковыми настройками
"""

from typing import List
from aiogram import types

class LanguageManager:
    """
        Класс для управления языковыми настройками пользователей
        
        Атрибуты:
            SUPPORTED_LANGUAGES: Список поддерживаемых языков
            
        Методы:
            get_user_language: Определяет язык пользователя
            set_user_language: Устанавливает язык для пользователя
            get_available_languages: Возвращает список доступных языков
    """
    
    SUPPORTED_LANGUAGES = ['ru', 'en']
    
    @classmethod
    def get_user_language(cls, user: types.User) -> str:
        """
            Определяет язык пользователя
            
            Аргументы:
                user: Объект пользователя Telegram
                
            Возвращает:
                Код языка (например, 'ru' или 'en')
        """
        # Сначала проверяем язык, установленный пользователем
        if hasattr(user, 'language_code') and user.language_code in cls.SUPPORTED_LANGUAGES:
            return user.language_code
        
        # Если язык не поддерживается, возвращаем язык по умолчанию
        return 'ru'
    
    @classmethod
    def set_user_language(cls, user_id: int, language: str) -> bool:
        """
            Устанавливает язык для пользователя
            
            Аргументы:
                user_id: ID пользователя
                language: Код языка (например, 'ru' или 'en')
                
            Возвращает:
                True, если язык успешно установлен, иначе False
        """
        if language not in cls.SUPPORTED_LANGUAGES:
            return False
        
        # Здесь можно добавить логику сохранения языка в БД
        # Например: save_language_to_db(user_id, language)
        return True
    
    @classmethod
    def get_available_languages(cls) -> List[str]:
        """
            Возвращает список доступных языков
            
            Возвращает:
                Список кодов поддерживаемых языков
        """
        return cls.SUPPORTED_LANGUAGES 
    
language = LanguageManager()
