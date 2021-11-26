# Polynome.py

from Monome import*

class Polynome:
    def __init__(self, equation: str):
        self.equation = equation
        self.monomes = ()
        self.coeffs = ()
        self.puissances = ()
        self.racineEvidente = 0
        self.polynomeFactorise = ''

        self.horner()

    def resetVal(self):
        self.monomes = ()
        self.coeffs = ()
        self.puissances = ()
        self.racineEvidente = 0

    def afficheMonomes(self):
        print("Les monômes sont: ")
        for monome in self.monomes:
            print(monome, end=', ')
        print()

    def afficheCoeffs(self):
        print("Les coefficients sont: ")
        for monome in self.monomes:
            print(monome.coeff, end=', ')
        print()

    def affichePuissances(self):
        print("Les puissances sont: ")
        for monome in self.monomes:
            print(monome.puissance, end=', ')
        print()

    def trouveMonomes(self):
        """Cherche les monômes de l'équation"""
        separateurs = "+-"
        aAjouter = ''

        for elem in self.equation:
            if elem in separateurs:
                if len(aAjouter) == 0:
                    aAjouter += elem
                elif aAjouter != '':
                    self.monomes += Monome(aAjouter),
                    aAjouter = elem
            else:
                aAjouter += elem
        self.monomes += Monome(aAjouter),
        self.afficheMonomes()

    def trouveCoeffs(self):
        """Cherche les coefficients pour chaque monôme"""
        for monome in self.monomes:
            self.coeffs += monome.coeff,
        self.afficheCoeffs()

    def trouvePuissances(self):
        for monome in self.monomes:
            if monome.puissance is not None:
                self.puissances += monome.puissance,
        self.affichePuissances()

    def isStandard(self):
        if len(self.puissances) != len(self.monomes):
            return False
        else:
            pass

    def standardise(self):
        for i in range(len(self.monomes), 0, -1):
            pass

    def trouveRacineEvidente(self):
        """Trouve une racine évidente"""
        equation = ''
        for i in range(len(self.monomes)):
            try:
                if self.coeffs[i] > 0:
                    equation += '+' + str(self.coeffs[i]) + 'x^' + str(self.puissances[i])
                else:
                    equation += str(self.coeffs[i]) + 'x^' + str(self.puissances[i])
            except IndexError:
                equation += str(self.coeffs[i])
        for i in range(0, 100):
            equa = equation.replace('x', "*(" + str(i) + ')').replace('^', '**')
            resEqua = eval(equa)
            if resEqua == 0:
                self.racineEvidente = i
                break
        print("La racine évidente trouvée est: ", self.racineEvidente)

    def resolutionSecondDegre(self):
        try:
            a = self.coeffs[0]
        except IndexError:
            a = 0
        try:
            b = self.coeffs[1]
        except IndexError:
            b = 0
        try:
            c = self.coeffs[2]
        except IndexError:
            c = 0
        delta = ((b**2) - (4*a*c))

        print("Delta vaut: ", delta)

        if delta == 0:
            x0 = -b/(2 * a)
            self.polynomeFactorise += str(a) + '(x' + str(-x0) + ')'
        elif delta < 0:
            self.polynomeFactorise += '(' + self.equation + ')'
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            self.polynomeFactorise += str(a) + '(x + ' + str(-x1) + ')' + '(x + ' + str(-x2) + ')'

    def coeffsToEqua(self, coeffs):
        res = ''
        for i in range(len(coeffs)):
            try:
                if coeffs[i] < 0:
                    if coeffs[i] != 0:
                        if int(self.puissances[i])-1 != 0:
                            res += str(coeffs[i]) + 'x^' + str(int(self.puissances[i])-1)
                        else:
                            res += str(coeffs[i])
                else:
                    if coeffs[i] != 0:
                        if int(self.puissances[i])-1 != 0:
                            res += '+' + str(coeffs[i]) + 'x^' + str(int(self.puissances[i])-1)
                        else:
                            res += '+' + str(coeffs[i])
            except IndexError:
                pass
        self.equation = res

    def horner(self):
        while True:
            print("L'équation est: ", self.equation)
            self.resetVal()
            self.trouveMonomes()
            self.trouvePuissances()
            self.standardise()
            self.trouveCoeffs()  # TODO mettre sous forme standard avant ça
            if max(self.puissances) == 2:
                break

            self.trouveRacineEvidente()

            res = ()
            for i in range(len(self.coeffs)):
                coeff = self.coeffs[i]
                if i == 0:
                    res += coeff,
                else:
                    mult = self.racineEvidente * res[-1]
                    add = mult + coeff
                    res += add,
            print("Après un passage par le tableau, on trouve ces coefficients là: ", res)
            self.polynomeFactorise += str('(x + ' + str(-int(self.racineEvidente)) + ')')
            self.coeffsToEqua(res)

        self.resolutionSecondDegre()
        print("Le polynôme factorisé est: ", self.polynomeFactorise)
