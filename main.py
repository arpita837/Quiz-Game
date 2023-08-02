class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question, choices, correct_choice):
        self.questions.append({
            'question': question,
            'choices': choices,
            'correct_choice': correct_choice
        })
        print("Question added successfully!")

    def take_quiz(self):
        if not self.questions:
            print("No questions available in the quiz.")
            return

        score = 0
        total_questions = len(self.questions)

        print(f"\n--- Quiz ({total_questions} Questions) ---")

        for idx, q in enumerate(self.questions, start=1):
            print(f"\nQuestion {idx}: {q['question']}")
            for choice_num, choice in enumerate(q['choices'], start=1):
                print(f"{choice_num}. {choice}")

            user_choice = int(input("Enter your choice (1-4): ")) - 1

            if 0 <= user_choice < len(q['choices']):
                if user_choice == q['correct_choice']:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is: {q['choices'][q['correct_choice']]}\n")

        print(f"\n--- Quiz Results ---")
        print(f"Total Questions: {total_questions}")
        print(f"Correct Answers: {score}")
        print(f"Your Score: {score}/{total_questions}")

def main():
    quiz = Quiz()

    while True:
        print("\n--- Quiz Application Menu ---")
        print("1. Add a question to the quiz")
        print("2. Take the quiz")
        print("3. Exit")

        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            question = input("Enter the question: ")
            choices = [input(f"Enter choice {i}: ") for i in range(1, 5)]
            correct_choice = int(input("Enter the correct choice (1-4): ")) - 1
            quiz.add_question(question, choices, correct_choice)

        elif choice == 2:
            quiz.take_quiz()

        elif choice == 3:
            print("Exiting the Quiz Application.")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
