from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import FSInputFile
import os

from ...utils import logger, language
from ...messages import ru, en
from ...states import AdminStates


async def add_user_command(message: types.Message, state: FSMContext):
    """
    Обработчик команды /add
    """
    logger.info(f"Received add command from {message.from_user.id}")
    
    lang = language.get_user_language(message.from_user)
    texts = en if lang == 'en' else ru
    
    await message.answer(texts.ADD_USER_NAME_PROMPT)
    await state.set_state(AdminStates.WAITING_FOR_NAME)

async def process_user_name(message: types.Message, state: FSMContext):
    """
    Обработка имени пользователя
    """
    lang = language.get_user_language(message.from_user)
    texts = en if lang == 'en' else ru
    
    await state.update_data(user_name=message.text)
    await message.answer(texts.ADD_USER_PHOTOS_PROMPT)
    await state.set_state(AdminStates.WAITING_FOR_PHOTOS)

async def process_user_photos(message: types.Message, state: FSMContext):
    """
    Обработка фотографий пользователя
    """
    lang = language.get_user_language(message.from_user)
    texts = en if lang == 'en' else ru
    
    if not message.photo:
        await message.answer(texts.ADD_USER_NO_PHOTOS)
        return
    
    # Получаем данные из состояния
    data = await state.get_data()
    user_name = data.get('user_name')
    
    # Создаем папку data/temp, если она не существует
    temp_dir = os.path.join("data", "temp")
    os.makedirs(temp_dir, exist_ok=True)
    
    # Сохраняем фотографии
    photo_paths = []
    
    try:
        # Берем только самую качественную версию фотографии (последнюю в массиве)
        photo = message.photo[-1]
        photo_file = await message.bot.get_file(photo.file_id)
        photo_path = os.path.join(temp_dir, f"{photo_file.file_id}.jpg")
        await message.bot.download_file(photo_file.file_path, photo_path)
        photo_paths.append(photo_path)
        
        # Добавляем пользователя
        message.bot.user_manager.add_user(user_name, photo_paths)
        message.bot.emb_manager.update_embeddings()
        
        await message.answer(texts.ADD_USER_SUCCESS.format(name=user_name))
    finally:
        # Удаляем временные файлы
        for photo_path in photo_paths:
            try:
                if os.path.exists(photo_path):
                    os.remove(photo_path)
                    logger.info(f"Deleted temporary file: {photo_path}")
            except Exception as e:
                logger.error(f"Error deleting temporary file {photo_path}: {e}")
    
    await state.clear()

