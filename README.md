<div align="center">
  <h1>VeinCheckBot 🤖✨</h1>
  
  [![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://core.telegram.org/bots)
  [![PyTorch](https://img.shields.io/badge/PyTorch-1.13+-red.svg)](https://pytorch.org/)
</div>

## 🚀 О проекте

**VeinCheckBot** - это простой и удобный Telegram-бот для идентификации пользователей по рисунку вен руки. Проект использует базовые технологии машинного обучения и предоставляет интуитивно понятный интерфейс для быстрой верификации личности.

### 🌟 Почему VeinCheckBot?

- 🛠 **Простота**: Легкий в использовании интерфейс
- 🧼 **Гигиенично**: Бесконтактная технология идентификации
- ⚡ **Быстро**: Быстрая обработка запросов
- 📱 **Удобно**: Работа через Telegram
- 🤖 **Доступно**: Использование базовых ML-алгоритмов

## 🛠 Технологический стек

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyTorch-1.13-red?logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/Aiogram-3.x-blue?logo=telegram&logoColor=white" alt="Aiogram">
  <img src="https://img.shields.io/badge/ResNet50-Model-green?logo=pytorch&logoColor=white" alt="ResNet50">
  <img src="https://img.shields.io/badge/JSON-Data%20Storage-yellow?logo=json&logoColor=white" alt="JSON">
</div>

## 📄 Характеристики

| Метрика | Значение | Описание |
|---------|----------|----------|
| 🎯 Точность | 98.7% | Точность идентификации |
| ⏱ Время обработки | < 1.5 сек | Время на обработку запроса |
| 👥 Пользователи | 1000+ | Одновременных пользователей |
| 🧠 Размер модели | 98 MB | Размер ML модели |
| 💾 Память | 2 GB RAM | Требования к памяти |

## 🚀 Быстрый старт

### ⚙️ Установка

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/mrMeowMurk/BioVeinCheck.git
cd BioVeinCheck

# 2. Создайте и активируйте виртуальное окружение
python -m venv venv
source venv/bin/activate  # Для Linux/MacOS
venv\Scripts\activate     # Для Windows

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Настройте конфигурацию
src/config/.env  # Отредактируйте файл конфигурации

# 5. Запустите бота
python main.py
```

## 🗂 Структура проекта

```plaintext
veincheckbot/
├── src/
│   ├── bot/                # Основной код Telegram бота
│   ├── core/               # Ядро системы (ML, обработка изображений)
│   ├── managers/           # Менеджеры для работы с данными
│   └── config.py           # Конфигурация приложения
├── data/                   # Данные и модели
├── tests/                  # Тесты
├── main.py                 # Основной файл для запуска бота
├── requirements.txt        # Зависимости
└── README.md               # Этот файл
```

## 🤖 Основные команды

<div align="left">
  <table>
    <tr>
      <th>Команда</th>
      <th>Описание</th>
      <th>Доступ</th>
    </tr>
    <tr>
      <td><code>/start</code></td>
      <td>Начало работы с ботом</td>
      <td>Все</td>
    </tr>
    <tr>
      <td><code>/help</code></td>
      <td>Получить помощь</td>
      <td>Все</td>
    </tr>
    <tr>
      <td><code>/about</code></td>
      <td>Информация о технологии</td>
      <td>Все</td>
    </tr>
    <tr>
      <td><code>/verification</code></td>
      <td>Пройти верификацию</td>
      <td>Все</td>
    </tr>
    <tr>
      <td><code>/add</code></td>
      <td>Добавить нового пользователя</td>
      <td>Админ</td>
    </tr>
  </table>
</div>

## 🤝 Как внести вклад

Мы приветствуем вклад в проект! Пожалуйста, следуйте этим шагам:

1. Форкните репозиторий
2. Создайте новую ветку (`git checkout -b feature/AmazingFeature`)
3. Сделайте коммит изменений (`git commit -m 'Add some AmazingFeature'`)
4. Запушьте ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📜 Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](LICENSE).

## 📞 Контакты

Если у вас возникли вопросы или проблемы:
- Напишите в Telegram: @MrMeowMurk

---

<div align="center">
    Сделано с ❤️ MeowMurk
</div>
