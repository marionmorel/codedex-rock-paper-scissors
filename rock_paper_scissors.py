import random

print('===================')
print('Rock Paper Scissors')
print('===================')

player = int(input('1) ✊ \n2) ✋ \n3) ✌️ \nPick a number: '))
computer = random.randint(1, 3)

if player == 1:
    print('\nYou chose: ✊')
elif player == 2:
    print('\nYou chose: ✋')
elif player == 3: 
    print('\nYou chose: ✌️')
else:
    print('Wrong input.')

if computer == 1:
    print('CPU chose: ✊')
elif computer == 2:
    print('CPU chose: ✋')
elif computer == 3: 
    print('CPU chose: ✌️')

if player == 1:
    if computer == 1:
        print('It\'s a tie!')
    elif computer == 2:
        print('The computer won!')
    elif computer == 3:
        print('The player won!')
elif player == 2:
    if computer == 1:
        print('The player won!')
    elif computer == 2:
        print('It\'s a tie!')
    elif computer == 3:
        print('The computer won!')
elif player == 3:
    if computer == 1:
        print('The computer won!')
    elif computer == 2:
        print('The player won!')
    elif computer == 3:
        print('It\'s a tie!')