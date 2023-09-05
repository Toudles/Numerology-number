name = input("Name: ")
cleanname = ""
total = 0
total1 = ""
for i in name.lower():
    if i.isalnum():
        cleanname += i
print("Your 'cleaned up' name is", cleanname)
print("Your 'cleaned up' name reduces to:")

for i in cleanname:
    total += (ord(i)-96)


    total1 = (str(ord(i)-96) + " + ")
    print(total1,end="")
    #print(total1 + str((ord(i)-96)) + " ", end=" + ")

print("=",total)







