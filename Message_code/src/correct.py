def message(chaine,mode):
    """
    pre
    :param chaine: une chaine de charactère de type string
    :param mode: un charactère string "c" (crypter) ou "d" (décripter) pour déterminer quel mode est choisi
    post : retourne une chaine de charactere string remplissant les conditions suivantes :
        - chaque lettre a été remplacée par la lettre se trouvant deux places vers la gauche dans l'alphabet (C=A)
        - les lettres spéciales telles que é, à, è sont considérées comme des lettres normales avant d'ếtre remplaçée
        - les chiffres restent inchangés et les espaces sont ignorés
    """
    global new_lettre
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    speciaux = "éèêëôöàâäùç"
    trad = "eeeeooaaauc"
    new_chaine = ""
    chaine == chaine.lower()
    for char in chaine:
        # si c'est une lettre normale
        if char in alphabet:
            if mode == "c":
                new_lettre = alphabet[alphabet.index(char)-2]
            elif mode == "d":
                if char == "z":
                    new_lettre = "b"
                elif char == "y":
                    new_lettre = "a"
                else:
                    new_lettre = alphabet[alphabet.index(char)+2]
        elif char.lower() in alphabet:
            char = char.lower()
            if mode == "c":
                new_lettre = alphabet[alphabet.index(char)-2]
            elif mode == "d":
                if char == "z":
                    new_lettre = "B"
                elif char == "y":
                    new_lettre = "A"
                else:
                    new_lettre = alphabet[alphabet.index(char)+2]
            new_lettre = new_lettre.upper()
        # si c'est un charactere spécial
        elif char in speciaux:
            modif = trad[speciaux.index(char)]
            if mode == "c":
                new_lettre = alphabet[alphabet.index(modif)-2]
            elif mode == "d":
                new_lettre = alphabet[alphabet.index(modif)+2]
        # si c'est un nombre ou autre chose
        else:
            new_lettre = char
        new_chaine += str(new_lettre)
    return new_chaine
