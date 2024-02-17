from .absPrinter import AbsPrinter
import logging

from .absPrinter import AbsPrinter
class StdPrinter(AbsPrinter):
    def __init__(self):
        pass

    def print(self,str='',end='\n'):
        print(str,end=end)

class LoggingPrinter(AbsPrinter):
    def __init__(self, logPath):
        self.logPath=logPath;
        print("[Init LogFile]\t" + logPath);
        logging.basicConfig(
            filename=logPath,
            level=logging.CRITICAL,
            format="[%(asctime)s]\t %(message)s",
            datefmt="%Y/%m/%d/ %I:%M:%S %p")

    def print(self,str=''):
        logging.getLogger().critical(str)