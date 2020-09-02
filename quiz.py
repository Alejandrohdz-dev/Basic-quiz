import os

play = True
while play:
    os.system('cls')
    score = 0
    print("Welcome to Quiz 1.0")
    print("-------------------")
    def q1():
        print("1. What mean the python's logo?")
        print("a) Two 'S' letter")
        print("b) Two snakes")
        print("c) A bird")

        answer = str(input("What's the right answer: "))
        global score

        if answer == "b":
            print("Correct answer!!")
            score += 1
        else: 
            print("Wrong")
        
        input("Press Enter to continue to the second question...")
        os.system('cls')
        q2()

    def q2():
        print("2. What is Django?")
        print("a) A framework")
        print("b) A library")
        print("c) A language")

        answer2 = str(input("What's the right answer: "))
        global score

        if answer2 == "a":
            print("Correct")
            score += 1
        else: 
            print("Wrong")

        input("Press Enter to continue to the third question...")
        os.system('cls')
        q3()

    def q3():
        print("3. What is Python?")
        print("a) A framework")
        print("b) A library")
        print("c) A language")

        answer3 = str(input("What's the right answer: "))
        global score

        if answer3 == "c":
            print("Correct answer!!")
            score += 1
            print("Your final score is: ", score)
        else: 
            print("Wrong answer")
            print("Your final score is: ", score)

    q1()

    again = (str(input("Do you Want to play again?(yes/no)\n")))
    if again == "no":
        play = False
        print("Thank you for play")
    


