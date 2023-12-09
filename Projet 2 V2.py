"""
def Boyer_Moore(str,BS):
    ""
    Définir se que fait le script

    str - str - Le mot qu'on veut chercher dans le texte 

    BS - tab - tableau representative de la base de données
     
    Sortie : lst - Les indices de la base de données contenant
                le mot cherché
    ""
    k=0
    dico = {}
    for caract in str: # Creation d'un dico pour savoir où est chaque lettre du mot
        if caract not in Chiffre:
            if caract in dico:
               dico[caract].append(k)
            elif caract not in dico:
                dico[caract] = [k]
            k+=1
            
    tab = []
    for i in range(len(BS)):# parcours des lignes
        first = str[0]
        f= BS[i]
        
        indice=1
        for j in range(len(f)):# parcours des lettres
            if f[j] in dico:# si la lettre est dans le dico
                indicecorresp = dico[f[j]][len(dico[f[j]])-1] 
                if f[j] == str[indicecorresp]:
                    #print(f"ligne {i}")
                    #print(j,f[j],str[indicecorresp],indice)
                    indice += 1
                    if indice-1 == len(str) and f[j] == first:
                        #print(indice,f[j], str[indicecorresp])
                        tab.append(i)
                        indice = 1
                    indicecorresp= indicecorresp-1    
            else:
                indice = 1
    if tab != []:
         return tab
    return "ERROR 404 - Aucun Mot Correspondant A Eté Trouvé Dans La Base De Données"
"""

"""
def decalage_horspool(motif, texte, i, j, bad_carac):
    ""
    motif - str, chaîne de caractères
    texte - str, chaîne de caractères
    i - int, position de la fenêtre telle que 0 <= i < len(texte)
    j - int, entier tel que 0 <= j < len(motif)
    bad_carac - dict, dictionnaire des mauvais caractères (Horspool)
    Sortie: int - décalage à appliquer à la fenêtre en cas de non correspondance
                    entre texte[i+j] et motif[j]
    ""
    if texte[i + j] not in bad_carac:
        return j + 1
    else:
        k = bad_carac[texte[i + j]]
        if k < j:
            return j - k
        else:
            return 1
"""

"""
def est_present(motif, texte):
    if len(motif) == 0 or len(motif) > len(texte):
            return False

    k=0
    dico = {}
    for caract in motif:
        if caract not in Chiffre:
            if k != len(motif):
               dico[caract]= k
            k+=1

    motif = lower_phrase(motif)
    texte = lower_phrase(texte)

    for i in range(len(texte)-1,0,-1):
        if texte[i] in motif and texte[i] == motif[len(motif)-1]:
            j = dico[texte[i]]
            while texte[i] == motif[j]:
                i -= 1
                j -= 1
                if j == 0 and texte[i] == motif[0]:
                    return True
    return False
"""
"""
def Boyer_Moore(texte,BS):
    tab = []
    for i in range(len(BS)):
        tBS = tab_str(BS[i])
        if est_present(texte,tBS):
            tab.append(i)
    if tab != []:
         return tab
    return "ERROR 404 - Aucun Mot Correspondant A Eté Trouvé Dans La Base De Données"
"""
import os, csv, sys

File_BD = "BaseDonneesV2.txt"
#F_Details = "Details.csv"
typealgo = "Naif"

##
## POGRAMMES SECONDAIRE
##

def lower(char):
    if 'A' <= char <= 'Z':
        return chr(ord(char) - ord('A') + ord('a'))
    else:
        return char

def lower_phrase(phrase):
    t=""
    for char in phrase:
        t+= lower(char)
    return t

def tab_str(tab):
    t= ""
    for el in tab:
        if el not in Interdit:
            t+= el
    return t

##
##PROGRAMME
##

Chiffre = ["0","1","2","3","4","5","6","7","8","9"]
Interdit = ["0","1","2","3","4","5","6","7","8","9",",","\n"]

# Si NameError sur __file__, effacez les try et les except, gardez juste la ligne avec getcwd
try:
    repertoire = os.getcwd()
    cheminBS = os.path.join(repertoire, File_BD)
    BaseD = open(cheminBS, "r+", encoding='utf-8')
except FileNotFoundError:
    try:
        repertoire = os.path.realpath(__file__)
        cheminBS = os.path.join(repertoire, File_BD)
        BaseD = open(cheminBS, "r+", encoding='utf-8')
    except FileNotFoundError:
        try :
            repertoire = os.path.realpath(__file__)
            repertoire = os.path.abspath(os.path.join(repertoire, os.pardir))
            cheminBS = os.path.join(repertoire, File_BD)
            BaseD = open(cheminBS, "r+", encoding='utf-8')
        except FileNotFoundError:
            print("Base de données non trouvé, merci de bien la mettre dans le meme dossier que le script")

cheminBS = os.path.join(repertoire, File_BD)
BaseD = open(cheminBS, "r+", encoding='utf-8')

with BaseD as Base:
    """
    Création du Tableau Table permettant de faciliter la recherche
    des mots demandé dans les algorithme Naif et de Boyer-Moore

    ATTENTION
    La base de donnée doit etre dans le meme dossier parent que le
    script pour le bon fonctionnement de cette partie du script
    ATTENTION
    """    
    BS = []
    i = 0
    for ligne in Base:
        nom = []
        nom.append(f"{i}")
        for caract in ligne:
            if caract not in Interdit:
                nom.append(lower(caract))
        BS.append(nom)
        i += 1

def HorsTab(tab):
    """
    Va chercher la ligne correspondante au numero de l'indice 0
    
    tab - lst - Tableau correspondant au mot recherché
    
    Sortie : str - Ligne complete contenant le mot recherché
    """
    text = ''
    for i in tab:
        text += f"[l.{i}] "
        for j in range(len(BS[i])):
            if j != 0:
                text += BS[i][j]
        text += "\n\n"
    return text

def debug(ligne,indice,bs):
    text = ''
    for j in range(indice,len(bs[ligne])):
        if j != 0:
             text += bs[ligne][j]
    text += "\n"
    return text

def Naif(mot, BS):
    """
    Balaye tout le texte de la base de données retranscrite dans
    le tableau "base_de_donnees" à la recherche du mot "mot".

    mot - str - Le mot qu'on veut chercher dans le texte.

    base_de_donnees - list - Tableau représentatif de la base de données.

    Sortie : indices - Les indices de la base de données contenant
                      le mot cherché.
    """
    if len(mot) == 0:
        return
    
    mot = lower_phrase(mot)
    tempo = []

    for i in range(len(BS)):
        k = 0
        f = BS[i]
        if len(mot) > len(f):
            pass
        for j in range(len(BS[i])):
            if k == len(mot) - 1 and mot[k] == f[j]:
                if i not in tempo:
                    tempo.append(i)
            elif k != len(mot) - 1 and mot[k] == f[j]:
                k += 1
            elif k != 0:
                k = 0

    if tempo != []:
         return tempo
    return "ERROR 404 - Aucun Mot Correspondant A Eté Trouvé Dans La Base De Données"

def est_present(motif, texte):

    if len(motif) == 0 or len(motif) > len(texte):
            return False
    
    k=0
    dico = {}
    for caract in motif:
        if caract not in Chiffre:
            if k != len(motif):
               dico[caract]= k
            k+=1

    motif = lower_phrase(motif)
    texte = lower_phrase(texte)

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

def Boyer_Moore(texte, BS):
    tab = []
    for i in range(len(BS)):
        tBS = lower_phrase(BS[i])
        if est_present(texte, tBS):
            tab.append(i)
    if tab != []:
         return tab
    return "ERROR 404 - Aucun Mot Correspondant A Eté Trouvé Dans La Base De Données"

##
##INTERFACE GRAPHIQUE
##
#"""
from tkinter import *
from tkinter.filedialog import askopenfilename

cheminlogo = os.path.join(repertoire, "Logo.ico")

def get_input():
    global typealgo
    mot = entry.get()
    if mot != "" and mot != " ":
        print(f"Mot trouvé : {mot}")

        if typealgo == "Naif":
            output = Naif(mot,BS)
        elif typealgo == "Boyer Moore":
            output = Boyer_Moore(mot,BS)

        if type(output) == list :
           reponse.delete(1.0,END)
           if len(output)> 400:
               reponse.insert(END,f"Il y a trop de correspondance pour {mot}, ({len(output)})\nMerci d'etre plus precis dans le choix de votre mot pour une meilleur détection")
               reponse.config(fg="#D05962")
               window.after(200, lambda: reponse.config(fg="black"))
           else:
                reponse.insert(END,f"Correspondance pour {mot} :\n{HorsTab(output)}")
                reponse.config(fg="#5B8F75")
                window.after(200, lambda: reponse.config(fg="black"))
           print(f"{len(output)} Réponse trouvé")
        else:
            reponse.delete(1.0,END)
            reponse.insert(END,f"Il n'y a aucune correspondance pour {mot}")
            reponse.config(fg="#D05962")
            window.after(200, lambda: reponse.config(fg="black"))
            print("Aucune correspondance")
    else:
        reponse.delete(1.0,END)
        reponse.insert(END,f"Je n'aime pas les espaces désolé\nJe préfère les mots")
        reponse.config(fg="#EEF3F1")

def changer_chemin():
    global File_BD
    global BS
    nouveau_chemin = askopenfilename(title="Sélectionner la nouvelle base de données", filetypes=[("Text files", "*.txt")])
    nomofficiel = os.path.basename(nouveau_chemin)
    if nouveau_chemin:
        File_BD = nomofficiel
        cheminBS = os.path.join(repertoire, File_BD)
        BaseD = open(cheminBS,"r+", encoding = 'utf-8')
        with BaseD as Base:
            BS = []
            i = 0
            for ligne in Base:
                nom = []
                nom.append(f"{i}")
                for caract in ligne:
                    if caract not in Chiffre:
                        nom.append(caract)
                BS.append(nom)
                i += 1
        BaseSelection.config(text=f"Base de données Sélectionné :\n{File_BD}\nAlgorithme utilisé : {typealgo}", fg="green")
        window.after(200, lambda: BaseSelection.config(fg="black"))
        print(f"Chemin de la base de données mis à jour : {File_BD}")

def changer_algoN():
    global typealgo
    typealgo = "Naif"
    BaseSelection.config(text=f"Base de données Sélectionné :\n{File_BD}\nAlgorithme utilisé : {typealgo}", fg="green")
    window.after(200, lambda: BaseSelection.config(fg="black"))
    print("Agltorithme Naif Choisi")

def changer_algoBM():
    global typealgo
    typealgo = "Boyer Moore"
    BaseSelection.config(text=f"Base de données Sélectionné :\n{File_BD}\nAlgorithme utilisé : {typealgo}", fg="green")
    window.after(200, lambda: BaseSelection.config(fg="black"))
    print("Agltorithme Boyer Moore Choisi")

##MISE EN PLACE DE LA FENETRE
window = Tk()
window.title("DWF - Database Word Finder by Lacassagne Students")
window.geometry("1400x700")
window.minsize(900,450)
window.maxsize(1400,700)

try:
    window.iconbitmap(cheminlogo)
except FileNotFoundError:
    pass

window.config(background="#c4c4c4")

##MENU
newmenu = Menu(window)
BaseM = Menu(newmenu, tearoff= 0)
BaseM.add_command(label="Parcourir les Bases de Données", command=changer_chemin)
BaseM.add_command(label="Quitter", command= window.destroy)
newmenu.add_cascade(label="Fichier", menu= BaseM)

menu_algo = Menu(newmenu,tearoff= 0)
menu_algo.add_command(label="Naif", command= changer_algoN)
menu_algo.add_command(label="Boyer_Moore", command= changer_algoBM)
newmenu.add_cascade(label="Algorithme", menu= menu_algo)

window.config(menu=newmenu)

##MISE EN PLACE DES GROUPES
frame = Frame(window, bg= "#c4c4c4", bd=1)
sframe = Frame(frame,bg= "#c4c4c4", bd=1, relief= SUNKEN)
output = Frame(frame,bg= "#c4c4c4", bd=1)
enbas = Frame(frame,bg= "grey", bd=1, relief= SUNKEN)

##CREATION DU TEXTE
label = Label(sframe,text="Bienvenue dans DWF\nChercheur de mots",font=("Courrier",40), background="#c4c4c4",fg= "black")
label.pack(expand=YES,fill= BOTH)

label2 = Label(sframe,text="Merci de mettre ici le mot cherché",font=("Courrier",20), background="#c4c4c4", fg= "black")
label2.pack(expand=YES,fill= BOTH)

##CREATION DE LA ZONE DE TEXTE
entry = Entry(sframe,font=("Courrier",30), background="#c4c4c4", fg= "black")
entry.pack(expand=YES)

##CREATION DE LA ZONE DE REPONSE
reponse = Text(output,font=("Courrier",15), background="#c4c4c4",fg= "grey")
reponse.pack(expand=YES,fill=BOTH)

##CREATION DU BOUTON
button = Button(sframe, text= "Chercher", font=("Courrier",40), background="#c4c4c4", fg= "black", command=get_input)
button.pack(expand=YES,pady=25)

##CREATION DE LA ZONE DE BASE DE DONNEES
BaseSelection = Label(sframe,text=f"Base de données Sélectionné :\n{File_BD}\nAlgorithme utilisé : {typealgo}",font=("Courrier",20), background="#c4c4c4", fg= "black")
BaseSelection.pack(expand=YES,fill=BOTH)

##PACKING DES FRAME
frame.pack(expand=NO,fill= BOTH, side = LEFT)
sframe.pack(expand=NO,fill= BOTH, side= LEFT)
output.pack(expand=YES,fill= BOTH, side= RIGHT)

print("Fenetre Ouverte")
window.mainloop()
#"""

"""
from random import randint

def test(el,BS):
    tab = ["Diekmeier","Nice","Tore","Mario","k"]
    #i = randint(0,len(tab)-1)
    #j = randint(0,len(tab[i]))
    #print(tab[i])
    n = Naif(el,BS)
    b = Boyer_Moore(el, BS)
    if n == b:
        return True
    else:
        print(n,b)
        return False
"""

if __name__ == "__main__":
    print("Script Fini")
    #print(Boyer_Moore("Dortmund",BS))
    #print(test("a",BS))
    #print(Naif("Nice",BS))
    #print(est_present_horspool("CAAGT","ATCAAGTTCAAGTCAGTCCCCAAGTTGATGCAAGT"))
    #print(Boyer_Moore("k",BS))
    #print(Boyer_Moore1("k",BS))
    #print(Naif("Corner",BS))
    #print(Naif("Hamburg"))
    #print(Naif("Nice",BS))
    #print(Naif("attempt"))