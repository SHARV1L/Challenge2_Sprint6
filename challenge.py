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
            # {
            #     print(Check out for
            #     "level": ""
            # }

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

