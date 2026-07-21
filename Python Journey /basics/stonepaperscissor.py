import random 

inpt = input("enter your choice (stone paper or scissor) : ")
list = ['stone','paper','scissor']
computer  = random.choice(list)
while True:
    print("computer choice is : ",computer)

    if inpt == computer:
       print("you both choose same thing")
    elif inpt != computer :
          if computer == 'stone' and inpt == 'scissor':
              print("you loose")
          elif  computer == 'stone' and inpt == 'paper' : 
              print("you win ")
          elif computer == 'paper' and inpt == 'stone' : 
              print("you loose")
          elif computer('paper') and inpt == 'scissor':
              print("you win")
          elif computer('scissor') and inpt == 'paper':
              print("you loose")
          elif computer('scissor') and inpt == 'stone':
              print("you win")
    choice = input("want to do another calculation ? (yes/no)")
    if choice == 'no':
        print("code exitted")
        break 
    elif choice == 'yes' :
        inpt = input("enter your choice (stone paper or scissor) : ")