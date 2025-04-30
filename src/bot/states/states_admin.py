
from aiogram.fsm.state import State, StatesGroup

class AdminStates(StatesGroup):
    WAITING_FOR_NAME   = State()
    WAITING_FOR_PHOTOS = State()