from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import logging
from telegram.ext import filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

BOT_TOKEN = "7566090908:AAGTqHEgryIB8rvSciKuDexIgl0pV6hCrIE"

START_ANIMATION_URL = "https://media.tenor.com/eTrT0gLmtG0AAAAi/monkey-greeting-monkey.gif"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.send_animation(chat_id=update.effective_chat.id, animation=START_ANIMATION_URL,
                                         caption="Приветствую, ознакомься с командами бота!")
        logging.info(
            f"Отправлена гифка пользователю {update.message.from_user.username} ({update.message.from_user.id})")
    except Exception as e:
        logging.error(f"Ошибка при отправке гифки: {e}")


USER_STICKERS = {
    7146058196: "CAACAgIAAxkBAAENK7hnx_7h6Sz8PWUog-h6kCIq9XfrjgACYSQAAjMYSEllM27K13R3HDYE",
    1788991408: "CAACAgIAAxkBAAENLzRnyE_t8eWh9gbPT4srtZv-Tlm8OgACYzQAAuaA-EtdfQABBw0vp2A2BA",
    1375000244: "CAACAgIAAxkBAAENK8VnyAABKMXs-xXfeoWXZuFe5RzzRKkAAr9IAAJM_TlIQFOzw_7HFsg2BA",
    1924072157: "CAACAgIAAxkBAAENLxlnyE3ai4xETmW36iaocLjsDHz56wACOjUAAnBegUiUGQHBPXcCcTYE",
    6615649601: "CAACAgIAAxkBAAENLzhnyFAphusldZD9aFaZYHyw4cd_TgACTGgAAkdBsEqdnfeDXo-aeDYE"
}


async def vopros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response_text = "а тебе какая нахуй разница?"
        await update.message.reply_text(response_text)
        logging.info(
            f"Отправлен ответ на команду /vopros пользователю {update.message.from_user.username} ({update.message.from_user.id})")
    except Exception as e:
        logging.error(f"Ошибка при обработке команды /vopros: {e}")


async def creator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response_text = "Заебатый тип, а че?"
        await  update.message.reply_text(response_text)
        logging.info(
            f"Отправлен ответ на команду /creator пользователю {update.message.from_user.username} ({update.message.from_user.id}")
    except Exception as e:
        logging.error(f"Ошибка при обработке команды /creator: {e}")


async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        respose_text = "да хуй, она не работает, так что чильте"
        await update.message.reply_text(respose_text)
        logging.info(
            f"Отправлен ответ на команду /ai пользователю {update.message.from_user.username} ({update.message.from_user.id}")
    except Exception as e:
        logging.error(f"Ошибка при обработке команды /ai: {e}")


async def handle_specific_user_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"handle_specific_user_message вызвана!")

    try:
        user = update.message.from_user
        user_id = user.id
        logging.info(f"Начало обработки сообщения от пользователя {user.username} ({user_id})")

        if user_id in USER_STICKERS:
            sticker_file_id = USER_STICKERS[user_id]
            logging.info(f"Найден стикер для пользователя {user_id}: {sticker_file_id}")
            # Отправляем стикер в ответ на сообщение пользователя
            logging.info(f"Пытаемся отправить стикер...")
            await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=sticker_file_id)
            logging.info(f"Стикер успешно отправлен пользователю {user.username} ({user_id})")
        else:
            logging.warning(f"Не найден стикер для пользователя {user_id}")
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Извини, для тебя нет стикера!")


    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения или отправке стикера: {e}")


async def skull_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("ооо нет, это же череп, нам всем пиздец")
        logging.info(
            f"Ответили на смайлик черепа пользователю {update.message.from_user.username} ({update.message.from_user.id})")
    except Exception as e:
        logging.error(f"Ошибка при обработке смайлика черепа: {e}")


async def people_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("Люди! Вы хуй на блюде!")
        logging.info(
            f"Ответили на сообщение 'люди' пользователю {update.message.from_user.username} ({update.message.from_user.id})")
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения 'люди': {e}")


async def door_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("Дверь мне запили!")
        logging.info(
            f"Ответили на сообщение 'дверь' пользователю {update.message.from_user.username} ({update.message.from_user.id})")
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения 'дверь': {e}")


async def yes_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("Пизда")
        logging.info(
            f"Ответили на сообщение 'да' пользователю {update.message.from_user.username} ({update.message.from_user.id})")
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения 'да': {e}")


async def no_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("пидора овтет")
        logging.info(
            f"Ответили на сообщение 'пидора ответ' пользователю {update.message.from_user.username} ({update.message.from_user.id})")
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения 'пидора ответ': {e}")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(CommandHandler("vopros", vopros))

    app.add_handler(CommandHandler("creator", creator))

    app.add_handler(CommandHandler("ai", ai))

    skull_filter = filters.Regex(pattern=r"💀|☠️")

    app.add_handler(MessageHandler(skull_filter, skull_reaction))

    people_filter = filters.Regex(pattern=r"(?i)^люди$")

    app.add_handler(MessageHandler(people_filter, people_reaction))

    door_filter = filters.Regex(pattern=r"(?i)^дверь$")

    app.add_handler(MessageHandler(door_filter, door_reaction))

    yes_filter = filters.Regex(pattern=r"(?i)^да$")

    app.add_handler(MessageHandler(yes_filter, yes_reaction))

    no_filter = filters.Regex(pattern=r"(?i)^нет$")

    app.add_handler(MessageHandler(no_filter, no_reaction))

    user_filter = filters.User(user_id=list(USER_STICKERS.keys()))

    app.add_handler(MessageHandler(user_filter & filters.TEXT, handle_specific_user_message))

    app.run_polling()


if __name__ == '__main__':
    main()
