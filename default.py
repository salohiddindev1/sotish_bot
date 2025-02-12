from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Share Contact",request_contact=True)
        ],
    ],resize_keyboard=True,one_time_keyboard=True
)


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Shop🛍"),
            KeyboardButton(text="My Products📝"),
        ],
        [
            KeyboardButton(text="Add Product➕")
        ]
    ],resize_keyboard=True
)


product_info = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Name"),
            KeyboardButton(text="Price")
        ],
        [
            KeyboardButton(text="Description"),
            KeyboardButton(text="Image"),
        ],
        [
           KeyboardButton(text="Back🔙")
        ]
    ],resize_keyboard=True
)