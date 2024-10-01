# quiz game
GREEN = "033[032m"
RED = "033[031m"
SKY_BLUE = "033[036m"

def quiz_game():
    questions = [
                ("Which country gives you the highest package and facilities more than other countries ?"),
                ("How many continents present in the World ?"),
                ( "How many wondors in the World?"),
                ( "Which gas do we need to survive?")]
    
    options = [
               ["1. Luxembourg","2. America","3. Switzerland","4. Netherlands","5. None of these"],
               ["1. 4","2. 9","3. 8","4. 0","5. 7"],
               ["1. 5","2. 1","3. 6","4. 7","5. 9"],
               ["1. Nitrogen","2. Helium","3. Carbon dioxide","4. Oxygen","5. None of these"]  
                                              ]
    
    answers = ("1","5","4","4")
    guesses = []
    score = 0
    que_num  = 0

    for quostion in questions:
        print("==================>")
        print(quostion)
        for option in options[que_num]:
            print(option)
        guess = input("Chose your option (1,2,3,4,5): ")
        guesses.append(guess)
        if guess == answers[que_num]:
            print("\033[032mCorrect answer\033[0m")
            score += 1
        else:
            print("\033[31mIncorrect\033[0m")
            print(f"\033[36m{answers[que_num]} is the correct answer.\033[0m")
        que_num +=1  
    

    print("\n+++++++++++++++++++++++++++++++")
    print("            RESULT            ")
    print("+++++++++++++++++++++++++++++++\n")

    print("Answers: ")
    for answer in answers:
        print(answer, end=" ")
    print()    

    print("\nGuesses: ")
    for guess in guesses:
        print(guess, end=" ")
    print() 

    score = int(score)/len(questions) * 100 
    print(f"\n\033[032mYour score is {score}%\033[0m")
    
quiz_game() 