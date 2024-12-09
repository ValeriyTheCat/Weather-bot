import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # paste your language here
owm = OWM( 'your pyOWM api', config_dict  )
owm = OWM('f173af0fc561a023c0561c674bbc7839')
mgr = owm.weather_manager()	
bot = telebot.TeleBot("12th:your telegram bot id", parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Введите имя любого города')
@bot.message_handler(commands=['info'])
def qwerty(message):
	bot.send_message(message.chat.id, 'Я бот созданый Зайко Валерием.\n' + 'Дата создания: 19.11.2021')
@bot.message_handler(content_types=['text'])
def maintask(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	preser = w.humidity
	wind = w.wind()["deg"]
	rainstatus = w.rain
	windway = ''
	if w.wind()['speed'] > 0:
		if wind < 180:
			if wind == 0:
				windway = 'Север'
			elif wind == 45:
				windway = 'Северo-Восток'
			elif wind > 45:
				windway = 'Bосток'
			elif wind == 90:
				windway = 'Bосток'
			elif wind == 130:
				windway = 'Юго-Восток'
			elif wind == 180:
				windway = 'Юг'
		if wind > 180 :
			if wind > 180 :
				windway = 'Юго-Запад'
			elif wind < 270 :
				windway = 'Юго-Запад'
			elif wind == 270:
				windway = 'Запод'
			elif wind > 270:
				windway = 'Северо-Заподo'
			elif wind < 360:
				windway = 'Северо-Заподo'
			elif wind > 315:
				windway = 'Север'
			elif wind > 360:
				windway = 'Север'
	else:
		windway = 'Там ветра нет'
	temp = w.temperature('celsius')["temp"]
	anwser = 'Сейчас в городе ' + message.text +' '+ w.detailed_status + '\n'
	anwser += 'Давление в районе ' + str(preser) + ' ед.'+ '\n' 
	anwser += 'Скоросьть ветра в городе ' + message.text +' '+ str(w.wind()['speed']) + ' м/с' + '\n' 
	if windway == 'Там ветра нет':
		pass
		# anwser =+ 'Там ветра нет'
	else:
		pass
		# anwser =+ str('Ветер дует на ') + str(windway) + str(' или на: ') +  str(wind) + str('\n')
	if rainstatus == {}:
		anwser += 'Дождь в районе ' + message.text + ' не идет' + '\n'
	elif rainstatus != {}:
		anwser += 'Дождь в районе ' + message.text + ' идет, надень дождевик!!!' + '\n'
	else:
		anwser += 'Я хз что там.Иди сам проверь.' +'\n'
	if temp < 10:
		anwser +='Там ппц как холодно, одевайся как танк.' + str(temp) + 'º'
	elif temp < 20:
		anwser +='Там холдодно, оденься потеплее.'+ str(temp) + 'º'
	else:
		anwser +='Там норм, одевайся как хочеш.'+ str(temp) + 'º'
	bot.send_message(message.chat.id, anwser)
	listofclients = []
	listofclients.append(message.chat.id)
	print(str(listofclients) + '\n' + anwser + '\n')
bot.infinity_polling()