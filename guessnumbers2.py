print "I am thinking of a number between 1 and 10."

secretNum = 7

while True:
    myNum = int(raw_input("Whats the number?: "))
    if myNum == secretNum:
        print "Yes! You win!"
        break
    if myNum > secretNum:
        print "%d is too high" % myNum

    else:
        print "%d is too low" % myNum
        
