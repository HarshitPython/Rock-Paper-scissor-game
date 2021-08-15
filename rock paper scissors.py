#Symbol for rock.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

#Symbol for paper.
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

#symbol for scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''






import random

a = int(input('What do you choose ?"0" for rock, "1" for paper, "2" for scissors \n'))

if a == 0:
    print(rock)
elif a == 1:
    print(paper)
elif a == 2:
    print(scissors)

b = random.randint(0,2)
print(f"Computer choose: \n {b}")

if b==0:
    print(rock)
elif b==1:
    print(paper)
else:
    print(scissors)

if(a == 0) and (b == 1):
    print("You Loose")
elif(a == 0) and (b == 2):
    print("You Win")
elif(a == 1) and (b == 0):
    print("You Win")
elif(a == 1) and(b == 2):
    print("You Loose")
elif(a == 2) and (b == 0):
    print("You Loose")
elif(a == 2) and (b == 1):
    print("You Win")
else:
    print("Draw")
    
