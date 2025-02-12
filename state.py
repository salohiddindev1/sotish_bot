from aiogram.dispatcher.filters.state import State,StatesGroup


class RegisterState(StatesGroup):
    fullname = State()
    phone_number = State()
    
class AddProductState(StatesGroup):
    name = State()
    price = State()
    description = State()
    image = State()
    done_or_cancel = State()

class MyProductState(StatesGroup):
    id = State()
    edit = State()
    name = State()
    price = State()
    description = State()
    image = State()
    

    
