class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):   # less than
        return self.a < other.a

    def __eq__(self, other):   # equal
        return self.a == other.a


ob1 = A(2)
ob2 = A(3)
print("Passed value is", ob1.a, ob2.a)
print("Is ob1 < ob2?", ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print("Passed value is", ob3.a, ob4.a)
print("Is ob3 == ob4?", ob3 == ob4)