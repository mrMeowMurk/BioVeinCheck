# embedding_manager.py
import os
import pickle
import numpy as np
from PIL import Image
import torch
from torchvision import models, transforms
from ..bot.utils import logger

from src.managers.manager_user import UserManager

# Корень проекта и папки
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_DIR     = os.path.join(PROJECT_ROOT, "data")
EMB_DIR      = os.path.join(DATA_DIR, "embeddings")
EMB_PATH     = os.path.join(EMB_DIR, "embeddings.pkl")

# Пути для модели
MODEL_DIR    = os.path.join(DATA_DIR, "model")
MODEL_PATH   = os.path.join(MODEL_DIR, "resnet50.pth")

from torchvision.models import ResNet50_Weights

class EmbeddingManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(EmbeddingManager, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized: return
        self.__initialized = True
        
        os.makedirs(EMB_DIR, exist_ok=True)
        os.makedirs(MODEL_DIR, exist_ok=True)
        self.user_mgr = UserManager()
        self.embeddings = self._load_embeddings()
        self._load_or_download_model()
        # Преобразования для ResNet50
        self.preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485,0.456,0.406],
                std=[0.229,0.224,0.225]
            )
        ])
        logger.info("EmbeddingManager initialized")

    def _load_embeddings(self):
        if os.path.exists(EMB_PATH):
            with open(EMB_PATH, 'rb') as f:
                embeddings = pickle.load(f)
                logger.debug(f"Loaded embeddings type: {type(embeddings)}")
                if isinstance(embeddings, dict):
                    return embeddings
                elif isinstance(embeddings, list):
                    return {str(k['path']): k['vector'] for k in embeddings}
                else:
                    logger.warning(f"Unknown embeddings format: {type(embeddings)}")
                    return {}
        logger.debug("No embeddings file found, creating new one")
        return {}

    def _save_embeddings(self):
        with open(EMB_PATH, 'wb') as f:
            # Сохраняем данные в формате, который можно загрузить
            pickle.dump(self.embeddings, f)

    def _load_or_download_model(self):
        # Загружаем или скачиваем ResNet50
        if not os.path.exists(MODEL_PATH):
            model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
            torch.save(model.state_dict(), MODEL_PATH)
        else:
            model = models.resnet50(weights=None)
            model.load_state_dict(torch.load(MODEL_PATH))
        model.fc = torch.nn.Identity()
        model.eval()
        
        self.model = model

    def _compute_emb(self, img_path):
        img = Image.open(img_path).convert('RGB')
        tensor = self.preprocess(img).unsqueeze(0)
        with torch.no_grad():
            emb = self.model(tensor).squeeze().cpu().numpy()
        return emb / np.linalg.norm(emb)

    def update_embeddings(self):
        # Синхронизируем: удаляем устаревшие
        valid_keys = set()
        for u in self.user_mgr.users:
            for rel in u['images']:
                # Убедимся, что rel - это строка
                if isinstance(rel, str):
                    valid_keys.add(rel)
                else:
                    print(f"Warning: Skipping unhashable key {rel} of type {type(rel)}")

        # Удаляем ненужные
        for k in list(self.embeddings):
            print(f"Checking key: {k}, type: {type(k)}")  # Отладочный вывод
            if k not in valid_keys:
                del self.embeddings[k]

        # Добавляем новые
        for u in self.user_mgr.users:
            uid = u['id']
            for rel in u['images']:
                if rel not in self.embeddings:
                    img_path = os.path.join(
                        PROJECT_ROOT, "data", "database", "users", rel)
                    if os.path.exists(img_path):
                        self.embeddings[rel] = self._compute_emb(img_path)
                        print(f"[EmbeddingManager] Compute emb for {rel}")
        self._save_embeddings()

    def identify_user(self, image_path):
        query = self._compute_emb(image_path)
        best, dist = None, float('inf')
        for rel, emb in self.embeddings.items():
            d = np.linalg.norm(query - emb)
            if d < dist:
                dist, best = d, rel
        return int(best.split('/')[0]) if best else None
