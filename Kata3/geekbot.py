from telegram.ext import Updater, CommandHandler

def main():
#    updater = Updater(token=open("./bot_token").read(), use_context=True) #llamada al token si lo tuviera en el archivo: bot_token
    updater = Updater(token="941495867:AAFGVk6eiYfErSqq0e9nYVUZ1HdLxdQXjTs", use_context=True)
    #Añadiendo un manejador al comando /start /repite /suma
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("repite", repite))
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    updater.start_polling()
    updater.idle() #cuando alguien intente terminar el bot, el bot intentará acabar las tareas

def start(update, context):
    update.message.reply_text("Hola, soy un bot")
    
def repite(update, context):
    update.message.reply_text(update.message.text) #respondemos al mensaje con el mensaje

def suma(update, context):
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("El resultado es " + str(resultado))

main()