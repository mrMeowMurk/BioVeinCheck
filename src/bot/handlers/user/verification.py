from aiogram              import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
import os

from ...utils             import logger, language
from ...messages          import ru, en
from ...states            import VerificationStates


async def verification_command(message: types.Message, state: FSMContext):
    """
        Обработчик команды /verification.
    """
    logger.info(f"Received verification command from {message.from_user.id}")
    
    lang = language.get_user_language(message.from_user)
    texts = en if lang == 'en' else ru
    
    await message.answer(texts.VERIFICATION_PHOTO_PROMPT)
    await state.set_state(VerificationStates.WAITING_FOR_PHOTO)

async def process_verification_photo(message: types.Message, state: FSMContext):
    """
    Обработка фотографии для верификации
    """
    lang = language.get_user_language(message.from_user)
    texts = en if lang == 'en' else ru
    
    if not message.photo:
        await message.answer(texts.VERIFICATION_NO_PHOTO)
        return
    
    # Создаем временную папку
    temp_dir = os.path.join("data", "temp")
    os.makedirs(temp_dir, exist_ok=True)
    
    try:
        # Сохраняем фото
        photo = message.photo[-1]
        photo_file = await message.bot.get_file(photo.file_id)
        photo_path = os.path.join(temp_dir, f"verify_{photo_file.file_id}.jpg")
        await message.bot.download_file(photo_file.file_path, photo_path)
        
        # Идентифицируем пользователя
        identified_id = message.bot.emb_manager.identify_user(photo_path)
        
        if identified_id is not None:
            user = next((u for u in message.bot.user_manager.users if u['id'] == identified_id), None)
            if user:
                await message.answer(texts.VERIFICATION_SUCCESS.format(name=user['name']))
            else:
                await message.answer(texts.VERIFICATION_USER_NOT_FOUND)
        else:
            await message.answer(texts.VERIFICATION_FAILED)
    
    except Exception as e:
        logger.error(f"Verification error: {e}")
        await message.answer(texts.VERIFICATION_ERROR)
    
    finally:
        # Удаляем временный файл
        if os.path.exists(photo_path):
            try:
                os.remove(photo_path)
                logger.info(f"Deleted temporary verification file: {photo_path}")
            except Exception as e:
                logger.error(f"Error deleting temporary file {photo_path}: {e}")
    
    await state.clear()
