#Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?

cost = float(input(" Please enter the actual cost of the product :"))
sale = float (input(" Please enter the sales amount :"))

if(sale > cost):
  amount = sale - cost
  print("Actual cost is {0} and sale amount = {1} so Total profit is {2}".format (cost,sale,amount))

if(sale < cost):
  amount = cost - sale
  print("Actual cost is {0} and sale amount = {1} so Total loss is {2}".format (cost,sale,amount))

else:
     print("No profit No gain !!!")
