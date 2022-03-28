from Official.Main.mathematic import Math


class Output:
    def __init__(self, code, data_variable):
        self.code = code
        self.data_var: dict = data_variable

    def run(self):
        if self.code[0] == 'Output':
            if self.code[1] == '>':
                if self.code[2][0] == '"' and self.code[-1][-1] == '"':
                    print("\033[90m" + str(self.code[2]).replace('"', '') + "\033[0m")
                elif self.data_var.get(self.code[2]) and len(self.code[2:]) == 1:
                    print("\033[90m" + str(self.data_var.get(self.code[2])).replace('"', '') + "\033[0m")
                else:
                    maths = Math(" ".join(self.code[2:]).replace('"', ''), self.data_var)
                    print("\033[90m" + maths.run() + "\033[0m")