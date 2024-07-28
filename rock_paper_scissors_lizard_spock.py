import random

print('================================')
print('Rock Paper Scissors Lizard Spock')
print('================================')

player = int(input('1) ✊ \n2) ✋ \n3) ✌️ \n4) 🦎 \n5) 🖖 \nPick a number: '))
computer = random.randint(1, 5)

if player == 1:
    print('\nYou chose: ✊')
elif player == 2:
    print('\nYou chose: ✋')
elif player == 3: 
    print('\nYou chose: ✌️')
elif player == 4:
    print('You chose: 🦎')
elif player == 5:
    print('You chose: 🖖')
else:
    print('Wrong input.')

if computer == 1:
    print('CPU chose: ✊')
elif computer == 2:
    print('CPU chose: ✋')
elif computer == 3: 
    print('CPU chose: ✌️')
elif computer == 4:
    print('CPU chose: 🦎')
elif computer == 5:
    print('CPU chose: 🖖')

if player == 1:
    if computer == 2 or computer == 5:
        print('The computer won!')
    elif computer == 3 or computer == 4:
        print('The player won!')
    elif computer == 1:
        print('It\'s a tie!')
elif player == 2:
    if computer == 1 or computer == 5:
        print('The player won!')
    elif computer == 3 or computer == 4:
        print('The computer won!')
    elif computer == 2:
        print('It\'s a tie!')
elif player == 3:
    if computer == 1 or computer == 5:
        print('The computer won!')
    elif computer == 2 or computer == 4:
        print('The player won!')
    elif computer == 3:
        print('It\'s a tie!')
elif player == 4:
    if computer == 1 or computer == 3:
        print('The computer won!')
    elif computer == 2 or computer == 5:
        print('The player won!')
    elif computer == 4:
        print('It\'s a tie!')
elif player == 5:
    if computer == 1 or computer == 3:
        print('The player won!')
    elif computer == 2 or computer == 4:
        print('The computer won!')
    elif computer == 5:
        print('It\'s a tie!')