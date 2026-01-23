class Employee :
    def __init__(self):
        print("Employee named Jack created .")

    def __del__ (self):
        print("Destructor is called now😈.")

def create_obj() :
    print("Making Objects......")
    obj = Employee( )
    print("Function ending......")
    return obj

print("Now ,the function create_obj() is called. Ha ha ha😈.")
obj = create_obj( )
print("Program ended , You escaped from darkness . ")
