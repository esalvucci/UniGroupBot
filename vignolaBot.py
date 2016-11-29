import telepot
import sys
import time
import random
import datetime
import vignolaBotToken


# funzione che viene eseguita ad ogni messaggio ricevuto
def handle(message):
<<<<<<< HEAD
	chat_id = message['chat']['id']
	command = message['text']

	foo = ['E\' bugggggia', 'uagliooo!', 'stasera devo programmare...', 'st\'Arduino!', 'Uaglio so arrivat ', 'eeeeeeeee credo di si...no buggia, \'sto weekend sto con Azzurra', 'Tonno e cipodda per fa lu soffrittu..capi\'?']
	
	print(random.choice(foo))	
=======
    chat_id = message['chat']['id']
    command = message['text']
    import random

    foo = ['E\' bugggggia', 'uagliooo!', 'stasera devo programmare...', 'st\'Arduino!', 'Uaglio so arrivat ',
           'eeeeeeeee credo di si...no buggia, \'sto weekend sto con Azzurra',
           'Tonno e cipodda per fa lu soffrittu..capi\'?']

    print(random.choice(foo))
>>>>>>> 85def9495b1a95cb4a8723c30ca58c66307316f7

    print('Ho ricevuto il comando %s' % command)

<<<<<<< HEAD
#			TODO			#
#	if command == '/help':
# 		bot.sendMessage(chat_id,messaggio)
	if command == '/start':
		bot.sendMessage(chat_id, 'Esegui il comando /random per richiedere una frase di Vignola a caso')
	elif command == '/random':
		bot.sendMessage(chat_id, random.choice(foo))
=======
    # TODO
    # if command == '/help':
    # bot.sendMessage(chat_id, messaggio)
    if command == '/start':
        bot.sendMessage(chat_id, 'Esegui il comando /random per richiedere una frase di Vignola a caso')
    elif command == '/random':
        bot.sendMessage(chat_id, random.choice(foo))
>>>>>>> 85def9495b1a95cb4a8723c30ca58c66307316f7

bot = telepot.Bot(vignolaBotToken.token)
bot.message_loop(handle)

print('In attesa di nuovi messaggi...')

while 1:
    time.sleep(100)