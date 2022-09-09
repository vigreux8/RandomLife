#programme principale
import random
import json
import os

"""
TACHE DU JOURS :
    crée class gestion fichier json :
        **le maitre en parent de chaque classe**
        -lire fichier json et returner le contenue 
        -écrie un fichier 
        -print le contenue d'un fichier json
    
    class main 
        -def selection aleatoire
        -def mélange d'activiter de differente liste
    
    **crée 2 table json avec des activiter en demos**
        
    
    

"""

"""
chose a faire : 

    IDEE :
        -Envoiyer un mails a des contact une fois une tache effetuer avec un fichier join preuve(image,screenshot)
        
    
    DONNEE:
 
    -crée fichier google_form pour récuperer les idée des gens
    -crée un convertisseur google_form a json au besoins
    
    AMELIORATION :
   
        
        
    
    FONCTIONALITER :
        -def fichier liste de la journée --> dossier tache --> nom du fichier : date du jours
        -def coder les donner ufc-8 **"voire se que ces
        -def divulguer la tache suivante une fois reussis
        
    class Action_utilisateur :
        -crée une liste personaliser (nom+activiter)
        
        
    class grapghique :
        **apprendre Tkinter ou pygame
        -crée les boutons 
        -associer les boutons a des actions
"""

REPERTOIRE_DATA ="data"


#initialisation fichier :
if not os.path.exists(REPERTOIRE_DATA):
    os.mkdir(REPERTOIRE_DATA)
list_activiter_total =[]

class Liste_createur:
    def __init__(self,nom_fichier = "activiter sans nom"):
        if not "\*.json" in nom_fichier:
            self.nom_fichier = nom_fichier+".json"
        else:
            self.nom_fichier = nom_fichier #egalement le nom du fichier
        self.contenue ={
            "nom" : self.nom_fichier,
            "activiters" : []}
        self.REPERTOIRE = os.path.join(REPERTOIRE_DATA, self.nom_fichier)
        if not os.path.exists(self.REPERTOIRE):
            self.fichier = open(self.REPERTOIRE,"w")
            self.fichier.write(json.dumps(self.contenue))
            self.fichier.close()
        else:
            self.contenue = json.load(open(self.REPERTOIRE))  #si le fichier existe il load les information
        self.nb_activiter = len(self.contenue["activiters"])
        self.list_activiter = self.contenue["activiters"]

    def __repr__(self):
        nom = self.nom_fichier
        nom = nom.split(".")
        return nom[0]

    def add_activity(self,activiters): #rajouter des activiter
        if  print(activiters) : #verifie si la liste contient 1 seul elements
            for activiter in activiters:
                if not activiter in self.list_activiter:
                    self.list_activiter.append(activiter)
        else:
            if not activiters in self.list_activiter:
                self.list_activiter.append(activiters)
        self.ecriture_fichier()

    def remove_activity(self,activiters):
        if activiters:
            for activiter in activiters:
                if activiter in self.list_activiter:
                    self.list_activiter.remove(activiter)
        else:
            if activiters in self.list_activiter:
                self.list_activiter.remove(activiters)
        self.ecriture_fichier()

    def ecriture_fichier(self): #implante le contenue en json dans le fichier
        self.fichier = open(self.REPERTOIRE,"w")
        self.fichier.write(json.dumps(self.contenue)) #écrie le fichier convertie en json
        self.fichier.close()

    def supprimer(self):
        os.remove(self.REPERTOIRE)

    def print_ficher(self):
        self.fichier_read("r")
        print(self.fichier.read())

    def fichier_read(self,etat="r"):
        self.fichier = open(self.REPERTOIRE,etat)

    def nom_fichier_sans_extension(self):
        nom = self.nom_fichier
        return nom.split(".")[0]

class Action_utilisateur:
    # rajouter liste_activiter dans d'autre
    # supprimer activiter
    # crée un fichier personaliser
    # afficher la liste
    # optenir toute les liste disponible OK
    # boucle tant que l'utilisateur rentre des donnée OK

    def __init__(self):
        self.MOT_CLES_DICTIONNAIRE =(("ajouter","ajouter des activiter")
                                     ,("liste_action","Enumere la liste contenue dans un fichier choisis ||"),
                                     ("supprimer","supprimer activiter d'un fichier choisis"),
                                     ("crée_fichier","crée un nouveaux dossier d'activiter"),
                                     ("help","affiche les commande disponible"),
                                     ("supprimer_activité","supression d'activiter"))
        self.REPERTOIRE_DATA ="data"
        self.liste_activiter_total = self.liste_fichier_data_present()
        # bibliotheque d'action et la cles qui les active

    def liste_fichier_data_present(self):
        liste_total_local = []
        if os.listdir(self.REPERTOIRE_DATA):
            for nom_repertoire in os.listdir(self.REPERTOIRE_DATA):  # recuperais la liste des document dans le repertoire
                liste_nom_chemin = [nom_repertoire]
                liste_nom_chemin.append(os.path.join(REPERTOIRE_DATA,nom_repertoire))
                liste_total_local.append(liste_nom_chemin) #[0] nom repertoire, [1]chemins repertoire
        return liste_total_local

    # optenir toute les liste disponible OK
    def enumeration_liste_json(self):
        index = 1
        if self.liste_fichier_data_present():
            for fichierjson in self.liste_fichier_data_present():
                print(f"defis random index: {index} :{fichierjson}")
                index += 1
                 #enumere les liste, avec leur index
        else:
            print(f"defis random index: {index} :{self.liste_fichier_data_present()}")

    #def enumeration_activiter(self):
        #demander le fichier a fouillier
        #entrer dans le fichier et afficher la liste

    # rajouter_des_activiter OK
    def rajouter_activiter(self):
        self.enumeration_liste_json()
        index_utilisateur = self.demande_int()
        activier_a_rajouter = self.boucle_input()
        if len(activier_a_rajouter) >0:
            fichier_selection = self.liste_activiter_total[index_utilisateur]
            fichier = open(fichier_selection[1])
            json_decripte = json.load(fichier)
            for activiter in activier_a_rajouter:
                if not activiter in json_decripte["activiters"]:
                    json_decripte["activiters"].append(activiter)
            fichier = open(fichier_selection[1],"w")
            fichier.write(json.dumps(json_decripte))
            fichier.close()
        self.lire_le_fichier(chemins=self.liste_activiter_total[index_utilisateur][1])

    def supprimer_activiter(self):
        self.enumeration_liste_json()
        index_utilisateur = self.demande_int(raison_demande="supprimer")
        self.lire_le_fichier(chemins=self.liste_activiter_total[index_utilisateur][1])
        activier_a_enlever = self.boucle_input()
        if len(activier_a_enlever) > 0:
            fichier_selection = self.liste_activiter_total[index_utilisateur]
            fichier = open(fichier_selection[1])
            json_decripte = json.load(fichier)
            for activiter in activier_a_enlever:
                if  activiter in json_decripte["activiters"]:
                    json_decripte["activiters"].remove(activiter)
            fichier = open(fichier_selection[1], "w")
            fichier.write(json.dumps(json_decripte))
            fichier.close()
        self.lire_le_fichier(chemins=self.liste_activiter_total[index_utilisateur][1])

    def lire_le_fichier(self,chemins=""):
        if chemins =="":  #si il n'y pas de chemins demande un fichier
            self.enumeration_liste_json()
            index = self.demande_int(raison_demande="a lire")
            fichier_selection = self.liste_activiter_total[index]
            fichier = open(fichier_selection[1],"r")
        else:
            fichier = open(chemins,"r")
        print(fichier.read())
        print()
        fichier.close()


    # recuperais un int et gere les cas d'erreur OK list activiter par defaud
    def demande_int(self,list ="",raison_demande = "modifier"):
        if list == "": #dans le cas ou demande int ces pour une autre list
            list = self.liste_activiter_total
        index_utilisateur = 0
        if len(self.liste_activiter_total) > 1: #si la liste des fichier n'ai pas superieur a 1
            try:
                index_utilisateur = int(input(f"Indiquer l'index du fichier a {raison_demande}: "))-1
            except:
                print("veuilliez saisir uniquement un numeros")
                self.demande_int()
        if  index_utilisateur >= len(self.liste_activiter_total) or  index_utilisateur < 0:
            print(f"veuillier saisir un nombre entre 1 et {len(self.liste_activiter_total)+1} ")
            self.demande_int()
        else:
            return index_utilisateur


        #demander l'index que l'utilisateur veus modifier -1
        #appelle fonction add_activiter sur l'index de la liste

    #boucle tant que l'utilisateur rentre des donnée OK
    def boucle_input(self,message="activiter a rajouter  :"):
        liste = []
        print("Appuier sur ENTRER pour QUITTER")
        while True:
            saisie_utilisateur = input(message)
            if saisie_utilisateur == "":
                break
            else:
                liste.append(saisie_utilisateur)
        return liste

    def help(self):
        #enumer les action possible
        print("*******-Commande Disponible-*******")
        for action in self.MOT_CLES_DICTIONNAIRE:
            print(f"commande : {action[0]} : Action {action[1]}")

    def action(self):
        saisie_utilisateur = input("saisir une action : ")
        if saisie_utilisateur == self.MOT_CLES_DICTIONNAIRE[0][0]: #ajouter
            self.rajouter_activiter()
        elif saisie_utilisateur == self.MOT_CLES_DICTIONNAIRE[1][0]: #enumer
            self.enumeration_activiter()
        elif saisie_utilisateur == self.MOT_CLES_DICTIONNAIRE[4][0]:
            self.help()
        elif saisie_utilisateur == self.MOT_CLES_DICTIONNAIRE[5][0]:
            self.supprimer_activiter()
        #gerer cas erreur de ne mettre uniquement le mot de l'action

class main:
    def __init__(self,utilisateur):
        self.utilisateur = utilisateur


if os.listdir("data"):
    utilisteur = Action_utilisateur()
    utilisteur.lire_le_fichier()
    utilisteur.rajouter_activiter()
    utilisteur.lire_le_fichier()
    utilisteur.supprimer_activiter()
Liste_createur("test1")
Liste_createur("test2")





#il vas crée un dictionnaire avec 2 cles l'index et le nom du fichier
