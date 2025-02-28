import logging
from logging.handlers import RotatingFileHandler
from setup import verbose

class AppLogger:
    def __init__(self):
        self.logfile = "app.log"

        logging.basicConfig(filename=self.logfile, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        self.smsLogger = logging.getLogger("SMS")
        self.gptLogger = logging.getLogger("GPT")
        self.gmailLogger = logging.getLogger("MAIL")

    def SMS_LOG_EVENT(self, message: str, type: str):
        if not verbose: return
        match type.lower():
            case "info":
                self.smsLogger.info(message)
            case "debug":
                self.smsLogger.debug(message)
            case "error": 
                self.smsLogger.error(message)
            case "warning": 
                self.smsLogger.warning(message)

    def GPT_LOG_EVENT(self, message: str, type: str):
        if not verbose: return
        match type.lower():
            case "info":
                self.gptLogger.info(message)
            case "debug":
                self.gptLogger.debug(message)
            case "error": 
                self.gptLogger.error(message)
            case "warning": 
                self.gptLogger.warning(message)

    def GMAIL_LOG_EVENT(self, message: str, type: str):
        if not verbose: return
        match type.lower():
            case "info":
                self.gmailLogger.info(message)
            case "debug":
                self.gmailLogger.debug(message)
            case "error": 
                self.gmailLogger.error(message)
            case "warning": 
                self.gmailLogger.warning(message)


