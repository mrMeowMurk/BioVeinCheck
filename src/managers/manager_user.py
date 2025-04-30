# user_manager.py
import os
import json
import shutil
from datetime import datetime


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

DATA_DIR     = os.path.join(PROJECT_ROOT, "data")
DB_DIR       = os.path.join(DATA_DIR, "database")
USERS_FILE   = os.path.join(DB_DIR, "users.json")
USERS_FOLDER = os.path.join(DB_DIR, "users")

class UserManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(UserManager, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized: return
        self.__initialized = True
        os.makedirs(USERS_FOLDER, exist_ok=True)
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(USERS_FILE):
            return []
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_users(self):
        os.makedirs(DB_DIR, exist_ok=True)
        with open(USERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.users, f, ensure_ascii=False, indent=4)

    def add_user(self, name, image_paths):
        new_id = max((u['id'] for u in self.users), default=0) + 1
        folder = os.path.join(USERS_FOLDER, str(new_id))
        os.makedirs(folder, exist_ok=True)

        stored = []
        idx = 1
        for src in image_paths:
            if not os.path.isfile(src): continue
            ext = os.path.splitext(src)[1]
            dst = os.path.join(folder, f"{idx}{ext}")
            shutil.copy(src, dst)
            stored.append(f"{new_id}/{idx}{ext}")
            idx += 1

        self.users.append({
            'id': new_id,
            'name': name,
            'registered_at': datetime.now().isoformat(),
            'images': stored
        })
        self.save_users()
        print(f"[UserManager] Added user {name} (ID={new_id})")

    def add_images(self, user_id, image_paths):
        user = next((u for u in self.users if u['id']==user_id), None)
        if not user:
            print(f"[UserManager] User ID={user_id} not found.")
            return
        folder = os.path.join(USERS_FOLDER, str(user_id))
        os.makedirs(folder, exist_ok=True)
        existing = {int(os.path.splitext(f)[0])
                    for f in os.listdir(folder)
                    if f.split('.')[0].isdigit()}
        idx = max(existing, default=0) + 1
        for src in image_paths:
            if not os.path.isfile(src): continue
            ext = os.path.splitext(src)[1]
            dst = os.path.join(folder, f"{idx}{ext}")
            shutil.copy(src, dst)
            user['images'].append(f"{user_id}/{idx}{ext}")
            print(f"[UserManager] Added image for user {user_id}: {idx}{ext}")
            idx += 1
        self.save_users()

    def delete_user(self, user_id):
        user = next((u for u in self.users if u['id']==user_id), None)
        if not user:
            print(f"[UserManager] User ID={user_id} not found.")
            return
        folder = os.path.join(USERS_FOLDER, str(user_id))
        if os.path.isdir(folder):
            shutil.rmtree(folder)
        self.users = [u for u in self.users if u['id']!=user_id]
        self.save_users()
        print(f"[UserManager] Deleted user ID={user_id}")
