print("Escape the Quiz Dungeon!!")
print("You are in a dark room with two doors. Do you go through door #1 or door #2?")

door = input(">")
score = 0
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("To survive you will have to answer a few questions correctly.")
    print("question 1: What is the capital of France?")
    print("1. Paris")
    print("2. London")
    print("3. Berlin")
    ans1 = input(">")
    
    if ans1 == "1":
        print("Correct! You may proceed.")
        score += 1
    else:
        print("Wrong! The bear eats you. Good job!")
        print("Your score is: ", score)
        exit(0)

    print("question 2: What is the capital of Germany?")
    print("1. Paris")           
    print("2. London")
    print("3. Berlin")
    
    ans2 = input(">")
    if ans2 == "3":
        print("Correct! You got silent boots and may proceed.")
        score += 1
    else:
        print("Wrong! The bear eats you. Good job!")
        print("Your score is: ", score)
        exit(0)

if door == "2":
    print("You find yourself in a room full of snakes.")
    print("To survive you will have to answer a few questions correctly.")
    print("question 1: What is the capital of India?")
    print("1. New Delhi")
    print("2. Mumbai")
    print("3. Guwahati")
    
    ans1 = input(">")
    
    if ans1 == "1":
        print("Correct! You may proceed.")
        score += 1
    else:
        print("Wrong! The snakes eat you. Good job!")
        print ("Your score is: ", score)
        exit(0) 

    print("question 2: What is the capital of switzerland?")
    print("1. Paris")           
    print("2. Zurich")
    print("3. Bern")

    ans2 = input(">")
    if ans2 == "3":
        print("Correct! You got flying boots and may proceed.")
        score += 1
    else:
        print("Wrong! The snakes eat you. Good job!")
        print ("Your score is: ", score)
        exit(0)

print("You have successfully escaped the quiz dungeon!")
print("Your score is: ", score)       
    
