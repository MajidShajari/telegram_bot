import logging

from telegram import Update
from telegram.ext import ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Stages
START_ROUTES, END_ROUTES = range(2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    logger.info("User started the conversation.")
    text_msg = f"""
                  درود
                  {user.first_name} {user.last_name}
                  به دمو تلگرام خوش آمدید
              """

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_msg)
    return START_ROUTES
