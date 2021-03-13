import unittest

import student as correct


class Testmessage_cod(unittest.TestCase):

    # est ce que le programme compile
    def test_compil(self):
        val = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z", " ", "," ,";","$","*","^","<",">","|","@",")","=","&","µ","!","?",1,2,3,4,5,6,7,8,9,
        0,"é","è","ê","ë","ô","ö","à","â","ä","ù","ç"]

        for i in val:
            try:
                code_etudiant = correct.message(str(i),'c')
            except:
                self.fail(
                    "Vocodagetre fonction semble ne pas compiler lorsqu'elle est appelée avec l'argument {} en mode crypter".format(i))
            try:
                code_etudiant = correct.message(str(i), 'd')
            except:
                self.fail("votre fonction ne semble pas compiler lorsqu'elle est appellée avec l'argument {} en mode decrypter".format(i))

    # test pour les nombres
    def test_num(self):
        nombres = [1,2,3,4,5,6,7,8,9,0]
        for i in nombres:
            code_etudiant_c = correct.message(str(i),'c')
            code_etudiant_d = correct.message(str(i),'d')
            self.assertEqual(code_etudiant_c,str(i))
            self.assertEqual(code_etudiant_d,str(i))

    # test pour les characteres spéciaux
    def test_speciaux(self):
        speciaux = ["é","è","ê","ë","ô","ö","à","â","ä","ù","ç"]
        i = 0
        while i < len(speciaux):
            code_etudiant_c = correct.message(str(speciaux[i]), 'c')
            if i <= 3:
                self.assertEqual(code_etudiant_c,'c')
            elif i <= 5:
                self.assertEqual(code_etudiant_c,'m')
            elif i <= 8:
                self.assertEqual(code_etudiant_c,'y')
            elif i <= 9:
                self.assertEqual(code_etudiant_c,'s')
            else:
                self.assertEqual(code_etudiant_c,'a')
            i += 1

    # tests pour les espaces
    def test_espaces(self):
        code_etudiant_c = correct.message(" ","c")
        code_etudiant_d = correct.message(" ","d")
        self.assertEqual(code_etudiant_c," ")


    # tests pour les majuscules
    def test_maj(self):
        maj = ["A","F","D","Z","E","K","L"]
        for i in maj:
            code_etudiant_c = correct.message(i,'c')
            code_etudiant_d = correct.message(i,'d')
            self.assertEqual(code_etudiant_c,code_etudiant_c.upper())
            self.assertEqual(code_etudiant_d,code_etudiant_d.upper())

    # cas précis
    def test_cas_precis(self):
        a_crypter = ["bonJour, comment ça va?", " é88zZ","écris moi à Noël"]
        deja_crypte = ["zmlHmsp, amkkclr ay ty?"," c88xX","capgq kmg y Lmcj"]
        a_decrypter = ["QmQ","22, tmgjy jcq djgaq!"]
        deja_decrypter = ["SoS", "22, voila les flics!"]
        for i in a_crypter:
            code_etudiant = correct.message(i,'c')
            self.assertEqual(code_etudiant,deja_crypte[a_crypter.index(i)])
        for i in a_decrypter:
            code_etudiant = correct.message(i,'d')
            self.assertEqual(code_etudiant,deja_decrypter[a_decrypter.index(i)])

if __name__ == '__main__':
    unittest.main()