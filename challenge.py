class learningBot:

    def __init__(self):
        self.levels = [
            {
                # introducing typo error in print
                "level1": "print('Hello World')",
                "error1": "prit('Hello World')"
             },
            {
                # introducing semantic error by printing: print(10); and syntax error by ignoring "."
                "level2": "for i in range(3): "
                          "print(i)",
                "error2": "for i in range(3)"   
                          "print(10)"
            }
        ]

        self.currentLevel = 0