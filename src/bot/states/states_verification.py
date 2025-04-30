from aiogram.fsm.state import State, StatesGroup

class VerificationStates(StatesGroup):
    WAITING_FOR_PHOTO = State()