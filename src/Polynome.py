# Polynome.py

from Monome import *


class Polynome:
    def __init__(self, equation: str):
        self.equation = equation

        self.puissancesEtCoeffs = {}

        self.monomes = ()
        self.racineEvidente = 0
        self.polynomeFactorise = ''

        self.horner()

    def resetVal(self):
        self.monomes = ()
        self.puissancesEtCoeffs = {}
        self.racineEvidente = 0

    def afficheMonomes(self):
        print("Les monômes sont: ", end='')
        for monome in self.monomes:
            print(monome, end=', ')
        print()

    def affichePuissanceEtCoeff(self):
        print("Les puissances et les coeffs: ", self.puissancesEtCoeffs)

    def trouvePuissancesEtCoeff(self):
        for monome in self.monomes:
            self.puissancesEtCoeffs[monome.puissance] = monome.coeff
        self.affichePuissanceEtCoeff()

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

    def isSecondDegre(self):
        for puissance in self.puissancesEtCoeffs.keys():
            if puissance is not None and puissance > 2:
                return False
        return True

    def trouveDegre(self):
        plusGrand = self.monomes[0].puissance
        for monome in self.monomes:
            if monome.puissance is not None and monome.puissance > plusGrand:
                plusGrand = monome.puissance
        return plusGrand

    def standardise(self):
        degre = self.trouveDegre()
        for i in range(degre, 1, -1):
            if i not in self.puissancesEtCoeffs.keys():
                self.puissancesEtCoeffs[i] = 0

    def trouveRacineEvidente(self):
        """Trouve une racine évidente"""
        coeffs = tuple(self.puissancesEtCoeffs.values())
        puissances = tuple(self.puissancesEtCoeffs.keys())

        equation = ''
        for i in range(len(self.monomes)):
            if puissances[i] is not None:
                if coeffs[i] > 0:
                    equation += '+' + str(coeffs[i]) + 'x^' + str(puissances[i])
                else:
                    equation += str(coeffs[i]) + 'x^' + str(puissances[i])
            else:
                equation += str(coeffs[i])
        for i in range(0, 100):
            equa = equation.replace('x', "*(" + str(i) + ')').replace('^', '**')
            resEqua = eval(equa)
            if resEqua == 0:
                self.racineEvidente = i
                break
        print("La racine évidente trouvée est: ", self.racineEvidente)

    def resolutionSecondDegre(self):
        a = self.puissancesEtCoeffs[2]
        b = self.puissancesEtCoeffs[1]
        c = self.puissancesEtCoeffs[None]
        delta = ((b ** 2) - (4 * a * c))

        print("Delta vaut: ", delta)

        if delta == 0:
            x0 = -b / (2 * a)
            self.polynomeFactorise += str(a) + '(x' + str(-x0) + ')'
        elif delta < 0:
            self.polynomeFactorise += '(' + self.equation + ')'
        else:
            x1 = (-b - (delta ** 0.5)) / (2 * a)
            x2 = (-b + (delta ** 0.5)) / (2 * a)
            self.polynomeFactorise += str(a) + '(x + ' + str(-x1) + ')' + '(x + ' + str(-x2) + ')'

    def coeffsToEqua(self, coeffs):
        # TODO à réécrire pour le passage au dico
        puissances = tuple(self.puissancesEtCoeffs.keys())
        res = ''
        for i in range(len(coeffs) - 1):
            if coeffs[i] < 0:
                if coeffs[i] != 0:
                    try:
                        if int(puissances[i]) - 1 != 0:
                            res += str(coeffs[i]) + 'x^' + str(int(puissances[i]) - 1)
                        else:
                            res += str(coeffs[i])
                    except TypeError:
                        res += str(coeffs[i])
            else:
                if coeffs[i] != 0:
                    try:
                        if int(puissances[i]) - 1 != 0:
                            res += '+' + str(coeffs[i]) + 'x^' + str(int(puissances[i]) - 1)
                        else:
                            res += '+' + str(coeffs[i])
                    except TypeError:
                        res += '+' + str(coeffs[i])
        self.equation = res

    def horner(self):
        while True:
            print("L'équation est: ", self.equation)
            self.resetVal()
            self.trouveMonomes()
            self.trouvePuissancesEtCoeff()

            self.standardise()

            if self.isSecondDegre():
                break

            coeffs = tuple(self.puissancesEtCoeffs.values())
            self.trouveRacineEvidente()

            # TODO à réécrire pour le passage au dico

            res = ()
            for i in range(len(coeffs)):
                coeff = coeffs[i]
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
