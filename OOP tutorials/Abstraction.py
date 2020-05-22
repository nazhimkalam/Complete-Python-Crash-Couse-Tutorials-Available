from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass             # NOTE: abstracted methods are only declared not defined

class Laptop(Computer):
    def process(self):
        print('Laptop running')

class Desktop(Computer):
    def process(self):
        print('Desktop running')

# main program
lap = Laptop()
lap.process()

des = Desktop()
des.process()