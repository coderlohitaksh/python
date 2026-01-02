a = {1 , 2 , 3 , 4 , 5}
b = {'a' , 'b' , 'c' , 'd' , 'e'}
c = zip(a , b)
print(c , "\n")

l1 = [10 , 20 , 30 , 40 , 50]
l2 = [2500 , 1600 , 900 , 400 , 100]
for x , y in zip(l1 , l2[::-1]):
    print(x , y)

stocks = ['Infosys' , 'Tata' , 'Tcs' , 'OCPL']
prices = [20000 , 10000 , 30000 , 100000]

new_dict = {stocks: prices for stocks , prices in zip(stocks , prices)}
print("\n{}".format (new_dict))
