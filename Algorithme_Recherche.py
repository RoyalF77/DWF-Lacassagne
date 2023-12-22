
## Note au Professeur
# Le Benchmarking est seulement présent dans l'interface utilisateur,
# au niveau de la console, bonne correction !

def lower(char):
    """
    Met le caractère en entrée en minuscule

    char - str - Un caractère

    Sortie : str - Le caractère mis en minuscule
    """
    if 'A' <= char <= 'Z':
        return chr(ord(char) - ord('A') + ord('a'))
    else:
        return char

def lower_phrase(phrase):
    """
    Met la phrase en entrée en minuscule

    char - str - Une phrase

    Sortie : str - La phrase mise en minuscule
    """
    t=""
    for char in phrase:
        t+= lower(char)
    return t

Chiffre = ["0","1","2","3","4","5","6","7","8","9"]
Interdit = ["0","1","2","3","4","5","6","7","8","9",",","\n","*","-","+","/",":",";",",","!","ù","$","^","(",")"]


def Naif(mot, texte):
    """
    Balaye tous les caractères du texte "texte" à la recherche du mot "mot".

    mot - str - Le mot qu'on veut chercher dans le texte.
    texte - str - Le texte où on veut chercher le mot.

    Sortie : bool - True si le mot est présent, False sinon.
    """
    if len(mot) == 0 or mot == " ":
        return "Error - Merci de ne pas tester des espaces ou rien"
    elif len(mot) > len(texte):
        return False
    
    mot = lower_phrase(mot)
    texte = lower_phrase(texte)

    k = 0
    for j in range(len(texte)):
        if k == len(mot) - 1 and mot[k] == texte[j]:
            return True
        elif k != len(mot) - 1 and mot[k] == texte[j]:
             k += 1
        elif k != 0:
            k = 0
    return False

def Boyer_Moore_Horspool(motif, texte):
    """
    Cherche le motif dans texte, en suivant l'algorithme simplifié
    Horspool de Boyer Moore

    motif - str - Le motif qu'on veut chercher dans le texte.
    texte - str - Le texte où on veut chercher le motif.

    Sortie : bool - True si le motif est présent, False sinon.
    """

    if len(motif) == 0 or motif == " ":
            return "Error - Merci de ne pas tester des espaces ou rien"
    elif len(motif) > len(texte):
        return False
    
    motif = lower_phrase(motif)
    texte = lower_phrase(texte)

    k=0
    dico = {}
    for caract in motif:
        if caract not in Chiffre:
            if k != len(motif):
               dico[caract]= k
            k+=1

    for i in range(len(texte)-1,0,-1):
        if len(motif) == 1 and texte[i] == motif[0]:
            return True
        elif texte[i] in motif and texte[i] == motif[len(motif)-1]:
            j = dico[texte[i]]
            while texte[i] == motif[j]:
                i -= 1
                j -= 1
                if j == 0 and texte[i] == motif[0]:
                    return True
    return False


if __name__ == "__main__":
    txt1 = "Attempt blocked. Michel Bastos (Lyon) left footed shot from the left side of the box is blocked. Assisted by Kim Källström."
    txt2 = "TophagGDJnDiKCjhDHHGEUGHRgr:Kje:J.Zeh9hUE(-RRoioçàeer)rjhjr)KuoaETt-ERHiY7YEè6Teèè--ejOEKe454f-f*r"
    txt3_chaos = "TopologieArbritielPasDuToutConnuMaisQuiExiste:LaTerreEstPlatePourInformation:)" * 90
    
    selection = input("Bienvenue dans le menu.\nChoisissez un algorithme entre 'Naif' et 'Boyer Moore Horspool'")
    while lower_phrase(selection) != 'naif' and lower_phrase(selection) != 'boyer moore horspool':
        selection = input("Mode incorrect, ressaisissez le : ")
    if lower_phrase(selection) == 'naif':
        print("Test de l'algorithme Naif :")
        print("True :",Naif("Attempt",txt1))
        print("True :",Naif("LeFt FoOtEd",txt1))
        print("False :",Naif("sside",txt1))
        print("False :",Naif("sidee",txt1))
        print("True :",Naif(".",txt1))
        print("Error :",Naif(" ",txt1))
        print("False :",Naif("Taylor Swift",txt1))
        print("True :",Naif("J.Z",txt2))
        print("True :",Naif("9",txt2))
        print("False :",Naif("TopologieArbritielPasDuToutConnuMaisQuiExisteLaTerreEstPlatePourInformation:)",txt3_chaos))
        print("True :",Naif("平ら","地球は平らではない。"))
    else:
        print("Test de l'algorithme Boyer Moore Horspool :")
        print("True :",Boyer_Moore_Horspool("Attempt",txt1))
        print("True :",Boyer_Moore_Horspool("LeFt FoOtEd",txt1))
        print("False :",Boyer_Moore_Horspool("sside",txt1))
        print("False :",Boyer_Moore_Horspool("sidee",txt1))
        print("True :",Boyer_Moore_Horspool(".",txt1))
        print("Error :",Boyer_Moore_Horspool(" ",txt1))
        print("False :",Boyer_Moore_Horspool("Taylor Swift",txt1))
        print("True :",Boyer_Moore_Horspool("J.Z",txt2))
        print("True :",Boyer_Moore_Horspool("9",txt2))
        print("False :",Boyer_Moore_Horspool("TopologieArbritielPasDuToutConnuMaisQuiExisteLaTerreEstPlatePourInformation:)",txt3_chaos))
        print("True :",Boyer_Moore_Horspool("平ら","地球は平らではない。"))