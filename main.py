from os import path
import os
from configuration import Config
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, MessageHandler, filters
from ocr import get_text
from typing import Set
from models import Esper
from config import settings
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
config_path = path.abspath("config.json")
config = Config(config_path)


async def analyze(update: Update, context: CallbackContext.DEFAULT_TYPE):
    photos = update.effective_message.photo
    photo = photos[-1]
    file = await photo.get_file()
    downloaded = await file.download()
    path = str(downloaded.resolve().as_posix())
    recognized_text = get_text(path)
    os.remove(path)
    available_espers = config.to_set_full()
    possible_espers = [text for text in recognized_text if text.lower().replace(" ", "") in available_espers]
    sets: Set[Esper] = set([config.get_esper(esper) for esper in possible_espers])
    if len(sets) != 5:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"{update.effective_user.name} Ho trovato solo {len(sets)-1} Espers [{', '.join([esper.name for esper in sets-set(None)])}]")
        return

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"{update.effective_user.name} I tuoi esper sono [{', '.join([esper.name for esper in sets])}]")


if __name__ == '__main__':
    application = ApplicationBuilder().token(settings.TELEGRAM_TOKEN).build()
    analyze_handler = MessageHandler(filters.PHOTO & filters.Caption(['analyze', "Analyze"]) & filters.ChatType.GROUPS, analyze)
    application.add_handler(analyze_handler)
    application.run_polling()
