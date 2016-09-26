print "I am thinking of a number between 1 and 10."

myNum = int(raw_input("Whats the number?: "))

secretNum = 7

while True:
    if myNum == secretNum:
        print "Yes! You win!"
        break
    else:
        print "Nope, try again."
        myNum = int(raw_input("> "))


#another way shorter way

while True:
    guess = int(raw_input("what is your guess?? ")
    if guess == secret_number:
        break
    print "Nope, try again."

print "Yes! You win!"
