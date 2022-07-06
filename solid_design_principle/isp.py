from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


# ok if you need a multifunction device
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')


    
'''
in case of OldMachine , we have only print functionality working but other 2 are not develop on 
old one, but we have inhereted from Machine interface, if we make then not availabe or mot implement.
this may be create a confusion beacuse we have added fax and scanner feature but these are not implemented.


to resolve this issue , we can seperate Machine intergface into small interfaces.
'''

class Printer:
    @abstractmethod
    def print(self,document):
        pass
    
class Scanner:
    @abstractmethod
    def scan(self,document):
        pass
    
#my Printer
class MyPrinter(Printer):
    def print(self, document):
        print(document)
        
class Photocopy(Printer,Scanner):
    def print(self, document):
        print(document)
        
    def scan(self, document):
        # print(document)
        pass


class MultiFunctionDevice(Scanner,Printer):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass
    
    
class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
    
    
printer = OldFashionedPrinter()
printer.print(12)  # nothing happens
printer.scan(123)  # oops!
    
    