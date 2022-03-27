new_code['package'] = all_code
all_code = []

if x[-1] == '{' or (y < len(self.code) and self.code[y + 1][0] == '{'):
    for i, j in enumerate(self.code[y:]):
        if j[0] == 'program.main':
            in_main = True
            if j[0] == '}' or j[-1] == '}':
                in_main = False
        elif j[0] == '}' or j[-1] == '}':
            in_main = False
        elif in_main:
            all_code.append(j)
    new_code['program.main'] = all_code
    all_code = []
    # print(new_code['program.main'])

    for z, q in enumerate(new_code['program.main']):
        if q[0] in ['if', 'elif', 'else', 'for', 'while']:
            if q[-1] == '{' or (z < len(new_code['program.main']) and new_code['program.main'][z + 1] == '{'):
                print("'{'")