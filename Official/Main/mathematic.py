from Official.Main.error import error

class Math:
    def __init__(self, calcul: str, data_variable):
        self.calcul = calcul
        self.calcul2 = calcul
        self.var = data_variable

    def join_num(self):
        strings = ""
        calcul = []
        for x in self.calcul:
            if x in ['+', '-', '*', '/']:
                calcul.append(strings.replace(" ", ""))
                calcul.append(x)
                strings = ""
            else:
                strings += x
        else:
            calcul.append(strings.replace(" ", ""))
        return calcul

    def priority_operation(self):
        calcul = ""
        fist = True
        for m, n in enumerate(self.calcul):
            if self.var.get(n):
                self.calcul[m] = self.var.get(n)

        try:
            for y, x in enumerate(self.calcul):
                if x == '*':
                    if fist: calcul += str(int(self.calcul[y-1]) * int(self.calcul[y+1]))
                    else: calcul = str(int(calcul) * int(self.calcul[y+1]))
                    fist = False
                elif x == "+":
                    if fist: calcul += str(int(self.calcul[y-1]) + int(self.calcul[y+1]))
                    else: calcul = str(int(calcul) + int(self.calcul[y+1]))
                    fist = False
                elif x == "/":
                    if fist: calcul += str(int(self.calcul[y-1]) / int(self.calcul[y+1]))
                    else: calcul = str(int(calcul) / int(self.calcul[y+1]))
                    fist = False
                elif x == "-":
                    if fist: calcul += str(int(self.calcul[y-1]) - int(self.calcul[y+1]))
                    else: calcul = str(int(calcul) - int(self.calcul[y+1]))
                    fist = False
        except:
            error(TypeError, self.calcul2, 'use int for the operation')

        return calcul

    def run(self):
        self.calcul = self.join_num()
        return self.priority_operation()