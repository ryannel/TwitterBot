import logging
import sys, os
import __main__
import traceback

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("oauthlib").setLevel(logging.WARNING)
logging.getLogger("requests_oauthlib").setLevel(logging.WARNING)

mainPath = os.path.dirname(os.path.abspath(__main__.__file__))

FORMAT = "%(asctime)s - %(levelname)s: %(message)s"
logging.basicConfig(format=FORMAT, filename=mainPath + '/main.log' , level=logging.DEBUG)

logger = logging

def log_uncaught_exceptions(ex_cls, ex, tb):
        logging.critical('{0}: {1}'.format(ex_cls, ex) + '\nTrace:\n' + ''.join(traceback.format_tb(tb)))

sys.excepthook = log_uncaught_exceptions