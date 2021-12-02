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
        """Affiche les monomes du polynôme"""
        print("Les monômes sont: ", end='')
        for monome in self.monomes:  # pour tous les monomes
            print(monome, end=', ')  # affiche le monome
        print()

    def affichePuissanceEtCoeff(self):
        """Affiche le dico des puisances et des coeffs"""
        print("Les puissances et les coeffs: ", self.puissancesEtCoeffs)

    def trouvePuissancesEtCoeff(self):
        """Récupère les coeffs et les puissances de chaque monomes et les stocke dans un dico"""
        for monome in self.monomes:  # pour tous les monomes
            self.puissancesEtCoeffs[monome.puissance] = monome.coeff  # la puissance en clé, le coeff en valeur
        self.affichePuissanceEtCoeff()  # affiche le dico

    def trouveMonomes(self):
        """Cherche les monômes de l'équation"""
        separateurs = "+-"  # ce qui défini le début ou la fin d'un monome
        aAjouter = ''  # le monome à ajouter

        for elem in self.equation:  # pour toutes les lettres de l'équation
            if elem in separateurs:  # si la lettre est un séparateur
                if len(aAjouter) == 0:  # si le monome est vide
                    aAjouter += elem  # ajoute le séparateur
                elif aAjouter != '':  # si a ajouter n'est pas vide
                    self.monomes += Monome(aAjouter),  # ajoute un objet Monome avec aAjouter comme équation
                    aAjouter = elem  # pour le signe(peut-être)
            else:
                aAjouter += elem  # ajoute la lettre au monome à ajouter
        self.monomes += Monome(aAjouter),  # ajoute le dernier monome récupérer(car pas de "séparateur" à la fin)
        self.afficheMonomes()  # affiche les monomes

    def isSecondDegre(self):
        """Retourne si oui ou non l'équation gérée est du second degré
        :return: True ou False
        """
        return self.trouveDegre() == 2  # si le degré est égal à 2

    def trouveDegre(self):
        """Renvoie le degré de l'équation gérée
        :return: le degré de l'équation(int)
        """
        puissances = tuple(self.puissancesEtCoeffs.keys())  # liste des puissances
        res = puissances[0]  # prend la première puissance qui vient
        for elem in puissances:  # pour toutes les puissances
            try:
                if int(elem) > res:  # si la puissance est supérieure à res(qui est censée être la plus grande)
                    res = int(elem)  # remplace res par elem
            except TypeError:  # pour gérer le None
                pass
        return res  # retour du résultat

    def standardise(self):
        """Standardise l'équation"""
        degre = self.trouveDegre()  # le degre de l'équation
        for i in range(degre, 1, -1):  # parcours les puissances dans l'ordre décroissant
            if i not in self.puissancesEtCoeffs.keys():  # si une puissance(qui est censée être présente) n'est pas présente
                self.puissancesEtCoeffs[i] = 0  # l'ajoute et met son coeff à 0(puisque non présent de base)
                print(i, "n'est pas présent, rajout.\nLe dico maintenant: ", self.puissancesEtCoeffs)  # affichage

    def trouveRacineEvidente(self):
        """Trouve une racine évidente"""
        coeffs = tuple(self.puissancesEtCoeffs.values())  # les coeffs
        puissances = tuple(self.puissancesEtCoeffs.keys())  # les puissances

        equation = ''  # l'équation
        for i in range(len(self.monomes)):  # boucle de 0 jusqu'à la longeur de la liste des monomes
            if puissances[i] is not None:  # si la puissance i n'est pas None
                if coeffs[i] > 0:  # si le coeff de i est supérieur à 0
                    equation += '+' + str(coeffs[i]) + 'x^' + str(puissances[i])  # ajoute à l'équation(avec le '+' devant)
                else:
                    equation += str(coeffs[i]) + 'x^' + str(puissances[i])  # ajoute à l'équation(comme c'est < 0, le '-' esr de base
            else:
                equation += str(coeffs[i])  # sinon ajoute le coeff(car pas de puissance, juste un entier)

        for i in range(-1000, 1000):  # boucle de -1000 jusqu'à 1000
            equa = equation.replace('x', "*(" + str(i) + ')').replace('^', '**')  # remplace des éléments de l'équation par des symboles plus compréhensible par la focntion eval()
            resEqua = eval(equa)  # résout l'équation
            if resEqua == 0:  # si le résultat est 0
                self.racineEvidente = i  # alors i est une racine évidente
                break  # sort de la boucle
        print("La racine évidente trouvée est: ", self.racineEvidente)  # affichage

    def resolutionSecondDegre(self):
        """Résout une équation du 2nd degré"""
        abc = ()  # stocke les coeff a, b, et c
        print(self.puissancesEtCoeffs)  # affichage
        for i in range(2, -1, -1):  # le puissances(2, 1 et 0(None))
            try:
                if i != 0:  # i i ne vaut pas 0
                    abc += self.puissancesEtCoeffs[i],  # ajoute le coeff de i
                else:
                    abc += self.puissancesEtCoeffs[None],  # ajoute l'entier associée à None
            except KeyError:  # si la clé n'est pas présente
                abc += 0,  # ajoute 0 aux coeff
        # comme tout est censé être dans l'ordre
        a = abc[0]
        b = abc[1]
        c = abc[2]

        delta = ((b ** 2) - (4 * a * c))  # calcule delta

        print("Delta vaut: ", delta)  # affiche delta

        if delta == 0:  # si delta vaut 0
            x0 = -b / (2 * a)  # une racine
            self.polynomeFactorise += str(a) + '(x' + str(-x0) + ')'  # ajoute le résultat au résultat final
        elif delta < 0:  # si delta est < 0
            self.polynomeFactorise += '(' + self.equation + ')'  # ajoute l'équation telle quelle(mais la met entre ())
        else:  # delta > 0
            x1 = (-b - (delta ** 0.5)) / (2 * a)  # 1ère racine
            x2 = (-b + (delta ** 0.5)) / (2 * a)  # 2ème racine
            self.polynomeFactorise += str(a) + '(x + ' + str(-x1) + ')' + '(x + ' + str(-x2) + ')'  # ajoute les résultat au résultat final

    def puissancesEtCoeffs2Equa(self):
        """Convertit le dico en une équation"""
        equa = ''  # l'équation
        for puissance in self.puissancesEtCoeffs:  # pour toutes les puissances
            if puissance is None:  # i la puissance vaut None
                if self.puissancesEtCoeffs[puissance] > 0:  # si le coeff est > à 0
                    equa += '+' + str(self.puissancesEtCoeffs[None])  # rajoute +coeff_de_None
                else:
                    equa += str(self.puissancesEtCoeffs[None])  # rajoute coeff_de_None
            else:
                equa += str(self.puissancesEtCoeffs[puissance]) + 'x^' + str(puissance)  # rajoute le coeff x^puissance
        self.equation = equa  # défini l'équation à celle qui vient d'être "calculée"

    def horner(self):
        # TODO Commentaires
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
