import unittest

import correct
import student

class TestLa_Course(unittest.TestCase):
    
    def test_La_course(self):
        
        a = "Luka: 14\nIsam :1\n6 : 001\nAwidYamak:7\Bouchlaghem :  9\n Ismail;7\njdef:zefezf\n4: Mohamed\nSaid?5\n\n\njkfjr\n54564\n'(-è: 2"
        i = "Ismail: 14\nIzadin :1\n6 : 001\nBoukabouz:9\nRafik :  7\n Ismail;7\njdef:zefezf\n4: Mohamed\nSaid?5\n\n\njkfjr\n58:Samad"
        b = "Ismail: 20\nRomayssa :1\n6 : 001\nKartasou:7\nSaid :  9\n Ismail;7\njdef:?!\n4: Mohamed\nSaid?5\n\n\njkfjr\n\n\n;;;..?"
        c = "Mohamed: 15\nRodayna :13\n6 : 001\nRiiF:715\nAbjij :  14\n Ismail;7\njdef:zefezf\n4: Mohamed\nSaid?5\n\n\njkfjr\;,?:325"
        d = "Zafzafi: 19\nNassir :16\n6 : 001\nZafzafi:25\nAhdidouch :  24\n Ismail;7\njdef:zefezf\n4: Mohamed\nSaid?5\n\n\njkfjr\n$*^:&é3"
        e = "Zafzafi: 1\nHamza :16\n6 : 001\nAwidAbak:15\nFikri :  24\n Ismail;7\njdef:zefezf\n4: Mohamed\nSaid?5\n\n\njkfjr\nSamir: 6"
        f = "Karim: 6\nBilal :8\n6 : 001\nYouta:65\nGholam :  7\n Ismail;7\njdef:zefezf\n4: Mohamed\nSaid?5\n\n\njkfjr\n54564\nSaid:10\n\n\neff:64\nytu:Ay7"
        g = "Ilyass: 1\nSaffah :5\n6 : 001\nHalamala:715\nRayan :  4\n Ismail;7\njdef:zefezf\n4: Mohamed\nSaid?5\n\n\njkfjr\n54564\nImane:2"
        h = "Kamal: 1\nImad :5\n6 : 001\nAyoube:715\Lina :  4\nMohamed:10\nYassir:3\nRayan:14\nImran:2\nSouraya: 7\nImane:4\nAnissa:15"
        j = "Mohamed:3\nSalwa:2\nIsmail:4\nAymane:6\nAyoube:9\nRodayna:12\nImran:13\nYassir:14\nRayan:15\nFikri:1"
        k = "Sara:11\nNisrine:12\nSophia:13\nMarouan:14\nFatiha:15"
        m = "Wassima:1\nWassim:2\nWadie:3\nMohamed:4\nfjf:23\n2:Halim\??:2"
        l = [a,b,c,d,e,f,g,h,i,j,k,m]
        for i in range(len(l)):
            rep = ("Votre fonction a retourné {} alors que la réponse attendue est {}")
            f1 = open("Timssah_i+1.txt","w")
            f1.write(l[i])
            f1.close()
            try:
                student_course = student.La_course("Timssah_i+1.txt")
            except Exception as error:
                self.fail("la fonction 'La_course' a provoqué l'exception {}: {}".format(type(error), error))
                
            correct_course = correct.La_course("Timssah_i+1.txt")
            
            self.assertEqual(student_course, correct_course, rep.format(student_course, correct_course))
                    
                    
            



if __name__ == '__main__':
    unittest.main(verbosity=2)
