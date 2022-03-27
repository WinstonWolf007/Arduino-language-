class Adn:
    def __init__(self, code):
        self.line = 0
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

    def transform_hug_code_to_dict(self):
        return []

    def run(self):
        self.code = self.cleans_code_comment()
        self.code = self.cleans_code_string()
        self.code = self.transform_hug_code_to_dict()
