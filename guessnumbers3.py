import random



def guessingGame():
    my_random_number = random.randint(1, 20)

    guess = 5

    while guess > 0:

            guess -= 1
            myNum = int(raw_input("Whats the number?: "))
            if myNum == my_random_number:
                print "Yes! You win!"
                break
            if myNum > my_random_number:
                print "%d is too high" % myNum
                print "You have %d guesses left" % guess

            else:
                print "%d is too low" % myNum
                print "You have %d guesses left" % guess

    print "You're out of guesses!"
    print "Would you like to play again (Y or N)? "

    again = raw_input().upper()

    if again == "Y":
        guessingGame()
    else:
        print "Bye!"

guessingGame()
