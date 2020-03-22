import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

stuff_to_delete = {'content_type': 'text', 'message_id': 1012, 'from_user': {'id': 1106164002, 'is_bot': True, 'first_name': 'Гимназия 63', 'username': 'Gimn63bot', 'last_name': None, 'language_code': None}, 'date': 1583780538, 'chat': {'type': 'private', 'last_name': 'Захаров', 'first_name': 'Глеб', 'username': 'Vorendon', 'id': 845488769, 'title': None, 'all_members_are_administrators': None, 'photo': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'sticker_set_name': None, 'can_set_sticker_set': None}, 'forward_from_chat': None, 'forward_from': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': 'Выбирете параллель:', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'json': {'message_id': 1012, 'from': {'id': 1106164002, 'is_bot': True, 'first_name': 'Гимназия 63', 'username': 'Gimn63bot'}, 'chat': {'id': 845488769, 'first_name': 'Глеб', 'last_name': 'Захаров', 'username': 'Vorendon', 'type': 'private'}, 'date': 1583780538, 'text': 'Выбирете параллель:', 'reply_markup': {'inline_keyboard': [[{'text': '1 параллель', 'callback_data': '1'}], [{'text': '2 параллель', 'callback_data': '2'}], [{'text': '3 параллель', 'callback_data': '3'}], [{'text': '4 параллель', 'callback_data': '4'}], [{'text': '5 параллель', 'callback_data': '5'}], [{'text': '6 параллель', 'callback_data': '6'}], [{'text': '7 параллель', 'callback_data': '7'}], [{'text': '8 параллель', 'callback_data': '8'}], [{'text': '9 параллель', 'callback_data': '9'}], [{'text': '10 параллель', 'callback_data': '10'}], [{'text': '11 параллель', 'callback_data': '11'}]]}}}

data = {}

day_of_the_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

try:
	@bot.message_handler(commands = ['start'])
	def start(message):
		user = message.from_user
		try:
			print(user.first_name + '\n' + user.last_name + '\n' + user.username + '\n' + str(user.id) + '\n')
		except Exception as e:
			print(repr(e))

		markup = types.ReplyKeyboardMarkup(resize_keyboard=1)
		item = types.KeyboardButton('Показать расписание')
		markup.add(item)

		yodo = open("C:/Users/gleb/AppData/Local/Programs/Python/Python38-32/MyScripts/TelegramBot/yodo.mp4", 'rb')
		bot.send_document(message.chat.id, yodo)

		bot.send_message(message.chat.id, "Да прибудет с тобой сила, " + user.first_name + "!", reply_markup = markup)

	@bot.message_handler(content_types = ['sticker'])
	def sticker(message):
		user = message.from_user
		bot.send_message(message.chat.id, 'Нинавижу стикеры >:')

	@bot.message_handler(content_types = ['voice'])
	def voice(message):
		bot.send_message(message.chat.id, 'Голосовые сообщения для неграмотных')

	@bot.message_handler(content_types = ['text'])
	def text(message):
		user = message.from_user
		if message.text == 'Показать расписание':
			global stuff_to_delete
			global also_delete
			global and_this_delete

			try:
				bot.delete_message(chat_id = stuff_to_delete.chat.id, message_id = stuff_to_delete.message_id)
			except Exception as e:
				print(repr(e))

			try:
				bot.delete_message(chat_id = also_delete.chat.id, message_id = also_delete.message_id)
			except Exception as e:
				print(repr(e))

			try:
				bot.delete_message(chat_id = and_this_delete.chat.id, message_id = and_this_delete.message_id)
			except Exception as e:
				print(repr(e))
			
			data[user.id] = [0, 0, 0]
			items = []
			markup = types.InlineKeyboardMarkup(row_width = 2)

			for p in range(1, 12):
				item = types.InlineKeyboardButton(str(p)+' параллель', callback_data = p)
				markup.add(item)

			stuff_to_delete = bot.send_message(message.chat.id, 'Выбирете параллель:', reply_markup = markup)

		elif message.text == 'Вывести данные':
			print(data)

		elif message.text.lower() == 'reboot':
			raise

		else:
			bot.send_message(message.chat.id, 'Пока я не принимаю текстовые сообщения')

	def choose_parallel(call):
		user = call.from_user
		markup = types.InlineKeyboardMarkup(row_width = 2)

		item1 = types.InlineKeyboardButton('А', callback_data = 'А')
		item2 = types.InlineKeyboardButton('Б', callback_data = 'Б')

		markup.add(item1, item2)

		if not(data[user.id][0] == 10 or data[user.id][0] == 11):
			item3 = types.InlineKeyboardButton('В', callback_data = 'В')
			markup.add(item3)

		global also_delete
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Параллель выбрана', reply_markup = None)
		also_delete = bot.send_message(call.message.chat.id, 'ОК, ' + user.first_name + ', Вы выбрали ' + str(data[user.id][0]) + 'ю параллель. Какой класс?', reply_markup = markup)	

	def choose_letter(call):
		user = call.from_user
		data[user.id][1] = call.data
		parallel = data[user.id][0]-1

		if parallel == 9 or parallel == 10:
			if data[user.id][1] == 'В':
				bot.send_message(call.message.chat.id, user.first_name + ', харе ломать систему >:')
				data[user.id][1] = 'Б'

		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Класс выбран', reply_markup = None)

		markup = types.InlineKeyboardMarkup(row_width = 2)

		for day in day_of_the_week:
			if day == 'Суббота':
				if data[user.id][0] < 5:
					continue

			item = types.InlineKeyboardButton(day, callback_data = day)
			markup.add(item)

		if data[user.id][0] < 1:
			data[user.id][0] = 1

		if data[user.id][0] > 11:
			data[user.id][0] = 11

		global and_this_delete
		and_this_delete = bot.send_message(call.message.chat.id, 'Отлично, ' + str(data[user.id][0]) + data[user.id][1] + ' класс. На какой день недели?', reply_markup = markup)

	def choose_day_of_the_week(call):
		user = call.from_user
		data[user.id][2] = call.data
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'День недели выбран', reply_markup = None)
		bot.send_message(call.message.chat.id, 'Расписание для ' + str(data[user.id][0]) + data[user.id][1] + ' класса на ' + data[user.id][2].lower() + ':')
		show_table(call)

	def show_table(call):
		try:
			user = call.from_user
			parallel = data[user.id][0]-1

			if data[user.id][1] == 'А':
				letter = 0
			elif data[user.id][1] == 'Б':
				letter = 1
			else:
				letter = 2

			day = day_of_the_week.index(data[user.id][2])

			print(str(parallel) + ' ' + str(letter) + ' ' + str(day))

			table = config.table[parallel][letter][day]
			table_edit = []
			count = 1

			for item in table:
				table_edit.append(str(count) + '. ' + item)
				count += 1

			table = '\n'.join(table_edit)

			bot.send_message(call.message.chat.id, table)
		except:
			bot.send_message(call.message.chat.id, 'Ошибка. Нет данных для ' + str(data[user.id][0]) + data[user.id][1] + ' класса на ' + data[user.id][2].lower())


	@bot.callback_query_handler(func=lambda call:1)		
	def callback(call):
		user = call.from_user
		if call.message:
			if call.data.isdigit():
				if int(call.data) < 12:
					data[user.id][0] = int(call.data)
					choose_parallel(call)
			elif call.data == 'А' or call.data == 'Б' or call.data == 'В':
				choose_letter(call)
			elif call.data in day_of_the_week:
				choose_day_of_the_week(call)
except Exception as e:
	print(repr(e))

bot.polling(none_stop = 1)