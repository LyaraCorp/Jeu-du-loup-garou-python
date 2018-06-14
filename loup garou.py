from random import randint
from string import *
DICO_NBJOUEURS = {8:(2,6),9:(2,7),10:(2,8),11:(2,9),12:(3,9),13:(3,10),14:(3,11),15:(3,12),16:(3,13),17:(3,14),18:(4,14)}

class Loup:

    def __init__(self,pseudos):
        '''Initialisation du loup garou'''
        self.__role=["mj","loup","loup","voyante","sorciere","voleur","chasseur","cupidon"]
        self.__pseudos=pseudos
        self.__nb_player=len(pseudos)
        self.__nom={}
        self.__tue = []
        self.__amoureux = ()
        self.role()
        self.__potion=True
        self.__poison=True

    def role(self):
        '''Defini les rôles des personnes'''
        liste=self.__pseudos.copy()
        tmp=0
        i=0
        while liste != []:
            x=randint(0,len(liste)-1)
            if tmp==0:
                self.__nom[liste[x]] = self.__role[i]
                i+=1
            else :
                self.__nom[liste[x]] = "villageois"
            del(liste[x])

            tmp= (tmp+1)%2

    def nom_role(self):
        return self.__nom

    def nom(self):
        liste=[]
        for nom in self.__nom:
            if self.__nom[nom]!="mj":
                liste.append(nom)
        return liste

    #--------------------------JOUR--------------------------------------------------------------
    def tuer(self):
        phrase = ''
        for i in self.__tue:
            del(self.__nom[i])
            phrase += ', ' + i

        if len(self.__tue)>1:
            return 'Les joueurs ' + phrase + ' sont morts cette nuit'
        elif len(self.__tue) == 1:
            return 'Le joueur ' + str(self.__tue[0]) + ' est mort cette nuit'
        else :
            return "Personne n'est mort cette nuit"

    def assign_capitaine(self,votes):
        '''assigne le role de capitaine en fonction des resultat du votes
        vote = {pseudo:vote}'''
        maxi = []
        for i in votes.keys():
            if votes[i] >= max(votes.values()) :
                maxi.append(i)

        if len(maxi)>1:
            a = randint(0,len(maxi)-1)
            joueur = maxi[a]

        return joueur

    def design_capitaine(self,capitaine):
        '''designe le nouveau capitaine'''
        self.__capitaine = capitaine

    def vote(self,votes):
        '''fait un vote si personne ex oequos : le joueur est stocké dans self.__tue
         sinon on annonce les joueurs a égalité de votes'''

        maxi = []
        for i in votes.keys():
            if votes[i] == max(votes.values()) :
                maxi.append(i)
        if len(maxi) == 1 :
            self.__tue.append(maxi[0])
        else:
            print('Le vote se fera entre : ')
            for j in range(len(maxi)):
                print(' - ',maxi[j])
            x = input('Votre choix : ')
            self.__tue.append(x)



    #-------------------------NUIT---------------------------------------------------------
    def voleur(self):
        '''Fonction voleur'''
        self.nom()
        choix=input("Donner le nom de la personne a voler : ")
        tmp=self.__nom[choix]
        self.__nom[choix]="villageois"
        for nom in self.__nom:
            if self.__nom[nom] == "voleur":
                self.__nom[nom]=tmp

    def cupidon(self):
        '''Fonction cupidon'''
        self.nom()
        nom1= input("Donner le nom du premier amoureux : ")
        nom2= input("Donner le nom du deuxième amoureux : ")
        self.__amoureux=(nom1,nom2)

    def amoureux(self):
        '''Fonction amoureux'''
        print("les deux amoureux se réveillent (",self.__amoureux[0],",",self.__amoureux[1],")")

    def voyante(self):
        '''Fonction voyante'''
        self.nom()
        nom=input("la voyante se réveille et donne le nom de la personne qu'elle veux connaître : ")
        print("Cette personne est : ",self.__nom[nom])

    def loup(self):
        '''Fonction loup'''
        self.nom()
        votes = input('Entrez les votes (loup) : ')
        dico = {votes:1}
        self.vote(dico)


    def sorciere(self):
        '''Fonction sorciere'''
        if self.__potion==True or self.__poison==True:
            self.nom()
            choix=input("la sorciere veut elle faire quelque chose ? : ")
            choix=choix.upper()
            if choix == "OUI":
                popo=input("potion/poison ? : ")
                popo=popo.upper()
                if self.__potion == True and popo=="POTION":
                    print("Est ce que la sorciere veut sauver ",self.__tue[-1],"?",end="")
                    choix2=input(" ")
                    choix2=choix2.upper()
                    if choix2 == "OUI" and len(self.__tue)!=0:
                        del(self.__tue[-1])
                        self.__potion=False
                elif self.__poison == True and popo=="POISON":
                    choix3=input("Qui la sorciere veut elle empoisonné : ")
                    self.__tue.append(choix3)
                    self.__poison=False
                else:
                    print("la sorciere ne fait rien")

    def chasseur(self):
        '''Fonction chasseur'''
        self.nom()
        choix=input("Qui le chasseur veut-il tuer ? : ")
        self.__tue.append(choix)

    def ordre_premiere_nuit(self):
        ordre = ['voleur','cupidon']
        self.__vrai_ordre = []
        for i in ordre :
            if i in self.__nom.values():
                self.__vrai_ordre.append(i)



    def ordre_nuits(self):
        ordre = ['voyante','loup','sorciere']
        self.__vrai_ordre = []
        for i in ordre :
            if i in self.__nom.values():
                self.__vrai_ordre.append(i)



    def appel_fonction(self):
        if "voyante" in self.__vrai_ordre:
            self.voyante()
        if "loup" in self.__vrai_ordre:
            self.loup()
        if "sorciere" in self.__vrai_ordre:
            self.sorciere()
        if "voleur" in self.__vrai_ordre:
            self.voleur()
        if "chasseur" in self.__vrai_ordre:
            self.chasseur()
        if "cupidon" in self.__vrai_ordre:
            self.cupidon()
            self.amoureux()


    def loup_vivant(self):
        return "loup" in self.__nom.values()

    def villageois_vivant(self):
        x=0
        for i in self.__nom.keys():
            if self.__nom[i] != "loup" and self.__nom[i] != "mj":
                x+=1
        return x>=2

if 'name' == 'name':
    loup=Loup(["jean miche","kevin","gertrude","neuf","françois","bourdin","courgette","licorne","tesla",'milka','bite','couille','testicule droit','testicule gauche','ponyta','mamie'])
    print(loup.nom_role())
    loup.ordre_premiere_nuit()
    print('Les loups se réveillent prennent connaissance de leur meute et se rendorment')
    loup.appel_fonction()
    print('fin de la première nuit')
    loupgarou=False
    villageois=False
    while villageois == False and loupgarou == False:
        loup.ordre_nuits()
        loup.appel_fonction()
        loup.tuer()
        votes = input('Entrez les votes : ')
        dico = {votes:1}
        loup.vote(dico)
        loup.tuer()
        if loup.loup_vivant() == False:
            loupgarou=True
        elif loup.villageois_vivant() == False:
            villageois=True
    if loupgarou == True:
        print("Les loups garou ont gagné")
    else :
        print("Les villageois ont gagné")
