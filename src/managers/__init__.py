"""
    ╔════════════════════════════════════════════╗
    ║              __init__.py                   ║
    ╚════════════════════════════════════════════╝
    
    Инициализационный модуль пакета конфигурации
    
"""

from .manager_emb import EmbeddingManager
from .manager_user import UserManager

__all__ = ["EmbeddingManager", "UserManager"  ]