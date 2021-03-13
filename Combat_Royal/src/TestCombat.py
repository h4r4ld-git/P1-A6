#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
import sys
import CorrCombat as correct
import Combat as student

class CombatTest(unittest.TestCase):
    
    def test_combattant(self):
        rep8 =("Votre fonction a retournée None . Cela implique probablement qu'il manque un return dans votre code.")
        Combattant1 = correct.Combattant("Patrick",80,10)
        Combattant2 = correct.Combattant("ismael",100,15)
        Combattant3 = correct.Combattant("Luca",20,10)
        Combattant4 = correct.Combattant("saulgoodman",90,10)
        try:
            sCombattant1 = student.Combattant("Patrick",80,10)
            sCombattant2 = student.Combattant("ismael",100,15)
            sCombattant3 = student.Combattant("Luca",20,10)
            sCombattant4 = student.Combattant("saulgoodman",90,10)
            #self.fail("Votre fonction a provoqué l'exception {}: {}".format(type(e), e))
        except Exception as e:
            self.fail("""La class Combattant semble provoqué  une erreur  {}:{} lors de la création de nouveaux combattants:
            sCombattant1 = student.Combattant("Patrick",80,10)
            sCombattant2 = student.Combattant("ismael",100,15)
            sCombattant3 = student.Combattant("Luca",20,10)
            sCombattant4 = student.Combattant("saulgoodman",90,10) """.format(type(e),e))
        rep = _("Votre methode n'a pas associée les bonnes valeurs au combattant {} vous lui avez attribué {}:au lieu de {}")
        self.assertEqual(Combattant1.nom,sCombattant1.nom, rep.format( "Patrick", sCombattant1.nom, Combattant1.nom ))
        self.assertEqual(Combattant2.nom,sCombattant2.nom, rep.format( "ismael", sCombattant2.nom, Combattant2.nom ) )
        self.assertEqual(Combattant2.attaque,sCombattant2.attaque)
        self.assertEqual(Combattant3.life,sCombattant3.life , rep.format( "Luca", sCombattant3.life, Combattant3.life))
        self.assertEqual(Combattant3.attaque,  sCombattant3.attaque)
        #test de la méthode frapper
    
        self.assertEqual(Combattant1.frapper( Combattant2),sCombattant1.frapper( sCombattant2))
        self.assertEqual(Combattant3.frapper( Combattant4),sCombattant3.frapper( sCombattant4))
        self.assertEqual(Combattant2.life,  sCombattant2.life ,"Votre code semble ne pas bien implementer la methode frapper() de la classe combattant car il a retourner comme valeur {} au lieu de {} ".format(sCombattant2.life,Combattant2.life))
        self.assertEqual(Combattant4.life,  sCombattant4.life,"Votre code semble ne pas bien implementer la methode frapper() de la classe combattant car il a retourner comme valeur {} au lieu de {} ".format(sCombattant4.life,Combattant4.life) )
        self.assertIsNotNone(sCombattant1.frapper( sCombattant2),rep8)

    #verification de la creation de la classe chevalier        
    def test_chevalier(self):
        c1=correct.Chevalier("Joe",100,25)
        c2=correct.Chevalier("Mael",50,40)
        c3=correct.Chevalier("Rafael",30,10)
        c4=correct.Chevalier("lionel",90,20)
        try:
            stc1=student.Chevalier("Joe",100,25)
            stc2=student.Chevalier("Mael",50,40)
            stc3=student.Chevalier("Rafael",30,10)
            stc4=student.Chevalier("lionel",90,20)
        except Exception as e:
            self.fail("""La class chevalier  semble provoqué  une erreur {} : {} lors de la création des chevaliers:
            stc1=student.Chevalier("Joe",100,25)
            stc2=student.Chevalier("Mael",50,40)
            stc3=student.Chevalier("Rafael",30,10)
            stc4=student.Chevalier("lionel",90,20)""".format(type(e),e))
            
            #test de la  methode guerison
            rep2 = _("Votre code semble ne pas bien implementer la methode guerison() de la classe chevalier car il a retourner comme valeur {}: pour {} au lieu de {}")
            self.assertEqual(c1.guerison(20), stc1.guerison(20))
            self.assertEqual(c2.life, stc2.life)
            self.assertEqual(c1.attaque, stc1.attaque)
            self.assertEqual(c2.guerison(10), stc2.guerison(10))
            self.assertEqual(c3.guerison(50), stc3.guerison(50))
            #test pour voir si la methode frapper est bien implementer par la classe chevalier
            self.assertEqual(c1.frapper( c2),stc1.frapper( stc2),)
            self.assertEqual(c3.frapper( c4),stc3.frapper( stc4))
            self.assertEqual(c2.life,  stc2.life )
            self.assertEqual(c4.life,  stc4.life )

    def test_magicien(self):
        #test de la création d'objets magicien 
        Mag1=correct.Magicien("Merlin",50,15)
        Mag2=correct.Magicien("Morgane",54,33)
        Mag3=correct.Magicien("Arthur",47,27)
        Mag4=correct.Magicien("Gaillus",100,47)
    
    
        try:
            stMag1=student.Magicien("Merlin",50,15)
            stMag2=student.Magicien("Morgane",54,33)
            stMag3=student.Magicien("Arthur",47,27)
            stMag4=student.Magicien("Gaillus",100,47)

        except Exception as e:
            self.fail("""La class Magicien semble provoqué une erreur {}: {}  lors de la création de nouveaux magiciens:
            stMag1=student.Magicien("Merlin",50,15)
            stMag2=student.Magicien("Morgane",54,33)
            stMag3=student.Magicien("Arthur",47,27)
            stMag4=student.Magicien("Gaillus",100,47)""".format(type(e),e))

        rep3 = _("Votre fonction n'a pas associé les bonnes valeurs de point de vie , vous avez attribué  {} pour  {} à la place de: {} ")
        #test de la méthode sort()
        self.assertEqual(Mag1.sort(Mag2),stMag1.sort(stMag2))
        self.assertEqual(Mag4.sort(Mag3),stMag4.sort(stMag3))
        self.assertEqual(Mag2.life,  stMag2.life,rep3.format(stMag2.life, "stMag2",Mag2.life))
        self.assertEqual(Mag3.life,  stMag3.life, rep3.format(stMag3.life, "stMag3",Mag3.life))
        
        #test de la méthode frapper() pour le cas du Magicien
        self.assertEqual(Mag1.frapper(Mag4),stMag1.frapper(stMag4))
        self.assertEqual(Mag4.frapper(Mag1),stMag4.frapper(stMag1))
        self.assertEqual(Mag4.life,  stMag4.life,rep3.format(stMag4.life, "stMag4",Mag4.life))  
        self.assertEqual(Mag1.life,  stMag1.life, rep3.format(stMag1.life, "stMag1",Mag1.life))
        


if __name__ == "__main__":
    unittest.main()