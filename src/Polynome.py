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
        puissances = tuple(self.puissancesEtCoeffs)
        res = puissances[0]
        for elem in puissances:
            try:
                if int(elem) > res:
                    res = int(elem)
            except TypeError:
                pass
        return res

    def standardise(self):
        degre = self.trouveDegre()
        for i in range(degre, 1, -1):
            if i not in self.puissancesEtCoeffs.keys():
                self.puissancesEtCoeffs[i] = 0
                print(i, "n'est pas présent, rajout.\nLe dico maintenant: ", self.puissancesEtCoeffs)

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
        for i in range(-1000, 1000):
            equa = equation.replace('x', "*(" + str(i) + ')').replace('^', '**')
            resEqua = eval(equa)
            if resEqua == 0:
                self.racineEvidente = i
                break
        print("La racine évidente trouvée est: ", self.racineEvidente)

    def resolutionSecondDegre(self):
        abc = ()
        print(self.puissancesEtCoeffs)
        for i in range(2, -1, -1):
            try:
                if i != 0:
                    abc += self.puissancesEtCoeffs[i],
                else:
                    abc += self.puissancesEtCoeffs[None],
            except KeyError:
                abc += 0,
        a = abc[0]
        b = abc[1]
        c = abc[2]
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

    def puissancesEtCoeffs2Equa(self):
        equa = ''
        for puissance in self.puissancesEtCoeffs:
            if puissance is None:
                if self.puissancesEtCoeffs[puissance] > 0:
                    equa += '+' + str(self.puissancesEtCoeffs[None])
                else:
                    equa += str(self.puissancesEtCoeffs[None])
            else:
                equa += str(self.puissancesEtCoeffs[puissance]) + 'x^' + str(puissance)
        self.equation = equa

    def horner(self):
        while True:
            if self.equation != '':
                print("L'équation est: ", self.equation)
                self.trouveMonomes()
                self.trouvePuissancesEtCoeff()
                self.standardise()

            if self.isSecondDegre():
                break

            self.trouveRacineEvidente()

            res = {}
            for i in range(self.trouveDegre(), 0, -1):
                puissance = i
                coeff = self.puissancesEtCoeffs[puissance]
                if puissance == self.trouveDegre():
                    res[puissance - 1] = coeff
                else:
                    mult = self.racineEvidente * res[i]
                    add = mult + coeff
                    if i - 1 != 0:
                        res[i - 1] = add
                    else:
                        res[None] = add

            print("Après un passage par le tableau, on trouve ces coefficients là: ", res)
            self.polynomeFactorise += str('(x + ' + str(-int(self.racineEvidente)) + ')')
            self.puissancesEtCoeffs = res
            self.equation = ''

        self.puissancesEtCoeffs2Equa()
        self.resolutionSecondDegre()
        print("Le polynôme factorisé est: ", self.polynomeFactorise)
