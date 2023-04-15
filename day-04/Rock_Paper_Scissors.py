import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

map = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

computer_choice = random.choice(map)

user_choice_ascii = map[user_choice]

if user_choice_ascii == scissors and computer_choice == paper:
    print(f"{user_choice_ascii}\n{computer_choice}\nYou win.")

elif user_choice_ascii == paper and computer_choice == rock:
    print(f"{user_choice_ascii}\nComputer chose:\n{computer_choice}\nYou win.")

elif user_choice_ascii == rock and computer_choice == scissors:
    print(f"{user_choice_ascii}\nComputer chose:\n{computer_choice}\nYou win.")

elif user_choice_ascii == scissors and computer_choice == scissors:
    print(f"{user_choice_ascii}\nComputer chose:\n{computer_choice}\nIt's a draw")

elif user_choice_ascii == paper and computer_choice == paper:
    print(f"{user_choice_ascii}\nComputer chose:\n{computer_choice}\nIt's a draw")

elif user_choice_ascii == rock and computer_choice == rock:
    print(f"{user_choice_ascii}\nComputer chose:\n{computer_choice}\nIt's a draw")

else:
    print(f"{user_choice_ascii}\nComputer chose:\n{computer_choice}\nYou lose.")
