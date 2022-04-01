class Cleans:
    def __init__(self, code):
        self.code = code

    def cleans_code_comment(self):
        new_code = []
        block_comment = False
        for x, char in enumerate(self.code):
            char = char.split()
            if char:
                if char[0][0] == '#':
                    pass
                elif char[0][0:2] == '/"':
                    block_comment = True
                    if char[-1][-3:-1] == '"/':
                        block_comment = False
                elif char[0][0:2] == '"/':
                    block_comment = False
                elif not block_comment:
                    new_code.append(" ".join(char))
        return new_code

    def cleans_code_string(self):
        new_code = []
        for i in self.code:
            code = i.split('"')
            code2 = i.split()
            all_code_line = []
            all_string = []
            idx = 0

            for x, char in enumerate(code):
                if (x % 2) == 1:
                    all_string.append(f'"{char}"')

            in_string = False
            for y in code2:
                if y[0] == '"' and len(y) > 1:
                    in_string = True
                    all_code_line.append(all_string[idx])
                    idx += 1
                    if y[-1] == '"':
                        in_string = False
                elif y[-1] == '"':
                    in_string = False
                elif not in_string:
                    all_code_line.append(y)

            new_code.append(all_code_line)
        return new_code

    def pick_main_code_and_package_code(self):
        new_code = {'package': [], 'program.main': []}
        for y, x in enumerate(self.code):
            if x[0] in ['from', 'include']:
                new_code['package'].append(x)
            elif x[0] == "program.main":
                if x[-1] == '{' or (y < len(self.code)-1 and self.code[y + 1][0] == '{'):
                    code2 = self.code
                    code2.reverse()
                    for m, n in enumerate(code2):
                        if n[-1] == '}' or (m < len(self.code)-1 and self.code[m - 1][0] == '}'):
                            pos = len(self.code)-m
                            code2.reverse()
                            break
                    else:
                        # error it missing '{' (to ends)
                        pass
                    new_code['program.main'] = [x for x in self.code[y+1:pos-1]]
                else:
                    # Error: it missing '{' (to start)
                    pass
        return new_code

    def separate_accolade_to_keyword(self):
        all_code = []
        if self.code['program.main'][0][0] == '{':
            self.code['program.main'] = self.code['program.main'][1:]

        for x in self.code['program.main']:
            if '{' in x or '}' in x:
                if len(x) > 1 and x[0] in ['{', '}'] and x[-1] in ['{', '}']:
                    all_code.append(x[0])
                    all_code.append(x[1:-1])
                    all_code.append([x[-1]])
                elif len(x) == 1 and x[0] in ['{', '}']:
                    all_code.append(x[0])
                elif len(x) > 1 and x[0] in ["{", '}']:
                    all_code.append(x[0])
                    all_code.append(x[1:])
                elif len(x) > 1 and x[-1] in ["{", '}']:
                    all_code.append(x[:-1])
                    all_code.append(x[-1])
            else:
                all_code.append(x)
        self.code['program.main'] = all_code
        return self.code

    def create_dict_with_keyword(self):
        new_code = {}
        codes = {'keyword': '', 'code': []}
        in_func = False

        for y, x in enumerate(self.code['program.main']):
            if x[0] in ['if', 'elif', 'else']:
                in_func = True
            elif x == '}' and in_func:
                new_code[" ".join(codes['keyword'])] = codes['code']
                codes = {'keyword': '', 'code': []}
                in_func = False
            elif x == '{' and in_func:
                codes['keyword'] = self.code['program.main'][y-1]
            elif in_func:
                codes['code'].append(x)
            else:
                new_code[" ".join(x)] = ''

        self.code['program.main'] = new_code
        return self.code

    def run(self):
        self.code = self.cleans_code_comment()
        self.code = self.cleans_code_string()
        self.code = self.pick_main_code_and_package_code()
        self.code = self.separate_accolade_to_keyword()
        self.code = self.create_dict_with_keyword()
        return self.code
