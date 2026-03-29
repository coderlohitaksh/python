from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self, x):
        print("Passed value is", x)

    @abstractmethod
    def task(self):
        print("I am inside Abstract classes.")

class test_class(Absclass):
    def task(self):
        print("I am inside test classes.")

test_obj = test_class()
test_obj.task()
test_obj.print(100)