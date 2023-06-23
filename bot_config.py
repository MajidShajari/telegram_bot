from telegram import __version__ as TG_VER
from telegram.ext import Application, CommandHandler

from bot_command import start
from credentials import BOT_TOKEN

TOKEN = BOT_TOKEN


def _check_version():
    try:
        from telegram import __version_info__
    except ImportError:
        __version_info__ = (0, 0, 0, 0, 0)

    if __version_info__ < (20, 0, 0, "alpha", 1):
        raise RuntimeError(
            f"This example is not compatible with your current PTB version {TG_VER}. To view the "
            f"{TG_VER} version of this example, "
            f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
        )


def run_bot():
    _check_version()

    application = Application.builder().token(TOKEN).build()

    conv_handler = CommandHandler("start", start)

    application.add_handler(conv_handler)

    application.run_polling()
