# POO, Programmation Orienté Objet

class Voiture:
    # constructeur
    # le mot clé 'self' désigne l'instance en cours d'utilisation
    def __init__(self):
        # variables d'instances
        self._passagers = 0
        self._vitesse = 0

# encapsulation
    # méthode de type getter
    # c'est une fonction qui permet de lire une variable
    def getPassagers (self):
        return self._passagers

    # méthode de type setter
    # c'est une fonction qui permet de modifier une variable
    def setPassagers(self, passagers):
        if type(passagers) is int \ 
        and passagers >= 0 and passagers <=4 :
            self._passagers = passagers

    def getVitesse (self):
        return self._vitesse

    def setVitesse(self, vitesse):
        if (type(vitesse) is int or type(vitesse) is float) \
        and vitesse >= -10 and vitesse <= 240 :
            self._vitesse = vitesse

# v est une instance de la classe Voiture
#v est un objet de la classe Voiture
v1 = Voiture() 
print(v1.getPassagers())
print(v1.getVitesse())

v1.setPassagers(3)
v1.setVitesse(50)
print(v1.getPassagers())
print(v1.setVitesse())

v2 = Voiture()
print(v2.getPassagers())
print(v2.getVitesse())

