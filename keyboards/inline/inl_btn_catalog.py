from utils.settings_buttons import ListOfButtons


catalog_inl_btn = ListOfButtons(text=['Наборы', 'Специи', 'Чаи', 'Прочее'],
callback=['sets', 'seasoning', 'tea', 'other'],
align=[2, 2]).inline_keyboard