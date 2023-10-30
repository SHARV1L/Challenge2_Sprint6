class ProgrammingLearningBot:

    def __init__(self):
        self.levels = [
            {"task": "print('Hello World')", "error": "prit('Hello World')"},
            {"task": "for i in range(3): print(i)", "error": "for i in range(3) print(i)"},
            {"task": "def add(a, b): return a + b", "error": "def add(a, b) return a + b"},
            {"task": "if x > 10: print('Big')", "error": "if x > 10 print('Big')"},
            {"task": "data = {'key': 'value'}; print(data['key'])", "error": "data = {'key': 'value'}; print(data[key])"},
            {"task": "lst = [1,2,3]; print(lst[2])", "error": "lst = [1,2,3]; print(lst[3])"},
            {"task": "while x < 5: x += 1", "error": "while x < 5 x += 1"},
            {"task": "import math; print(math.sqrt(16))", "error": "import math; print(math.sqroot(16))"},
            {"task": "def greet(): return 'Hello'", "error": "def greet(): return Hello"},
            {"task": "for i in [1,2,3]: print(i)", "error": "for i in (1,2,3): print(i)"}
        ]
        self.current_level = 0

    def get_current_challenge(self):
        if self.current_level < len(self.levels):
            return self.levels[self.current_level]['error']
        return "Congratulations! You've completed all the challenges."

    def submit_solution(self, solution):
        correct_solution = self.levels[self.current_level]['task']
        if solution == correct_solution:
            self.current_level += 1
            return "Correct! Moving to next challenge."
        else:
            return "Incorrect. Try again!"

    def get_solution_hint(self):
        return self.levels[self.current_level]['task']

# Usage:

bot = ProgrammingLearningBot()
print("Welcome to the Programming Learning Bot!")
print("Here's your first challenge:")

while True:
    print("\nChallenge:", bot.get_current_challenge())
    solution = input("Enter your solution: ")
    feedback = bot.submit_solution(solution)
    print(feedback)
    if feedback == "Congratulations! You've completed all the challenges.":
        break