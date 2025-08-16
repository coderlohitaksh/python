colors = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣"]  
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="") 
    for j in range(i):
        print(colors[j % len(colors)] , end = "")
    print()
