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


reduce = total
trait = False
reduction = 0
while trait == False:
    for i in str(reduce):
        reduction += int(i)
        
    print("Furhter reduction: ", reduction)
    if int(reduction) == 0:
        print("This name means... emptiness, nothingness, blank")
        trait = True
    elif int(reduction) == 1:
        print("This name means... independence, loneliness, creativity, originality, dominance, leadership, impatience")
        trait = True
    elif int(reduction) == 2:
        print("This name means... quiet, passive, diplomatic, co-operation, comforting, soothing, intuitive, compromising, patient")
        trait = True
    elif int(reduction) == 3:
        print("This name means... charming, outgoing, self expressive, extroverted, abundance, active, energetic, proud")
        trait = True
    elif int(reduction) == 4:
        print("This name means... harmony, truth, justice, order discipline, practicality")
        trait = True
    elif int(reduction) == 5:
        print("This name means... new directions, excitement, change, adventure")
        trait = True
    elif int(reduction) == 6:
        print("This name means... love, harmony, perfection, marriage, tolerance, public service")
        trait = True
    elif int(reduction) == 7:
        print("This name means... spirituality, completeness, isolation, introspection")
        trait = True
    elif int(reduction) == 8:
        print("This name means... organization, business, commerce, new beginnings")
        trait = True
    elif int(reduction) == 9:
        print("This name means... romatic, rebellious, determined, passionate, compassionate")
        trait = True
    reduce = reduction
    reduction = 0