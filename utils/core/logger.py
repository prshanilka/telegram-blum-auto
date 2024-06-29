import sys

from loguru import logger


def logging_setup():
    format_info = "<green>{time:HH:mm:ss.SS}</green> | <blue>{level}</blue> | <level>{message}</level>"
    logger.remove()

    logger.add(sink=sys.stdout, format="<white>{time:YYYY-MM-DD HH:mm:ss}</white>"
                                       " | <level>{level: <8}</level>"
                                       " | <cyan><b>{line}</b></cyan>"
                                       " - <white><b>{message}</b></white>")
    logger.add("logfile.log",
               format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
               rotation="10 MB",  # Rotate the log file when it reaches 10 MB
               retention="10 days",  # Keep logs for 10 days
               level="INFO")


logging_setup()
