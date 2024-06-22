from telebot import types
def phone_number_bt():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button=types.KeyboardButton('contact',request_contact=True)
    kb.add(button)
    return kb
def location_bt():
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    button=types.KeyboardButton('send location', request_location=True)
    kb.add(button)
    return kb
def main_menu_kb():
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    products=types.KeyboardButton(text="Menu")
    cart=types.KeyboardButton(text="Cart")
    feedback=types.KeyboardButton(text="Coment")
    kb.add(products,cart,feedback)
    return kb
def products_in(all_products):
    kb=types.InlineKeyboardMarkup(row_width=2)
    #sozdanie postayannix knopok
    main_menu=types.InlineKeyboardButton(text='Main menu',callback_data='main_menu')
    cart=types.InlineKeyboardButton(text='cart',callback_data='cart')
    #sozdanie dinamichnix knopok
    all_buttons=[types.InlineKeyboardButton(text=product[1], callback_data=f"prod_{product[0]}") for product in all_products]
    kb.add(*all_buttons)
    kb.row(cart)
    kb.row(main_menu)
    return kb



