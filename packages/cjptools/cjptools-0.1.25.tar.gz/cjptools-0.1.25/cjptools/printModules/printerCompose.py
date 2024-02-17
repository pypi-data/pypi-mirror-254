from .absPrinter import AbsPrinter

class PrinterCompose(AbsPrinter):

    def __init__(self,printers=[]):
        self.printers=printers;

    def add(self,printer):
        self.printers.append(printer);

    def print(self, str=''):
        for printer in self.printers:
            printer.print(str);