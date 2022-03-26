import string


class Function:
    def __init__(self, code: str) -> None:
        code = code.split()
        self.keyword = code[0]
        self.funcName = code[1]
        self.param_end = code[2:]

    def exe(self):
        if self.keyword == 'Function:':
            if self.funcName[0] == '$':
                for letter in self.funcName[1:]:
                    if letter not in string.ascii_letters+'_':
                        break
                else:
                    in_param = False
                    all_param = []
                    for x in self.param_end:
                        if x[0] == '<':
                            in_param = True
                        if in_param:
                            all_param.append(x.replace('<', '').replace('>', '').replace(',', '').replace(' ', ''))

                        if x[-1] == '>':
                            in_param = False
                            break

                    if self.param_end[-1] == '=>':
                        dataList = []
                        data = ""
                        while data != "endf":
                            data = input("...    ")
                            dataList.append(data)
        else:
            pass


code = "Function $length <$list $name $array> =>"
while True:
    code = input('>>> ')
    func = Function(code)
    func.exe()
