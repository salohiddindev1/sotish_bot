import logging
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from database import ADMINS, delete_product, get_my_product, insert_product, get_my_products, update_product_description, update_product_image
from database import insert_user, get_user
from default import phone, menu,product_info
from inline import done_or_cancel,delete_or_edit
from state import MyProductState, RegisterState, AddProductState

logging.basicConfig(level=logging.INFO)

API_TOKEN = "7632611002:AAFHlmp_5TqHMNe8UGVLRXcYLuMzJlTuX3o"

bot = Bot(token=API_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
PROXY_URL = "http://proxy.server:3128"


async def on_startup(dp):
	for admin_chat_id in ADMINS:
		await bot.send_message(chat_id=admin_chat_id, text="Bot has been started")


async def on_shutdown(dp):
	for admin_chat_id in ADMINS:
		await bot.send_message(chat_id=admin_chat_id, text="Bot has been stopped")


@dp.message_handler(commands="start", state="*")
async def start_handler(message: types.Message, state: FSMContext):
	await state.finish()
	chat_id = message.chat.id
	user = get_user(chat_id=chat_id)
	if user:
		await message.answer("Welcome <b>SHOP BOT</b>", reply_markup=menu)
	else:
		await state.update_data(chat_id=chat_id)
		await message.answer("Send your fullname")
		await RegisterState.fullname.set()


@dp.message_handler(text="My Products📝")
async def my_products_handler(message: types.Message, state: FSMContext):
	chat_id = message.chat.id
	products = get_my_products(chat_id=chat_id)
	result = ""
	if products:
		for product in products:
			result += f"name: {product[1]} ID: {product[0]}\n"
	else:
		await message.answer("Product not found")
	await message.answer(result)
	await message.answer("Send your product ID")
	await MyProductState.id.set()

@dp.message_handler(state=MyProductState.id)
async def my_product_id_handler(message: types.Message, state: FSMContext):
	product_id = message.text
	chat_id = message.chat.id
	product = get_my_product(chat_id=chat_id,product_id=product_id)
	if product:
		await message.answer_photo(photo=product[3], caption=f'''ID:{product[0]}\nName: {product[1]}\nPrice: {product[4]}\nDescription: {product[2]}''',
                             reply_markup=delete_or_edit)
	else:
		await message.answer("Product not found")
	await state.finish()

 
@dp.message_handler(state=MyProductState.edit)
async def edit_handler(message: types.Message, state: FSMContext):
    if message.text.lower() == "name":
        await message.answer("Send new product name:")
        await MyProductState.name.set()
    elif message.text.lower() == "price":
        await message.answer("Send new product price:")
        await MyProductState.price.set()
    elif message.text.lower() == "description":
        await message.answer("Send new product description:")
        await MyProductState.description.set()
    elif message.text.lower() == "image":
        await message.answer("Send new product image (png, jpg):")
        await MyProductState.image.set()
    else:
        await message.answer("Invalid choice, please choose from: Name, Price, Description, or Image.")

@dp.message_handler(content_types="photo", state=MyProductState.image)
async def edit_image_handler(message: types.Message, state: FSMContext):
    new_image = message.photo[-1].file_id
    data = await state.get_data()
    product_id = data.get("product_id")
    success = update_product_image(product_id, new_image)
    if success:
        await message.answer("Product image updated.")
    else:
        await message.answer("Error in updating image.")
    await state.finish()
    
 
@dp.message_handler(state=MyProductState.description)
async def edit_description_handler(message: types.Message, state: FSMContext):
    new_description = message.text
    data = await state.get_data()
    product_id = data.get("product_id")
    success = update_product_description(product_id, new_description)
    if success:
        await message.answer(f"Product description updated.")
    else:
        await message.answer("Error in updating description.")
    await state.finish()
    
def update_product_name(product_id, new_name):
    query = "UPDATE products SET name = %s WHERE id = %s"
    pass


@dp.message_handler(text="Add Product➕")
async def add_product_handler(message: types.Message, state: FSMContext):
	await message.reply("Send your product name")
	await state.update_data(chat_id=message.chat.id)
	await AddProductState.name.set()


@dp.message_handler(state=AddProductState.name)
async def product_name_handler(message: types.Message, state: FSMContext):
	name = message.text
	await state.update_data(name=name)
	await message.answer("Send your product price")
	await AddProductState.price.set()


@dp.message_handler(state=AddProductState.price)
async def price_handler(message: types.Message, state: FSMContext):
	try:
		price = float(message.text)
		await state.update_data(price=price)
		await message.answer("Send your product description!!")
		await AddProductState.description.set()

	except:
		await message.reply("Price must be only number")


@dp.message_handler(state=AddProductState.description)
async def description_handler(message: types.Message, state: FSMContext):
	description = message.text
	await state.update_data(description=description)
	await message.answer('Send your product image(png,jpg)')
	await AddProductState.image.set()


@dp.message_handler(content_types="photo", state=AddProductState.image)
async def image_handler(message: types.Message, state: FSMContext):
	file_id = message.photo[-1].file_id
	await state.update_data(file_id=file_id)
	data = await state.get_data()
	await message.answer_photo(photo=file_id,
	                           caption=f'''Product name:{data.get('name')}
Product price:{data.get('price')}
Product description:{data.get('description')} ''', reply_markup=done_or_cancel)


@dp.callback_query_handler(text="done", state="*")
async def add_shop_handler(call: types.CallbackQuery, state: FSMContext):
	data = await state.get_data()
	insert = insert_product(data=data)
	if insert:
		await call.message.answer("Successfully added")
	else:
		await call.message.answer("Error in adding")
	await call.answer()
	await state.finish()


@dp.callback_query_handler(text="cancel", state="*")
async def cancel_handler(call: types.CallbackQuery, state: FSMContext):
	await call.message.delete()
	await call.answer()
	await state.finish()


@dp.message_handler(state=RegisterState.fullname)
async def fullname_handler(message: types.Message, state: FSMContext):
	fullname = message.text
	await state.update_data(fullname=fullname)
	await message.answer("Share Contact", reply_markup=phone)
	await RegisterState.phone_number.set()


@dp.message_handler(content_types="contact", state=RegisterState.phone_number)
async def phone_number_handler(message: types.Message, state: FSMContext):
	phone_number = message.contact.phone_number
	await state.update_data(phone_number=phone_number)
	data = await state.get_data()
	is_insert = insert_user(data=data)
	if is_insert:
		await message.answer("Successfully register", reply_markup=menu)
	else:
		await message.answer("Error in register")
	await state.finish()


if __name__ == "__main__":
	executor.start_polling(dispatcher=dp, skip_updates=True, on_shutdown=on_shutdown, on_startup=on_startup)
