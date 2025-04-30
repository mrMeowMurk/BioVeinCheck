import os
import glob
import pickle
import numpy as np
from PIL import Image
import torch
import torchvision.models as models
import torchvision.transforms as transforms
import argparse

from torchvision.models import ResNet50_Weights

# Определим корень проекта как два уровня выше текущего файла (т.е. из src/core/ -> в корень проекта)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Пути к папкам и файлам
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DATABASE_DIR = os.path.join(DATA_DIR, "database")

EMB_DIR = os.path.join(DATA_DIR, "embeddings")
EMB_PATH = os.path.join(EMB_DIR, "embeddings.pkl")

MODEL_DIR = os.path.join(DATA_DIR, "model")
MODEL_PATH = os.path.join(MODEL_DIR, "resnet50.pth")


# Создаём необходимые директории, если их нет
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(DATABASE_DIR, exist_ok=True)
os.makedirs(EMB_DIR, exist_ok=True)

# Загрузка или сохранение модели
if not os.path.exists(MODEL_PATH):
    # Скачиваем предобученную ResNet50 и сохраняем веса
    model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
    torch.save(model.state_dict(), MODEL_PATH)  # сохраняем state_dict&#8203;:contentReference[oaicite:5]{index=5}
else:
    # Инициализируем модель и загружаем ранее сохранённые веса
    model = models.resnet50(weights=None)
    model.load_state_dict(torch.load(MODEL_PATH))
# Готовим модель к инференсу и удаляем последний слой
model.eval()
model.fc = torch.nn.Identity()

# Описание преобразований для входного изображения
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225])
])

# Загружаем существующую базу эмбеддингов или создаём пустую
if os.path.exists(EMB_PATH):
    with open(EMB_PATH, "rb") as f:
        embedding_db = pickle.load(f)
else:
    embedding_db = []  # список записей: {'path': ..., 'label': ..., 'vector': np.array}

# Проходим по всем изображениям в базе
for root, dirs, files in os.walk(DATABASE_DIR):
    for fname in files:
        if not fname.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        filepath = os.path.join(root, fname)
        rel_path = os.path.relpath(filepath, DATABASE_DIR)
        user_label = os.path.basename(root)  # предполагаем, что имя папки = пользователь
        # Проверяем, был ли этот файл уже обработан
        if any(entry['path'] == rel_path for entry in embedding_db):
            continue  # пропускаем уже известные файлы
        # Вычисляем эмбеддинг нового изображения
        img = Image.open(filepath).convert('RGB')
        input_tensor = preprocess(img).unsqueeze(0)
        with torch.no_grad():
            vec = model(input_tensor).squeeze().numpy()
        embedding_db.append({'path': rel_path, 'label': user_label, 'vector': vec})

# Сохраняем обновлённую базу эмбеддингов
with open(EMB_PATH, "wb") as f:
    pickle.dump(embedding_db, f)

# Разбор аргументов командной строки для входного изображения
parser = argparse.ArgumentParser(description="Распознавание пользователя по вено-образу ладони")
parser.add_argument("input_image", type=str, help="путь к входному изображению ладони")
args = parser.parse_args()

# Вычисляем эмбеддинг для входного изображения
inp_img = Image.open(args.input_image).convert('RGB')
inp_tensor = preprocess(inp_img).unsqueeze(0)
with torch.no_grad():
    inp_vec = model(inp_tensor).squeeze().numpy()

# Сравниваем с базой: находим минимальное евклидово расстояние
min_dist = float('inf')
closest_label = None
for entry in embedding_db:
    dist = np.linalg.norm(inp_vec - entry['vector'])
    if dist < min_dist:
        min_dist = dist
        closest_label = entry['label']

# Вывод результата
print(f"Найден пользователь: {closest_label} (расстояние {min_dist:.4f})")
