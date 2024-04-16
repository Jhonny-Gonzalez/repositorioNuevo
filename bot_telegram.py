import logging
import re

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Expresión regular para iniciar el bot con cualquiera de las siguientes expresiones
iniciar_bot = re.compile(r"konnichiwa|hi|hey|hola", re.IGNORECASE)
# Expresión regular para poder recibir respuestas posibles
answer1 = re.compile(r"si|simon|sip", re.IGNORECASE)
# Expresión regular para poder recibir respuestas posibles
question1 = re.compile(r"obvio|claro", re.IGNORECASE)
# Expresion regular que solo admite el número 2006 o alguna cadena que termine con este año como respuesta
answer2 = re.compile(r"^([a-zA-Zñ]?\s?)+(2006)$", re.IGNORECASE)
# Expresion regular que solo admite el número 2000 o alguna cadena que termine con este año como respuesta
answer3 = re.compile(r"^([a-zA-Zñ]?\s?)+(2000)$", re.IGNORECASE)
# Expresion regular que solo admite el número 2000 o alguna cadena que termine con este año como respuesta
answer4 = re.compile(r"no|ño|jaja gracias|nel", re.IGNORECASE)
# Expresión regular para poder recibir respuestas posibles
answer5 = re.compile(r"cuarteto referencia", re.IGNORECASE)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def adios_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /adios is issued."""
    await update.message.reply_text("Adios!")
    context.application.stop_polling()


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches the regular expression."""
    message_text = update.message.text
    if iniciar_bot.search(message_text):
        await update.message.reply_text("Buenas, sos fan de El Cuarteto de nos? 🤔")
    elif answer1.search(message_text):
        await update.message.reply_text("Apoco si tinguililingui? 🤨")
    elif question1.search(message_text):
        await update.message.reply_text("Avr si muy duro mi tibio, ¿En qué año se lanzo el albúm 'Raro'? 🥴")
    elif answer2.search(message_text):
        await update.message.reply_text("Si es, waos, avr dime en que año se lanzó 'Cortamambo'? 😎")
    elif answer3.search(message_text):
        await update.message.reply_text("Ayyyyy, si le mueves bien sabroso master 🥵🤑🥵, por último, dame los 16 dígitos de tu tarjeta y te digo que miembro del Cuareto eres 👻")
    elif answer4.search(message_text):
        await update.message.reply_text("a, ta wenu, me voy a punta cana causa 💅💅 *se va volando")
    elif answer5.search(message_text):
        await update.message.reply_text("Ño, fokiu, ya no juego *se va a la casa de damian 👻")
    else:
        await update.message.reply_text("Jijo mano, yo en inglés solo se decir 'yes' 🤡")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token("6943124235:AAG3R_aC9YnQqd_pslAuCLgaXg_0Qw0uWX4").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CommandHandler("adios", adios_command))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()