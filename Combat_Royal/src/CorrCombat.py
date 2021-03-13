class Combattant:
    #création du personnage combatant.
    def __init__(self,nom,life,attaque = None):
        self.nom = nom
        self.attaque= attaque
        self.life= life
        #-------------------------------------------------------------------------------------
        
    def frapper(self,adversaire):
        
        """pré : vérifier qu'on ne se frappe pas soi-même.
           post :  l'adversaire perd des points de vie équivalent aux points d'attaque de l'autre.
        """
         #---------------------------------------------------------------------------------------
         
        if self.nom!= adversaire.nom and adversaire.life > 0:
            adversaire.life-= self.attaque
            return ("Il ne vous reste que :" + str(adversaire.life)+ "points de vie")
        elif adversaire.life < 0:
            adversaire.life=0
            return (str(adversaire.nom) + " a été detruit ")
        elif self.nom == adversaire.nom:
            return ("vous ne pouvez pas vous infliger des dommages")
        #------------------------------------------------------------------------------------------
class Chevalier(Combattant):
    def __init__(self, nom, life, attaque):
        super().__init__(nom,life, attaque)    
        #------------------------------------------------------------------------------------------
    def guerison (self, points):
        """pré -
           post: Augmente les points de vie du personnage du nombre passé en paramètre, attention  le seuil des  points de vie est fixé à 100.
        """
        Newlife = self.life + points
        if (Newlife > 100):
            self.life = 100
        else:
            self.life = Newlife
         #---------------------------------------------------------------------------------------------------
#création d'une classe Magicien, un Magicien jette les sorts qui éliminent directement l'adversaire des points de vie 

class Magicien(Combattant):
    def __init__(self, nom, life, attaque):
        super().__init__(nom,life,attaque)

    def sort(self,adversaire):
        """ pré: vérifier que l'on ne se jette pas un sort pas soi-même.
            post: l' adversaire est detruit directement par le sort et ses points de vie sont ramener à 0.
        """
        if self.nom!= adversaire.nom and adversaire.life > 0:
            adversaire.life-= self.attaque
            return ("Il ne vous reste que :" + str(adversaire.life)+ "points de vie")
        elif adversaire.life < 0:
            adversaire.life=0
            return (str(adversaire.nom) + " est hors d'état de continuer le combat ")
        elif self.nom == adversaire.nom:
            return ("vous ne pouvez pas vous lancer de sort")