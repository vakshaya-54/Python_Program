list_5=[1,2,3,4,5]
print(list_5)

for data in list_5:
    print(data,end=" ")
print()
i=0 #1<5
while i<len(list_5):
    print(list_5[i],end=" ")
    i+=1
print()
list_6=[1,2,3,4,5]
list_6.append(6)
list_6.append(7)
print(list_6)
list_6.insert(0,1000)
print(list_6)

list_7=[10,20,30,40,20,30]
list_7.remove(30)
print(list_7)
list_7.pop()
print(list_7)
list_7.clear()
print(list_7)

print("index")
list_7=[10,20,30,40,20,30]
print(list_7[4])
print(list_7[-4])
