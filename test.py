from datetime import datetime
from time import sleep
import logging

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "mylog.log",
                    filemode = "w",
                    format = Log_Format,
                    level = logging.INFO)
logger = logging.getLogger()
logger.error("Our First Log Message")

while(1):
    sleep(5)

    print("print " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    logger.info(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    # print(1/0) # 輸出錯誤時使用