class IOString:
    def __init__(self):
        self.str = ""
    def get_String(self):
        self.str = input("Give any word , sentence etc : ")
    def print_String(self) :
        print("The word/sentence which you have given will be now printed in uppercase . So, the result is ",self.str.upper())
    
str1 = IOString()
str1.get_String()
str1.print_String()