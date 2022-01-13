from aiogram import types
from loader import dp 
from keyboards.inline.inl_btn_catalog import catalog_inl_btn
from keyboards.inline.inl_btn_tea import tea_menu
from filters.buttons_filter import Button


@dp.message_handler(text='Каталог')
async def bot_start(message: types.Message):
    await message.answer(f"Каталог, {message.from_user.full_name}!", reply_markup=catalog_inl_btn)

@dp.callback_query_handler(Button('tea'))
async def inline_menu(call: types.CallbackQuery):
    await call.message.answer(f"Вот ассортимент:", reply_markup=tea_menu)
    await call.message.edit_reply_murkup()

