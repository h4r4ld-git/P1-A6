#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys
import correct as correct
import student as student

class IngenieursTest(unittest.TestCase):

    def setUp(self):
        """
        Création des objet participants et ingenieurs
        """
        self.Cpart1 = correct.Participant("Jonathan","Peterson","0645123",19.5)
        self.Cpart2 = correct.Participant("Zinedine","Zidane","0645123",18)
        self.Cpart3 = correct.Participant("Conor","Mcgregor","0645123",9)
        self.Cpart4 = correct.Participant("Jennifer","Aniston","0645123",14)
        
        try:
            self.Spart1 = student.Participant("Jonathan","Peterson","0645123",19.5)
            self.Spart2 = student.Participant("Zinedine","Zidane","0645123",18)
            self.Spart3 = student.Participant("Conor","Mcgregor","0645123",9)
            self.Spart4 = student.Participant("Jennifer","Aniston","0645123",14)
        except Exception as e:
            self.fail("Erreur dans les variables d'instances de la classe Participant: {}".format(e))

        self.SpartL = [self.Spart1,self.Spart2,self.Spart3,self.Spart4]
        
        try:
            self.SIng = student.Ingenieurs()
            for i in self.SpartL:
                self.SIng.add(i)
        except Exception as e:
            self.fail("La methode add dans la class Ingenieur n'a pas été correctement implémenté: {}".format(e))
        
        try:
            self.Sparts = self.SIng.participants()
        except Exception as e:
            self.fail("La methode participants dans la class Ingenieur n'a pas été correctement implémenté: {}".format(e))
        
        self.CpartL = [self.Cpart1,self.Cpart2,self.Cpart3,self.Cpart4]
        self.CIng = correct.Ingenieurs()
        for i in self.CpartL:
            self.CIng.add(i)
        self.Cparts = self.CIng.participants()

    def test_participant(self):
        """
        test pour les objets participants
        """
        for x in range(len(self.CpartL)):
            for y in self.CpartL[x].__dict__.keys():
                self.assertIn(y, self.SpartL[x].__dict__, "Les attributs ne sont pas correctement intégrés")

        self.assertEqual(self.Spart1 >= self.Spart2, True, "Erreur dans la methode __ge__")
        self.assertEqual(self.Spart3 >= self.Spart4, False, "Erreur dans la methode __ge__")

    def test_ingenieur(self):
        """
        test pour les objets ingenieurs
        """
        for i in range(len(self.Cparts)):
            for y in self.Cparts[i].__dict__:
                self.assertEqual(self.Cparts[i].__dict__[y], self.Sparts[i].__dict__[y],"Erreur dans la methode participants de class Ingenieurs, les participant ne sont pas correctement ajoutés")
        
        self.assertEqual(str(self.SIng), str(self.CIng), "Les participants ne sont pas représenté correctement dans la class Ingenieurs")
        
    def test_admis(self):
        """
        test de la fonction admis
        """
        Coradm = correct.admis(self.Cparts)
        try:
            Stuadm = student.admis(self.Cparts)
            for i in range(len(Coradm)):
                self.assertEqual(Coradm[i], Stuadm[i], "Les participants ne sont pas choisis correctement dans la fonction admis")
        except Exception as e:
            self.fail("La fonction admis n'a pas été correctement implémenté : {} ".format(e))

    def test_statistiques(self):
        """
        test de la fonction statistique
        """
        Corstat = correct.statistique(self.Cparts)
        try:
            Stustat = student.statistique(self.Cparts)
            self.assertEqual(Corstat, Stustat, "La statistique n'est pas calculée correctement")
        except Exception as e:
            self.fail("La fonction statistique n'a pas été correctement implémenté : {} ".format(e))

if __name__ == '__main__':
    unittest.main()