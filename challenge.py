class programLearningBot:

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