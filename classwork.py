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
