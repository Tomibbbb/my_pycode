import random


def generate_otp(n):
    otp= ""
    for _ in range(n):
       otp+=str(random.choice(range(10)))
    return otp

data={}
print("Welcome to VICTORIA'S GAME❤️!")
#D=input("Do you want to login or signup? press 1 to login and 2 to signup\n")
while True:
   D=input("Do you want to login or signup? press 1 to login and 2 to signup\n")
   if D == '2':
        name=input("What is your name? ")
        uid = generate_otp(6)
        data[uid]={"name":name,
                    "score":0}
        print("Thank you for signing up",name)

        print("This is your unique ID", uid)
   elif D == 1:
        uid =input("enter you unique ID: ")
        B=data.get(uid,False)   
        if B:
            import random
            option = ["r","p","s"]
            trial = 3
            score = 0
            print("Welcome to victoria")
            while trial > 0:

                print("""\n select R  for  rock ,P for paper and S for scissors""")
                player_choice= input("enter you choice \n")
                com_choice = random.choice(option)
    
                if player_choice in option:

                    if player_choice == option[0] and com_choice==option[2]:
                        print("You win")
                        print("computer choose",com_choice)
                        trial+=1
                        score+=2
                    elif player_choice==option[2] and com_choice==option[1] :
                         print("You win")
                         print("computr choose",com_choice)
                         trial+=1
                         score+=2
                    elif player_choice== option[1] and com_choice[0]:
                         print("You win")

                         print("computer choose",com_choice)  
                         trial+=1
                         score+=2
                    else:

                        print("Invalid input")
                        trial=1

                    print(f"{trial} trails left")
            print("Game over")  
            print("you scored",score) 
            prev_score = data.get("score",0) 
            if score > prev_score:

                print("You just beat your previous high score!🎉🎉")
                data["score"]= score
                print (f"\nYou scored{score} points")  
                print("Game over ):")      
                choice =input("Play again?Y/N :").lower()
                if choice=="n":

                    break

print(data)        
  
   


