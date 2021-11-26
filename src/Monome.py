# Monome.py

class Monome:
    def __init__(self, equation: str):
        self.equation = equation
        self.coeff = self.getCoeff()
        self.puissance = self.getPuissance()

    def __str__(self):
        return "Equation: " + self.equation

    def getCoeff(self):
        signes = '+-'
        res = self.equation[0]
        for elem in self.equation:
            if elem == 'x':
                if len(res) == 1:
                    return int(res + str(1))
                else:
                    return int(res)
            elif elem not in signes:
                res += elem
        return self.equation

    def getPuissance(self):
        res = ''
        for i in range(len(self.equation) - 1, 0, -1):
            if self.equation[i] == '^':
                return int(res[::-1])
            else:
                res += self.equation[i]
        if 'x' in self.equation:
            return 1
        else:
            return None
