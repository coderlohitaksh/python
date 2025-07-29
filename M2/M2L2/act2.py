

txt = str(input("Enter a string : "))
txt = txt.split()
bwl = 0

for wrd in txt:
    txtlen = wrd(len)
if (txtlen > bwl):
    bwl = txtlen

print("The largest word is : ")
for txtlen in txt:
    txtlen = len(txt)
    if txtlen == bwl :
        print(txt)
