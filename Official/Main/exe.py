from Official.Variable.var import Var
from Official.Fonction.output import Output
from Official.Condition import condition

"""
include "string" => class
from "json" include "openFile" => function
"""


class Exe:
    def __init__(self, code):
        self.code = code
        self.data_variable = {}

    def run(self):
        for i, codeLine in enumerate(self.code):
            if codeLine[0] == 'include':
                if len(codeLine) == 2:
                    self.data_variable['$'+str(codeLine[1]).replace('"', '')] = {'package': [str(codeLine[1]).replace('"', '')+'.adn', 'all']}
                else:
                    # error
                    pass
            elif codeLine[0] == 'from':
                if len(codeLine) == 4:
                    self.data_variable['$'+str(codeLine[3]).replace('"', '')] = {'package': [str(codeLine[1]).replace('"', '')+'.adn', codeLine[3].replace('"', '')]}
                else:
                    # error
                    pass
            elif codeLine[0] == 'program.script':
                for line in self.code[i:]:
                    if line[0] == 'Output':
                        if len(line) > 2:
                            if line[2][0] == '$':
                                print(self.data_variable[line[2]])
                            else:
                                print(line[2])