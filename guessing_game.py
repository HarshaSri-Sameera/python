import random                                                           # Imported the random module
answer = random.randint(1, 11)
print("""RULES TO PLAY GUESSING GAME:                                   
        1) Guess a number between 1 to 10
        2) To exit the game press the number zero
        """)
print('Okay lets start! Guess any no. from 1 to 10:')
guess = int(input())
if guess == 0 or guess > 10:
            print('GAME OVER')
            print('Answer:{}'.format(answer))
else:        
    if guess == answer:                                                     # Game logic
        print("you got it first time")
        print("Excellent! you are good at guessing random numbers")
    else:
        while guess != answer:      
            if guess < answer:
                print("guess higher")
            else:
                print("guess lower")
        guess = int(input())
            if guess == 0 or guess > 10:
                print('GAME OVER')
                print('Answer:{}'.format(answer))
                break
           else:
                if guess == answer:
                    print("well done! you guessed it correctly.")
                    break
                else:
                    print("TRY AGAIN!(keep guessing)")
