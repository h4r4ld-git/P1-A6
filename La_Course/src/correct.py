"""
with open("participant.txt","w") as file:
    file.write("Ismail: 1\nPatrick :15\n6 : 001\nSaul:715\nSacha :  14\n Ismail;7\njdef:zefezf\n4: Mohamed\nSaid?5\n\n\njkfjr\n54564")
"""

def La_course(filename):
    """
    pre: filename est un fichier contient dans chaque ligne
         un participant et sa durée pendant la course sous format
         suivante: "Le nom : la durée pendant la course en minutes"
         
    post:
         * Retourne un dictionnaire qui:
            -Contient comme des clées les trois premières places
             gagnantes dans la course dans un ordre croissant
             (1, 2, 3) et chaque clé contient comme valeur une liste
             des participants gagnants; les participants qui sont
             dans l'intervalle [0(minute),5(minutes)] seront en
             première place, les participant qui sont dans ]5, 10]
             seront en deuxième et les participant qui sont dans ]10, 15]
             seront en troisième place.
             
           -Dans lesquels les participant doivent respecter la forme
            suivante: "Le nom de participant : miniutes", et ignorez
            tous les autres formats comme "Ismail?12", "10:Luka", "Sacha?4"... 
        
           -Ne contient pas des clées où ses valeur sont des listes vides
            par exemple si on a pas des participant qui ont fait la course
            entre ]5, 10], il faut retouner un dictionnaire sans la deuxième
            place "{1: ['timssah'], 3:['Said']}"

           -Où les participants gagnants sont classée par ordre croissant
            selon le temps qu'ils ont passés pendant la course
            
    """
    with open(filename) as file:
        l = []
        for line in file:
            #print(line)
            if verification(line):
                #print(line)
                line = line.replace(" ","").strip().split(":")
                l += line

        l1 = []
        for i in range(1,len(l) +1,2):
            l1.append(int(l[i]))
        l1 = sorted(l1)
        
        s = []
        for i in range(len(l1)):
            s.append(l[l.index(str(l1[i]))-1])
            s.append(l1[i])
            
        dic = {i:[] for i in (1,2,3)}
        for i in range(0,len(s),2):
            print(s[i])
            if s[i+1] <= 5:
                dic[1] = dic.get(1, []) + [s[i]]
            elif s[i+1] > 5 and s[i+1] <= 10:
                dic[2] = dic.get(2, []) + [s[i]]
            elif s[i+1] > 10 and s[i+1] <= 15:
                dic[3] = dic.get(3, []) + [s[i]]
        
        #print(dic)        
        dic2 = {}
        for i in dic:
            if dic[i] != []:
                dic2[i] = dic[i]
        if len(dic2) >= 1:
            return dic2
        else:
            return {}
            
                    
                
def verification(string):
    """
    Vérifiez si la chaîne en argument a bien respecté la forme
    de " chaine de caractère : nombre entier "
    return True s'elle respecte bien la condition et False sinon
    """
    a = ",;!)(?'[]{}=+-_#@&'*$%¨^"
    for i in a:
        if i in string:
            return False
    if ":" in string and string != "\n":
        string = string.replace(" ","").strip().split(":")
        for i in range(len(string)):
            try:
                string[i] = str(string[i])
                string[i+1] = int(string[i+1])
                a = True
                if a:
                    try:
                        string[i] = int(string[i])
                        string[i+1] = str(string[i+1])
                        return False
                    except:
                        return True                         
            except:
                return False
    else:
        return False        



#print(La_course("participant.txt"))


