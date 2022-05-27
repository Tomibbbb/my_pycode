#a=[4,3,2,1,8]
#b=a
#b[3]=7
#print(b)
#print(a)

#b=a.copy()
#b[3]=7
#print(b)
#print(a)

#a=[1,2,3,4]
#b=[1,2,3,4]
#print(a==b)
#print(a is b)


#list1=["mike","","emma","kelly","","brad"]
#list1.pop(1)
#list1.pop(3)
#print(list1)

#or

#j=[x for x in list1 if x]
#print(j)
import random


def generate_otp(n):
    otp= ""
    for _ in range(n):
       otp+=str(random.choice(range(10)))
    return otp

print(generate_otp(7))

##SET

#a={1,2,3,4,5}
#b={2,4,6,8,10}
#a.discard(4)
#a.remove(4)
#a.clear()
#c=a.union(b)
#c=a.intersection(b)
#a.intersection_update(b)
#print(a)

##a={3,4781017}
#b={1,4,3,1,3,5,7,9}
#print(b)

