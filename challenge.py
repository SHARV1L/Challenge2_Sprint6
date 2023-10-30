class learningBot:

    def __init__(self):
        self.levels = [
            {
                "sample": "print('Hello World')",
                "error1": "prit('Hello World')"
             },
            {
                "sample": "print",
                "error2": ""
            }
        ]

        self.currentLevel = 0