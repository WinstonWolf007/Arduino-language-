class Error:
    def __init__(self, type_, mgs, code_line):
        self.eType = str(type_).split("'")[1]
        self.eMsg = mgs
        self.eCode = code_line

    def display(self):
        print(
            '\033[91m' +
            'Traceback (most recent call last):\n' +
            '\033[0m' +
            f'\t\t{self.eCode}\n' +
            '\033[91m' +
            f'\t{self.eType}: {self.eMsg}' +
            '\033[0m'
        )


def error(type_, line, mgs):
    Error(type_, mgs, line).display()
    exit()
