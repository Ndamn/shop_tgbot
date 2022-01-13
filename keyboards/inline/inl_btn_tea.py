from utils.settings_buttons import ListOfButtons


tea_menu = ListOfButtons(text=['Назад', 'В начало', 'Вперёд', 'Купить', 'В избранное'],
callback=['back', 'first_menu', 'go', 'buy', 'in_favorite'],
align=[3, 2]).inline_keyboard