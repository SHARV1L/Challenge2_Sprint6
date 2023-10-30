class ProgramLearningBot:

    def __init__(self):
        self.levels = [
            # level 1: introducing typo error in print
            {
                "level": "print('Hello World')",
                "error": "prit('Hello World')"
             },
            # level 2: introducing semantic error by printing: print(10); and syntax error by ignoring ":"
            {
                "level": "for i in range(3): "
                          "print(i)",
                "error": "for i in range(3)"   
                          "print(10)"
            },
            # level 3: introducing syntax error in addition/subtraction
             {
                 "level": "sum = (12 + 78) "
                           "print(f"The sum of {num1} and {num2} is {sum}")",
                  "error": "sum = (12 + 78 "
                           "print(f"The sum of {num1} and {num2} is {sum}")"
             },
            # level 4: introducing runtime error in multiplication/division
             {
                 "level": "num1 = 10"
                           "num2 = 5"
                           "quotient = num1 / num2"
                           "print(f"The quotient of {num1} and {num2} is {quotient}")",
                 "error": "num1 = 10"
                          "num2 = 0"
                          "quotient = num1 / num2"
                          "print(f"The quotient of {num1} and {num2} is {quotient}")"
             },
            #level 5: introducing logical error in conditional statement
             {
                 "level": "time = 12"
                          "if 5 < time < 12: "
                                "print("Good Morning")"
                           "elif 12 <= time < 16: "
                                 "print("Good Afternoon")"
                            "elif 16 <= time < 19: "
                                  "print("Good Evening")"
                             "else: "
                                   "print("Good Night")",
                 "error": "time = 12"
                           "if 16 < time < 19: "  # Reversed order, which is a logical error
                                "print("Good Evening")"
                            "elif 12 < time < 16: "
                                "print("Good Afternoon")"
                             "elif 5 < time < 12: "
                                 "print("Good Morning")"
                              "else: "
                                  "print("Good Night")"
              },
             #level 6: introducing runtime, semantic and logical error in While loop
              {
                  "level": "while True: "
                                "try: "
                                    "print("This is an infinite loop!")"
                                 "except KeyboardInterrupt: "
                                     "print("Loop interrupted. Exiting...")"
                                     "break",
                  "error": "while True: "
                            # This code will run indefinitely
                                "print("This is an infinite loop!")"
              },
             #level 7: introducing logical and semantic error in Reverse a number condition
              {
                  "level": "number = 12345"
                           "reversed_number = 0"
                           "while number > 0: "
                                "digit = number % 10"
                                "reversed_number = reversed_number * 10 + digit"
                                "number = number // 10"
                            "print("Reversed number:", reversed_number)",
                  "error": "number = 12345"
                           "reversed_number = 0"
                            "while number > 0: "
                                 "number = number // 10 "
                                 "digit = number % 10 "
                                 "reversed_number = reversed_number * 10 + digit"
                            "print("Reversed number:", reversed_number)"
               },
              #level 8: introducing semantic error in Typecast
               {
                   "level": "number1 = 42"
                            "number2 = "12" "
                            "num_2 = int(num_string)"
                            "result = number1 + num_2"
                            "print("Result is :",result)",
                   "error": "number1 = 42"
                            "number2 = "12" "
                            "result = number1 + number2"
                            "print("Result is :",result)",
                },
               #level 9: introducing logical error in checking Palindrome word
                {
                    "level": "def is_palindrome(word): "
                                "return word == word[::-1]"
                              "word = "racecar" "
                              "if is_palindrome(word): "
                                   "print(f"{word} is a palindrome.")"
                              "else: "
                                   "print(f"{word} is not a palindrome.")",
                    "error": "def is_palindrome(word): "
                                "return word == word"
                              "word = "racecar" "
                              "if is_palindrome(word): "
                                    "print(f"{word} is a palindrome.")"
                              "else: "
                                    "print(f"{word} is not a palindrome.")"
                },
               #level 10: introducing logical and semantic error in Amstrong program
                {
                    "level": "def is_armstrong(number): "
                                "num_str = str(number)"
                                "num_digits = len(num_str)"
                                "sum_cubed = 0"
                                "for digit in num_str: "
                                    "sum_cubed += int(digit) ** num_digits"
                                "return number == sum_cubed"
                            "number = 153"
                            "if is_armstrong(number):"
                                "print(f"{number} is an Armstrong number.")"
                            "else: "
                                "print(f"{number} is not an Armstrong number.")",
                    "error": "def is_armstrong(number): "
                                "num_str = str(number)"
                                "num_digits = len(num_str)"
                                "sum_cubed = 0"
                                "for digit in num_str:"
                                    "sum_cubed += int(digit) * num_digits"
                                "return number == sum_cubed"
                             "number = 153"
                             "if is_armstrong(number): "
                                 "print(f"{number} is an Armstrong number.")"
                             "else: "
                                 "print(f"{number} is not an Armstrong number.")"
                },
               #level 11: introducing an error in writing initials
                {
                    "level": "def get_initials(name): "
                                "name_parts = name.split()"
                                "initials = "" "
                                "for part in name_parts: "
                                    "initials += part[0].upper() "
                                "return initials"
                             "name = "John Doe" "
                             "initials = get_initials(name) "
                             "print(f"The initials of {name} are {initials}")",
                    "error": "def get_initials(name): "
                                "name_parts = name.split()"
                                "initials = "" "
                                "for part in name_parts: "
                                    "initials = part[0]"
                                "return initials"
                                "name = "John Doe" "
                                "initials = get_initials(name)"
                                "print(f"The initials of {name} are {initials}")"
                 },
                #level 12: Finding number of words/spaces
                 {
                     "level": "def count_words_and_spaces(sentence): "
                                    "num_words = len(sentence.split())"
                                    "num_spaces = sentence.count(' ')"
                                    "return num_words, num_spaces"

                                "sentence = "This is an example sentence with spaces."
                                "num_words, num_spaces = count_words_and_spaces(sentence)"
                                "print(f"Number of words: {num_words}")"
                                "print(f"Number of spaces: {num_spaces}")",
                    "error": "def count_words_and_spaces(sentence): "
                                    "num_words = len(sentence.split())"
                                    "num_spaces = sentence.count(' ')"
                                    "return num_words, num_spaces"

                             "sentence = "This is an example sentence with spaces."
                             "num_words, num_spaces = count_words_and_spaces(sentence)"
                             "print(f"Number of words: {num_words}")"
                             "print(f"Number of spaces: {num_spaces}")"
                 }
        ]

        self.currentLevel = 0

    def get_current_challenge(self):
        if self.currentLevel < len(self.levels):
            return self.levels[self.currentLevel]['error']
        return "Congratulations! You've completed all the challenges."

    def submit_solution(self, solution):
        correct_solution = self.levels[self.currentLevel]['level']
        if solution == correct_solution:
            self.currentLevel += 1
            return "Correct! Moving to next challenge."
        else:
            return "Incorrect. Try again!"

    def get_solution_hint(self):
        return self.levels[self.currentLevel]['level']

def runChallenge():
    bot = ProgramLearningBot()

    while True:
        print("\nChallenge:", bot.get_current_challenge())
        solution = input("Enter your solution (or type 'next'/'prev' to toggle levels, 'exit' to quit): ")

        ######################################
        if solution.lower() in ["exit", "quit"]:
            print("Exiting the challenge. Goodbye!")
            break
        elif solution.lower() == "next":
            print("You can't move to the next challenge until you complete the current one!")
            continue
        elif solution.lower() == "prev":
            if bot.currentLevel > 0:
                bot.currentLevel -= 1
                print("Moved to the previous challenge.")
                continue
            else:
                print("You're at the first challenge.")
                continue
        ########################################

        feedback = bot.submit_solution(solution)
        print(feedback)

        if feedback == "Correct! Moving to next challenge.":
            # Automatically move to the next challenge after the correct solution
            if bot.currentLevel < len(bot.levels) - 1:
                bot.currentLevel += 1
                print("Moved to the next challenge.")
            elif feedback == "Congratulations! You've completed all the challenges.":
                break

if __name__ == "__main__":
    runChallenge()

