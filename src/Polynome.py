# Polynome.py

class Polynome:
    def __init__(self, equation: str):
        self.equation = equation
        self.monomes = ()
        self.coeffs = ()
        self.puissances = ()
        self.racineEvidente = 0

        self.horner()

    def trouveMonomes(self):
        """Cherche les monômes de l'équation"""
        separateurs = "+-"
        aAjouter = ''

        for elem in self.equation:
            if elem in separateurs:
                if len(aAjouter) == 0:
                    aAjouter += elem
                elif aAjouter != '':
                    self.monomes += aAjouter,
                    aAjouter = elem
            else:
                aAjouter += elem
        self.monomes += aAjouter,
        print("Les monômes sont: ", self.monomes)

    def trouveCoeffs(self):
        """Cherche les coefficients pour chaque monôme"""
        aAjouter = ''
        for monome in self.monomes:
            aAjouter += monome[0]  # signe
            if monome[1] == 'x':  # le cas 1x <=> x
                aAjouter += '1'
            else:
                for i in range(1, len(monome)):
                    elem = monome[i]
                    if elem == 'x':
                        break
                    else:
                        aAjouter += elem
            self.coeffs += int(aAjouter),
            aAjouter = ''
        print("Les coefficients sont: ", self.coeffs)

    def trouvePuissances(self):
        for monome in self.monomes:
            for i in range(len(monome)):
                if monome[i] == "x":
                    try:
                        if monome[i + 1] == "^":
                            self.puissances += monome[i + 2],
                        else:
                            self.puissances += 1,
                    except IndexError:
                        self.puissances += 1,
        print("Les puissances sont: ", self.puissances)

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
        for i in range(-100, 100):
            equa = equation.replace('x', "*(" + str(i) + ')').replace('^', '**')
            resEqua = eval(equa)
            if resEqua == 0:
                self.racineEvidente = i
                break
        print("La racine évidente trouvée est: ", self.racineEvidente)

    def horner(self):
        print("L'équation est: ", self.equation)
        self.trouveMonomes()
        self.trouvePuissances()
        self.trouveCoeffs()  # TODO mettre sous forme standard avant ça

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
