# Rock Paper Scissors

## Codedex Checkpoint Project - Python

Rock, Paper, Scissors is a classic game that resonates with folks from around the world.

Create a **rock_paper_scissors.py** program where the user plays a round of Rock, Paper, Scissors with the computer.

The rules are as follows:

- Rock beats Scissors.
- Scissors beat Paper.
- Paper beats Rock.

First, create a <code>player</code> and a <code>computer</code> variable.

Prompt the player to select number between 1 and 3 with <code>input()</code> and store it in <code>player</code>:

- <code>1</code> is for <code>“✊”</code> (Rock).
- <code>2</code> is for <code>“✋”</code> (Paper).
- <code>3</code> is for <code>“✌”</code> (Scissors).

Then, use the <code>random.randint()</code> method to assign a number to the <code>computer</code> variable (1 to 3).

Lastly, use control flow to compare the user's choice and the computer's choice, determine the winner, and print out who won.

The output should look something like this:
``` console
===================
Rock Paper Scissors
===================
1) ✊
2) ✋
3) ✌️
Pick a number: 2

You chose: ✋
CPU chose: ✊
The player won!
```

## Bonus: Rock Paper Scissors Lizard Spock

Okay, you have played Rock, Paper, Scissors, but have you heard of Rock, Paper, Scissors, Lizard, Spock? It's a fun variation of the classic game brought to popularity with a TV show called The Big Bang Theory.

The rules are very similar to the ones from the classic “Rock Paper Scissors” but with two new options, “Lizard” and “Spock”:

- Scissors cut Paper.
- Paper covers Rock.
- Rock crushes Lizard.
- Lizard poisons Spock.
- Spock smashes Scissors.
- Scissors beat Lizard.
- Lizard eats Paper.
- Paper disproves Spock.
- Spock vaporizes Rock.
- Rock breaks Scissors.

Go back to your Rock Paper Scissors program and see if you can turn it into Rock Paper Scissors Lizard Spock!

Use <code>"🖖"</code> for "Spock and <code>"🦎"</code> for "Lizard".

The output should look something like this:

``` console
================================
Rock Paper Scissors Lizard Spock
================================
1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖
Pick a number: 3

You chose: ✌️
CPU chose: ✌️
It's a tie!
``` 