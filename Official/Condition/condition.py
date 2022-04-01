class Condition:
    def __init__(self, code):
        self.code = code

    def run(self):
        inExe = False
        exe = []
        for x in self.code:
            if x == '{':
                inExe = True
            elif x == '}':
                inExe = False
            else:
                if inExe:
                    exe.append(x)
        keywords = self.code[0]
        conditions = self.code[1:4]

        dictCondition = {
            '==': True if conditions[0] == conditions[2] else False,
            '!=': True if conditions[0] != conditions[2] else False
        }

        if keywords == 'if':
            return dictCondition.get(conditions[1]), exe
        elif keywords == 'elif':
            return dictCondition.get(conditions[1]), exe
        else:
            return True, exe
