txt = "Welcome to my quiz game."

print("+" * len(txt), "\n")
print("Welcome to computer quiz game.", "\n")
print("+" * len(txt), "\n")

def quiz():
    question_with_answers = {
        "qu1": {
            "question": "Who wrote the famous play 'Romeo and Juliet'?",
            "answer": "William Shakespeare"
        },
        "qu2": {
            "question": "What is the capital of Japan?",
            "answer": "Tokyo"
        },
        "qu3": {
            "question": "Who was the first person to walk on the moon?",
            "answer": "Neil Armstrong"
        },
        "qu4": {
            "question": "What is the largest ocean on Earth?",
            "answer": "Pacific Ocean"
        },
        "qu5": {
            "question": "What is the chemical symbol for oxygen?",
            "answer": "O2"
        }
    }

    score = 0  # Define the score outside the loop
    for i in range(len(question_with_answers)):
        # Load key
        key = "qu" + str(i + 1)
                
        # Load question
        _q = input(question_with_answers[key]["question"] + "\n")
        
        # Check the answers
        if _q == question_with_answers[key]["answer"]:
            print("Correct answer")
            score += 1
        else:
            print("Incorrect answer")

    print("The quiz has ended")
    print("Your score is", score * 10)

    if score == 5:
        print("Successfully passed all questions\n\tCongrats! :)")
    else:
        print("You are not passed. :(")

    return score == 5

def start_quiz():
    while True:
        passed = quiz()  # Run the quiz

        if not passed:  # If the user did not pass all questions
            retry = input("Do you want to retake the quiz? (yes/no): ").strip().lower()
            
            if retry[0] != "y":  
                print("Thank you for playing!")
                break  # Exit the loop if the user doesn't want to retake
        else:
            print("Thank you for playing!")
            break  # Exit if the user passed all questions

start_quiz()  # Start the quiz when the program runs
