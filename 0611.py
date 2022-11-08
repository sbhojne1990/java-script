listA =[1989,1990,1991,1992]
listB =[33,32,31,30]
for items in listA:
    # print(2022-items)
    listB.append(2022-items)
print(listB)

#Map
q2=list(map(lambda x:2022-x,listA))
print(q2)


listC=[11,1,2,33,4,4,55]

q3=list(map(lambda x:x*3,listC))
print(q3)

listD=[11,22,33,44,55,66]
q4 = list(map(lambda y:y*3,listD))
print(q4)

listE = [11,22,33,44,55,66,77]
listf=[]

for items in listE:
    if items>50:
        listf.append(items)
print(listf)
        
q5 = list(filter(lambda x:x>50,listE))
print(q5)

listG = [33,44,55,22,3,477,88,99]
print(list(filter(lambda x : x%2 == 0,listG)))

