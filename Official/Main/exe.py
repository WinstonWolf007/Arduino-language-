from Official.Variable.var import Var
from Official.Fonction.output import Output


class Exe:
    def __init__(self, code):
        self.code = code
        self.data_variable = {}

    def run(self):
        for codeLine in self.code['program.main']:
            exe = {
                "Output": Output(codeLine, self.data_variable).run
            }

            # check if this is variable
            if codeLine[0][0] == '$' and codeLine[1][0] == '=':
                var = Var(codeLine)
                if var.check_error() == 200:
                    self.data_variable[codeLine[0]] = " ".join(codeLine[2:])
            else:
                if exe.get(codeLine[0])():
                    pass