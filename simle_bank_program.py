from os import name
import time
import random

print("WELCOME TO BANJO'S BANK!\n")  
print("1) Create an account\n2) Login\n3) Quit ") 
res=input("Press 1 to create an account and two to login\n") 
data={}

if res=="1":
  first_name=input("First name:  \n")
  last_name=input("Last name: \n")
  login_pin=input("Set your login pin: ")
  transaction_pin=input("Set your transaction pin: ")
  print("Creating account....")
  time.sleep(3)
  print("Please wait...")
  time.sleep(3)
  print("Completing setup...")
  time.sleep(2)
  def generate_acc(n):
    acc= ""
    for _ in range(n):
       acc+=str(random.choice(range(10)))
    return acc
    
  acc_no=("0"+generate_acc(9))
  print("Your account number is:"+ " "+acc_no)
  print("Welcome to BANJO'S BANK ",first_name," ",last_name)
  data[acc_no]={"first_name":first_name,
  "last_name":last_name,
  "login_pin":login_pin,
  "transaction_pin":transaction_pin,
  "balance":0}
elif res=="2":
    acc_no = input("Please enter your account number ::> ")
    login_pin = input("enter your login pin ::>")
    acc_no= data.get(acc_no, False)
    login_pin= data.get(login_pin, False)
    if acc_no and login_pin:
        print("PRESS \n 1) Deposit money. \n 2) Withdraw money. \n 3) Transfer \n 4) Check balance \n")
        tran=input("::>")
        if tran=="1":
            




