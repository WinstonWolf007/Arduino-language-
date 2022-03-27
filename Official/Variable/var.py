from Official.Main.error import error
import string


class Var:
    def __init__(self, code):
        self.code = code

    def check_error(self):
        # check each letter in variable name
        for letter in self.code[0][1:]:
            if letter not in string.ascii_letters+'_':
                error(SyntaxError, " ".join(self.code), f"Invalid character in variable name '{letter}'")

        # check good type in variable value (string, int, list, float, bool)
        try:
            if self.code[2] in ['true', 'false']:
                pass
            elif self.code[2][0] == '[' and self.code[-1][-1] == ']':
                all_element = "".join(self.code[2:]).replace('[', '').replace(']', '').split(",")
            elif self.code[2][0] == '"' and self.code[2][-1] == '"':
                pass
            elif str(self.code[2]).isdigit() or str(self.code[2]).split('.')[1] == len(str(self.code[2]).split('.')[1])*'0':
                pass
            elif str(self.code[2]).split('.')[1] != len(str(self.code[2]).split('.')[1])*'0':
                pass
            else:
                error(TypeError, " ".join(self.code), f"Not good type, the types is (string, int, list, float, bool)")
        except:
            error(TypeError, " ".join(self.code), f"Not good type, the types is (string, int, list, float, bool)")
        return 200

