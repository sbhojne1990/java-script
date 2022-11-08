# b=22
# print(b)
# def myfunctionB():
#     global b
#     print (b)
#     b=10
#     print(b)
# print(b)
# myfunctionB()
# print(b)
# f = lambda y:y*y
# print(f(5)) 
# def addall(a,b,c):
#     print(a+b+c)
# addall(11,22,33)
# def addallb(*args):
#     print(args)
#     return sum(args)
# q1 = addallb(11,33,44,55,66,77,88)
# print(q1)

# def displayPV(**kwargs):
#     print(kwargs.items())
#     for k,v in kwargs.items():
#         print(k,v)
# displayPV(firstname="Shriram",lastname="Bhojne",age=25)

# k=11,
# print(k)
# print(type(k))

# a1,b1 =k
# print(a1)
# print(b1)
# def addA():
#     a=10
#     print(a)
# addA()
# print(a)    // print(a) is not a global defined

# b=30
# def addB():
#     print(b)
# addB()
# print(b)

# diff in local and global scope
# c=100
# def addC():
   
#     c=90
#     print(c)
# addC()
# print(c)
# e=1000
# def addE():
#     global e
#     e=100
#     print(e)
# print(e)
# addE()
# print(e)

# e2=4000
# def addD():
#     global e2
#     e2=40
#     print(e2)
# print(e2)
# addD()
# print(e2)

# def square(x):
#     return x*x
# print(square(12))

# def mul(y):
#     return y+y
# print(mul(5))

# q1 = lambda x:x*x
# print(q1(10))
# print(q1(3))

# q2 = lambda y:y+y
# print(q2(5))

# def findGreater(x,y):
#     if(x>y):
#         print('X is Greater')
#     else:
#         print('Y is greater')

# findGreater(12,1)

q3 = lambda x,y:x if x>y else y
print(q3(22,33))


