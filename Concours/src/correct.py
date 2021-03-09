class Ingenieurs:
    """
    Liste chainée contenant les participants dans l'ordre
    """
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0

    def add(self, data):
        """ Ajoute le participant dans la liste chainée en respectant l'ordre
        Arg : 'data' est un objet de la classe Participant
        Return : None
        """
        if self.length == 0:
            self.head = self.Node(data)
            self.last = self.head
        else:
            tail = self.head
            while tail.next is not None and tail.next.data >= data:
                tail = tail.next
            tail.next = self.Node(data, tail.next)
        self.length += 1

    def participants(self):
        """
        Args : -
        Return : Liste des objets Participants dans l'ordre par rapport aux resultats
        """
        tail = self.head
        s = [tail.data]
        while tail.next is not None:
            tail = tail.next
            s.append(tail.data)
        return s

    def __str__(self):
        """
        Affiche les éléments de la liste chainée
        """
        tail = self.head
        s = [tail.data.prenom]
        while tail.next is not None:
            tail = tail.next
            s.append(tail.data.prenom)
        return str(s)

class Participant:
    """
    Args:   'prenom' spécifie un str,
            'nom' spécifie un str,
            'matricule' spécifie un int,
            'resultat' spécifie un int,
    Return: None
    """
    def __init__(self, prenom, nom, matricule, resultat):
        self.prenom = prenom
        self.nom = nom
        self.matricule = matricule
        self.resultat = resultat

    def __ge__(self, other):
        if self.resultat >= other.resultat:
            return True
        return False

def admis(participants):
    """
    Args: 'participants' est une liste contenats les objets participants dans l'ordre par rapport aux resultats
    Return : None
    """
    lines = []
    i = 0
    while participants[i].resultat > 9 and i < 12:
        lines.append(f"{i+1}) {participants[i].prenom} {participants[i].nom} {participants[i].matricule} {participants[i].resultat}")
        i += 1
    return lines

def statistique(participants):
    """
    Args : participants spécifie les objets participants dans l'ordre
    Return: retourne le pourcentage d'étudiant admis
    (nombre total d'étudiantadmis *nombre total d'étudiant ayant composé)*100
    """
    return int(( len(admis(participants)) / len(participants) ) * 100)

if __name__ == "__main__":
    part1 = Participant("Jonathan","Peterson","0645123",19.5)
    part2 = Participant("Zinedine","Zidane","0645123",18)
    part3 = Participant("Conor","Mcgregor","0645123",9)
    part4 = Participant("Jennifer","Aniston","0645123",14)
    obj = Ingenieurs()
    obj.add(part1)
    obj.add(part2)
    obj.add(part3)
    obj.add(part4)
    print(admis(obj.participants()))
    print(statistique(obj.participants()))