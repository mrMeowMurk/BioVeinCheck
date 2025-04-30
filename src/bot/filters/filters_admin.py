
from aiogram import types
from config import config

async def filter_only_admin(message: types.Message) -> bool:
    """
        Фильтр: разрешает доступ только администраторам 
    """

    if not(message.from_user.id in config.users.admins):
        await message.answer("Данная команда доступна только администратору")

    return message.from_user.id in config.users.admins
