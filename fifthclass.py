# program for prime number
def pnf(n)
num =int(input("enter a number \n"))
bas = False
if pnf(num )> 1 :
   for i in range(2,num):
       if(num % i) ==0:
          bas = True

          break
if bas:
   print(num,"is not a prime number")  
else:
   print(num,"is a prime number")  


 #while loop
 # h=1
 # while h<=10:
 #    h+=1
 #    print(h)  

#c =[ 6,7,8,9,10]  
#c[3]=56
#print(c)



#a=[1,2,3,4,5,6,7]
#for element in a:
 #   print(element)


#a = [x**2 for x in range(10)]
#print(a)


#a=[x if x%2==0 else 0 for x in range(10)]
#print(a)

