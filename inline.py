from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

done_or_cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Add to shop✅",callback_data="done"),
            InlineKeyboardButton(text="Cancel❌",callback_data="cancel"),
        ]
    ]
)

delete_or_edit = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Delete❌",callback_data="delete"),
            InlineKeyboardButton(text="Edit✏️",callback_data="edit"),
        ]
    ],
)