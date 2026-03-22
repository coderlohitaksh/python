class myClass :
    __privateVar = 27;

    def __privMeth (self):
        print("I am in private session 😈")
    def hello (self):
        print("The secret code is ",myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privMeth