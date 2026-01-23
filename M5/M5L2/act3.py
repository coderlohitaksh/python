class pair_elements:
    def two_sum(self , target , number):
        lookup = {}

        for i , num in enumerate(num):
            if target - i in lookup :
                return(lookup[target - num] , i)
            lookup(num) = i

value = int(input("Enter sum which you want to take for this search :"))
print("index1 = %d , index2 = %d" % pair_elements().two_sum(10 , 20 , 30 , 40 , 50 , 60 , 70),value) 
