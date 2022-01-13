from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery

class Button(BoundFilter):
    def __init__(self, key, constains=False):
        self.key = key
        self.constains = constains

    async def check(self, message) -> bool:
        if isinstance(message, Message):
            if self.constains:
                return self.key in message.text
            else:
                return message.text == self.key
        elif isinstance(message, CallbackQuery):
            if self.constains:
                return self.key in message.data
            else:
                return self.key == message.data