class Error:
    def __init__(self, type_, line, mgs, file, code_line):
        self.eType = str(type_).split("'")[1]
        self.eLine = line
        self.eMsg = mgs
        self.eFile = file
        self.eCode = code_line

    def display(self):
        print(
            '\033[91m' +
            'Traceback (most recent call last):\n' +
            f'\tFile "{self.eFile}", line {self.eLine}\n' +
            '\033[0m' +
            f'\t\t{self.eCode}\n' +
            '\033[91m' +
            f'\t{self.eType}: {self.eMsg}' +
            '\033[0m'
        )


def error(type_, line, mgs, file, code_line):
    Error(type_, line, mgs, file, code_line).display()