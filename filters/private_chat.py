# - *- coding: utf- 8 - *-
from aiogram.dispatcher.filters import BoundFilter
from data.config import admins
from aiogram import types


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        if str(message.from_user.id) in admins:
            return True
        else:
            return False
