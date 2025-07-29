print("\nHello welcome to power calculator !! \n Firstlly, you have to give a number in the prompt.")
print("🧠What is power? Well, power means multiplying the number . For example : 3 and small 2 on top it means 3 * 3 which is nine / 9 . So let us begin !\n")

base = int(input("Type a number : "))
exp = int(input("How many times to be multiplied : "))

res = 1

for i in range(exp):
    res = res * base

print("\nThe answer is:", res)
print("Bye friends , be back next week .\n")
