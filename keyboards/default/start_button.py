from utils.settings_buttons import ListOfButtons


start_btn = ListOfButtons(text=['Каталог', 'Корзина', 'Избранное', 'Помощь'], 
callback=['catalog', 'bucket', 'favorite', 'help'], 
align=[2, 1, 1]).reply_keyboard