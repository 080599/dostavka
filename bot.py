import telebot
import buttons as bt
import database as db

bot = telebot.TeleBot(token='7483772913:AAHS6IIH-tO_ofQumFV72UYCjL_7PCblvMM')


# db.add_products(pr_name="Burger", pr_des='best',pr_photo='https://amiel.club/uploads/posts/2022-03/1647563503_2-amiel-club-p-kartinki-burgerov-2.jpg', price=50000, pr_quantity=15)
# db.add_products(pr_name="CheeseBurger", pr_des='bestofthebest' ,pr_photo='https://i.pinimg.com/originals/f9/dd/78/f9dd78f4fd9b262b85b03731762dc947.jpg', price=52000, pr_quantity=15)
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    cheker = db.chek_user(user_id)
    print(cheker)
    bot.send_message(user_id, text="hi this bot for deliver food")

    if cheker is True:
        bot.send_message(user_id, 'choose', reply_markup=bt.main_menu_kb())
    elif cheker is False:
        bot.send_message(user_id, 'Hi this deliver bot.\n'
                                  'Please send ur name')


        bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_id = message.from_user.id
    name = message.text
    bot.send_message(user_id, text='send ur number', reply_markup=bt.phone_number_bt())
    bot.register_next_step_handler(message, get_number, name)
    print(name)


def get_number(message, name):
    user_id = message.from_user.id
    if message.contact:
        number = message.contact.phone_number
        print(name, number)
        bot.send_message(user_id, 'send ur location', reply_markup=bt.location_bt())
        bot.register_next_step_handler(message, get_location, name, number)
    else:
        bot.send_message(user_id, 'send ur number by button', reply_markup=bt.phone_number_bt())
        bot.register_next_step_handler(message, get_number, name)


def get_location(message, name, number):
    user_id = message.from_user.id
    if message.location:
        location = message.location
        bot.send_message(user_id, f'u sucsseful registered.ur data:\n'
                                  f'name:{name}\n'
                                  f'number:{number}\n'
                                  f'location:{location}')
        db.add_users(user_id, name, number)
        start(message)
    else:
        bot.send_message(user_id, 'send ur location', reply_markup=bt.location_bt())
        bot.register_next_step_handler(message, get_location, name, number)
@bot.callback_query_handler(lambda call: call.data in ['main_menu'])
def all_calls(call):
    user_id=call.message.chat.id
    if call.data=='main_menu':
        bot.delete_message(user_id,call.message.message_id)
        bot.send_message(user_id, 'Choose the action', reply_markup=bt.main_menu_kb())
@bot.callback_query_handler(lambda call: 'prod_' in call.data)
def product_call(call):
    user_id=call.message.chat.id
    bot.delete_message(user_id, call.message.message_id)
    product_id=int(call.data.replace('prod_',''))
    product_info=db.get_exact_products(product_id)
    bot.send_photo(user_id, photo=product_info[3], caption=f'{product_info[0]}\n\n'
                                                            f'Discription:{product_info[2]}\n'
                                                            f'Price:{product_info[1]}')
@bot.message_handler(content_types=['text'])
def main_menu(message):
    user_id = message.from_user.id
    text = message.text
    if text == 'Menu':
        all_products = db.get_pr_id_name()
        bot.send_message(user_id, 'Chose the product', reply_markup=bt.products_in(all_products))
    elif text == 'Cart':
        bot.send_message(user_id, 'Your cart')
    elif text == 'Comment':
        bot.send_message(user_id, 'Send your comment')


bot.infinity_polling()
