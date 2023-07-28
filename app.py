from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys


try:
    ans = 2 + "3"
    print(ans)
    logging.info(ans)
except Exception as e:
    logging.info(SignException(e,sys))
    raise SignException(e,sys)




