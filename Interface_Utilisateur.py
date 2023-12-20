import os, time
from Algorithme_Recherche import *

## ATTENTION
# La base de données originel et le script "Algorithme_Recherche.py" doivent
# être dans le même dossier parent que le script pour le bon fonctionnement du programme
# (sauf dans l'interface graphique où vous pouvez ouvrir n'importe que base de données
# via l'explorateur de fichier)


File_BD = "BaseDonneesV2.txt" # La Base de Données Originel
typealgo = "Naif"

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
except:
    try:
        repertoire = os.path.realpath(__file__)
        cheminBS = os.path.join(repertoire, File_BD)
        BaseD = open(cheminBS, "r+", encoding='utf-8')
    except:
        print("Base de données non trouvée, merci de bien la mettre dans le même dossier que le script")

cheminBS = os.path.join(repertoire, File_BD)
BaseD = open(cheminBS, "r+", encoding='utf-8')

with BaseD as Base:
    """
    Création du tableau de tableaux BS permettant de faciliter la recherche
    des mots demandés dans les algorithmes Naif et de Boyer-Moore en divisant
    la base de données en phrases puis en caractères

    Sortie : None - Création du tableau de tableaux BS, la base de données
                    par effet de bord
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
    Va chercher les lignes avec les indices dans tab

    tab - lst - Tableau avec les indices des lignes contenant le mot recherché

    Sortie : str - Les lignes contenant le mot recherché
    """
    text = ''
    for i in tab:
        text += f"[l.{i}] "
        for j in range(1,len(BS[i])):
            text += BS[i][j]
        text += "\n\n"
    return text

##
##INTERFACE GRAPHIQUE
##

#"""
from tkinter import *
from tkinter.filedialog import askopenfilename

cheminlogo = os.path.join(repertoire, "Logo.ico")

def get_input():
    """
    Cherche le mot qu'on veut trouver dans la base de données
    puis l'affiche dans "reponse"
    
    {global} typealgo - str - Le type d'algorithme qu'on
                            utilise

    Sortie : None : Récupère le mot qu'on veut chercher, 
                    trouve les indices correspondants via
                    les algorithmes de recherche puis affiche
                    les lignes correspondantes aux indices
                    trouvées par effet de bord
    """
    global typealgo
    output = []
    mot = entry.get()
    if mot != "" and mot != " ":
        print(f"Mot trouvé : {mot}")
        
        if typealgo == "Naif":
            start = time.time()
            for i in range(len(BS)):
                if Naif(mot,BS[i]):
                    output.append(i)
            end = time.time()

        elif typealgo == "Boyer Moore Horspool":
            start = time.time()
            for i in range(len(BS)):
                if Boyer_Moore_Horspool(mot,BS[i]):
                    output.append(i)
            end = time.time()
            
        temps = end - start
        if len(output) != 0 :
           reponse.delete(1.0,END)
           if len(output)> 600:
               reponse.insert(END,f"Il y a trop de correspondance pour {mot}, ({len(output)})\nMerci d'etre plus precis dans le choix de votre mot pour une meilleur détection")
               reponse.config(fg="#D05962")
               window.after(200, lambda: reponse.config(fg="black"))
           else:
                reponse.insert(END,f"Correspondance pour {mot}:\n{HorsTab(output)}")
                reponse.config(fg="#5B8F75")
                window.after(200, lambda: reponse.config(fg="black"))
           print(f"{len(output)} Réponse trouvé en {temps:.2}ms")
        else:
            reponse.delete(1.0,END)
            reponse.insert(END,f"Il n'y a aucune correspondance pour {mot}")
            reponse.config(fg="#D05962")
            window.after(200, lambda: reponse.config(fg="black"))
            print(f"Aucune correspondance en {temps:.2}ms")
    else:
        reponse.delete(1.0,END)
        reponse.insert(END,f"Je n'aime pas les espaces désolé\nJe préfère les mots")
        reponse.config(fg="#EEF3F1")

def changer_chemin():
    """
    Change le chemin de la base de données

    {global} File_BD - str - Le nom du fichier de la base de données
    {global} BS - tab - La base de données en tableaux de tableaux

    Sortie : None : Demande le chemin de la nouvelle base de données
                    puis modifie la base de données en tableaux de tableaux
                    et modifie le nom du fichier de la base de données par
                    effet de bord
    """
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
    """
    Change l'algorithme utilisé

    {global} typealgo - str - Le type d'algorithme qu'on
                            utilise

    Sortie : None : Change l'algorithme utilisé par Naif
                    via effet de bord
    """
    global typealgo
    typealgo = "Naif"
    BaseSelection.config(text=f"Base de données Sélectionné :\n{File_BD}\nAlgorithme utilisé : {typealgo}", fg="green")
    window.after(200, lambda: BaseSelection.config(fg="black"))
    print("Agltorithme Naif Choisi")

def changer_algoBM():
    """
    Change l'algorithme utilisé

    {global} typealgo - str - Le type d'algorithme qu'on
                            utilise

    Sortie : None : Change l'algorithme utilisé par Boyer
                    Moore via effet de bord
    """
    global typealgo
    typealgo = "Boyer Moore Horspool"
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
except:
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
menu_algo.add_command(label="Boyer_Moore_Horspool", command= changer_algoBM)
newmenu.add_cascade(label="Algorithme", menu= menu_algo)

window.config(menu=newmenu)

##MISE EN PLACE DES GROUPES
frame = Frame(window, bg= "#c4c4c4", bd=1)
sframe = Frame(frame,bg= "#c4c4c4", bd=1, relief= SUNKEN)
output = Frame(frame,bg= "#c4c4c4", bd=1)

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

if __name__ == "__main__":
    print("Script Fini")