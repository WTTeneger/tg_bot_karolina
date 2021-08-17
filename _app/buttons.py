from _app import *
inline_button = types.InlineKeyboardMarkup()  # наша клавиатура
otv1 = types.InlineKeyboardButton(
    text="Страница в клетку", callback_data=f"Select_list_type_work_1")
otv2 = types.InlineKeyboardButton(
    text="Страница в линию", callback_data=f"Select_list_type_work_2")

inline_button.row(otv1, otv2)  # добавляем кнопку в клавиатуру

menu_button = types.ReplyKeyboardMarkup(
    row_width=2, resize_keyboard=True)  # наша клавиатура
button0 = types.KeyboardButton(text='▶️Начать◀️')
button1 = types.KeyboardButton(text='Вот так')
menu_button.row(button0)
menu_button.row(button1)