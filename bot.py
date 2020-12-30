import os
from telegram.ext import Updater, Defaults
from telegram import ParseMode
from addons.utils import logger
from handlers.handlers import msg_handlers


def main():
    logger.warning("ahh waking up...")
    defaults = Defaults(parse_mode=ParseMode.HTML)
    updater = Updater(token = "1427727502:AAFBD9STpqKLD9rfSEXrQnB92od1RTR_WII" ,use_context=True ,workers=200)
    msg_handlers(updater.dispatcher)
    updater.start_polling()
    logger.warning("Ready to rock...")
    updater.idle()

if __name__ == '__main__':
    main()