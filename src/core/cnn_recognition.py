import sys
import os
import argparse

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.managers.manager_user import UserManager
from src.managers.manager_emb import EmbeddingManager

def main():
    # Инициализируем менеджеры
    user_manager = UserManager()
    emb_manager = EmbeddingManager()

    # Обновляем базу эмбеддингов (учет новых/удаленных изображений)
    emb_manager.update_embeddings()

    # # Пример: добавить нового пользователя с изображениями
    # user_manager.add_user("Шестой Шестой", ["input.jpg"])
    # emb_manager.update_embeddings()  # пересчитаем эмбеддинги после добавления

    # Пример: идентификация по новому изображению
    new_image = "input.jpg"
    identified_id = emb_manager.identify_user(new_image)
    if identified_id is not None:
        user = next((u for u in user_manager.users if u['id'] == identified_id), None)
        if user:
            print(f"Изображение соответствует пользователю {user['name']} (ID={identified_id})")
        else:
            print("Пользователь не найден.")

if __name__ == "__main__":
    main()
