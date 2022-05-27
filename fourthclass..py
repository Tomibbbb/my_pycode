#def factorial(n):
 #   if n==1 :
 #       return 1
 #   if n==0 :
 #       return 1
 #   recurse = n * factorial(n-1)
  #  print(recurse)
  #  return recurse

#factorial(5)

#print("x")
#if 4>5:
 #   print(7)

#print(4)



#print("x")
#if 7>5:
 #   print(7)
#if 4<5:
 #   print(8)
#my_str = "this is a lovely sring"
#a = list(map(lambda f:f.upper(),my_str))
#print("".join(a))
            
#def tri_recursion(k):
#  if(k > 0):
#    result = k + tri_recursion(k - 1)
#    print(result)
#  else:
#    result = 0
#  return result

#print("\n\nRecursion Example Results")
#tri_recursion(6)




import random
from stringprep import in_table_c5
from tkinter import TRUE

data={}
a=[1,2,3,4,5,6,7]

print("Guess the computer's choice to win the prize. ")
print("select a number from",a)

while TRUE:
  username =input("Username: ")
  trial = 3
  score = 0
  while trial > 0:
   random.shuffle(a)
   print("\n select a number from:",a)
   com_choice = random.choice(a)
   user =int(input("your choice: \n"))
   if user == com_choice:

      print("You win")
      score+=2
      trial+=1
      print(f"You have won an extra trial")
      print(f"{trial} trail(s) left")
   else:

     if user > com_choice:
       print("Too high")
     else:
        print("Too low")
     trial-=1
     print(f"{trial} trail(s) left") 
   prev_score = data.get(username,0) 
   if score > prev_score:
     print("You just beat your previous high score!🎉🎉")
     data[username]= score
  print (f"\nYou scored{score} points")  
  print("Game over ):")      
  choice =input("Play again?Y/N :").lower()
  if choice=="n":
    break

print(data)



#for i in range (90,120):
 # if i % 2 != 0:
  # print(i)
   

#b =[1,2,3,4,15,22,21,33,50,55,72,66,95]
#for i in b:
#  if i%3==0 or i%5==0:
 #   print(i)


 
             

