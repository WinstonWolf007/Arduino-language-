class Output:
    def __init__(self, code, data_variable):
        self.code = code
        self.data_var: dict = data_variable

    def run(self):
        if self.code[0] == 'Output':
            if self.code[1] == '>':
                if self.data_var.get(self.code[2]):
                    print("\033[90m" + str(self.data_var.get(self.code[2])) + "\033[0m")
                else:
                    print("\033[90m" + " ".join(self.code[2:]) + "\033[0m")