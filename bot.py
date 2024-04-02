#!/usr/bin/python

import finanzas
import telebot
import threading
from mi_conf import TOKEN, MI_CHAT_ID # importo el archibo mi_conf.py donde tengo mi token del bot, y la constante mi_token
from function_registro import registro # importo de function_registro.py la funcion registro()

bot = telebot.TeleBot(TOKEN) # instancio el bot y le paso el token

@bot.message_handler(commands=["start"]) # manejador del comando start

def cmd_start(message):
    # funcion que contiene las acciones del bot cuando convoquen start
    var_comando = message.text
    respuesta = "200"
    registro(message.chat.id, respuesta, var_comando, message.from_user.username)
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id,f" Hola {message.from_user.first_name}, Bienvenido a  Blindtrading Bot ")    
    bot.reply_to(message,text=
    f"""<i><b><u>El siguiente menu, muestra los comandos disponibles</u></b></i>
    <b><i>/start</i></b> ➡️ Menu de inicio
    <b><i>/p</i></b> ➡️ Precio del activo (enviame /p espacio el ticker o par).
    """, parse_mode="html")

@bot.message_handler(commands=["p"]) # manejador del comando p de precio 

def cmd_ultimopreciobtc(message):
    # contiene las accione del comando /p
    var_comando = message.text
    respuesta = "200"
    registro(message.chat.id, respuesta, var_comando, message.from_user.username)
    activo = var_comando[3:].upper()
    pa = finanzas.PrecioActual(activo)
    bollinger = finanzas.BandasBollinger(activo)    
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message,text=
    f"""El precio de {activo}, es:
    {pa}.
    La Ma de 7 es: {finanzas.Ma7(activo)},
    la Ma de 21 es: {finanzas.Ma21(activo)},
    la Ma de 30 es: {finanzas.Ma30(activo)},
    la Ma de 50 es: {finanzas.Ma50(activo)}
    y la Ma de 100 es: {finanzas.Ma100(activo)}
    <i>Las Bandas de Bollinger</i>
    Superior: {round(bollinger[0][-1])}
    Media: {round(bollinger[1][-1])}
    Inferior: {round(bollinger[2][-1])}
    los datos suministrados son en temporalidad de un dia
    """, parse_mode="html")


@bot.message_handler(commands=["log"]) # manejador del comando log

def cmd_log(message):
    # contiene las accione del comando log
    var_comando = message.text
    if message.chat.id == MI_CHAT_ID:
        respuesta = "200"
        registro(message.chat.id, respuesta, var_comando, message.from_user.username)
        bot.send_chat_action(message.chat.id, "upload_document")
        archibo_log = open("registro_ID.txt", "rb")
        bot.send_document(message.chat.id, archibo_log)
    else:
        respuesta = "404"
        registro(message.chat.id, respuesta, var_comando, message.from_user.username)
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "COMANDO DISPONIBLESOLO PARA USUARIOS AUTORISADOS")

#respondiendo a los mensajes de texto que no son comandos

@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact']) # manejador de todo lo que no esta permitido

def bot_mensajes_texto(message):
    # Gestiona los mensajes de texto recibidos
    if message.text and message.text.startswith("/"):
        registro(message.chat.id, "404", message.text, message.from_user.username)
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "Comando no disponible")
    else:
        registro(message.chat.id, "404", message.text, message.from_user.username)
        bot.send_chat_action(message.chat.id, "upload_photo")
        #foto = open("prueba.png", "rb")
        #bot.send_photo(message.chat.id, foto, "Alto Wallpaper perro")

def recibir_mensajes():
    # Bucle infinito que comprueba si hay nuevos mensajes en el bot
    bot.infinity_polling()

#MAIN ########################################################
def main():
    #Por cada nuevo comando que agrego, se debe agregar el comando, y este rige el orden de los mismos. 
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Menu Inicio"),
        telebot.types.BotCommand("/p", "Dvuelve el precio del activo y las Ema de 7, 20 hy 30"),
        #telebot.types.BotCommand("/log", "Envia el archibo registro_ID"),
        ])
    print('Iniciando " Bot"')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    print('Bot iniciado')
    bot.send_message(MI_CHAT_ID,"Elvin Vargas Bot, iniciado con éxito😁")

if __name__ == "__main__":
    main()   


