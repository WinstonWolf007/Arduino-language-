from Official.Variable.var import Var
from Official.Fonction.output import Output
from Official.Condition import condition
from Official.Main.error import error


class Exe:
    def __init__(self, code):
        self.code = code
        self.data_variable = {}

    def run(self):
        for codeLine in self.code['program.main']:
            exe = {
                "Output": Output(codeLine, self.data_variable).run,
            }

            # check if this is variable
            if codeLine[0][0] == '$' and codeLine[1][0] == '=':
                var = Var(codeLine, self.data_variable)
                if var.check_error() == 200:
                    self.data_variable[codeLine[0]] = " ".join(codeLine[2:])
            elif codeLine[0] == 'if':
                cond = condition.Condition(codeLine)
                result = cond.run()
                if result[0]:
                    for codeLine2 in result[1]:
                        try:
                            if exe.get(codeLine2[0])():
                                pass
                        except:
                            pass
            else:
                try:
                    if exe.get(codeLine[0])():
                        pass
                except:
                    pass