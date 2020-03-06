# -*- coding: utf-8 -*-

class animal :
    """
        Cette classe est la classe mère, toutes les classes filles
        héritent des attributs de cette classe
        
    """
    
    def __init__(self, q_nourriture, nbr_pattes, regime_alimentaire):
        self.q_nourriture = q_nourriture
        self.nbr_pattes = nbr_pattes
        self.regime_alimentaire = regime_alimentaire
        
    def __str__(self):
        return "Cet animal a " + self.nbr_pattes + " pattes. Il doit manger " + self.q_nourriture + "g de nourriture et son régime alimentaire est " + self.regime_alimentaire
    
class mammifere(animal):
    
    pass
    
    
class domestique(animal):
    pass
    
    
class animal_marin(animal):
    """
        cette classe regroupe tous les animaux marins, ils ne possèdent aucune patte
        
    """
    
    def __init__(self, q_nourriture, regime_alimentaire, nbr_pattes = 0):
        super().__init__(q_nourriture, nbr_pattes, regime_alimentaire)
        self.nbr_pattes = nbr_pattes
        
    def __str__(self):
        return "C'est un animal marin. Cette animale n'a pas de pattes. Il doit manger " + self.q_nourriture + "g de nourriture et son régime alimentaire est" + self.regime_alimentaire

def animal_factory(espece, q_nourriture, regime_alimentaire, nbr_pattes):
    
    if(espece == "animal"):
        return animal(q_nourriture, regime_alimentaire, nbr_pattes)
    
    elif (espece == "mammifere"):
        return mammifere(q_nourriture, regime_alimentaire, nbr_pattes)
    
    elif (espece == "domestique"):
        return animal(q_nourriture, regime_alimentaire, nbr_pattes)
    
    elif (espece == "marin"):
        return animal_marin(q_nourriture, regime_alimentaire, nbr_pattes)
    
    else :
        print("this class doesn’t exist")



if __name__ == "__main__":
    mon_zoo = {}
    mon_zoo["Poule"] = domestique("200", "4", "Omnivore")
    mon_zoo["Serpent"] = animal("200", "0", "Carnivore")
    mon_zoo["Autruche"] = animal("1000", "4", "Omnivore")
    mon_zoo["Humain"] = mammifere("600", "2", "Omnivore")
    mon_zoo["Pieuvre"] = animal_marin("200", "Carnivore")
    mon_zoo["Sardine"] = animal_marin("50", "Omnivore")
    
    requette = int(input("Que voulez vous faire ?\n 1- Voir l'état du Zoo.\n 2- Voir la nourriture a acheter par semaine.\n 3- Voir le nombre d'animaux marins.\n 4- Pour voir le nombre d'animaux omnivores dans le zoo.\n 5- Pour voir le nombre de pattes dans le zoo.\n"))
    
    
    if (requette == '1'):
        
        for my_key in mon_zoo:
            print(my_key + " " + str(mon_zoo[my_key]))
            print("_____________________________________")
    elif (requette == '2'):
        
    
        q_semaine = 0
            
        for my_key in mon_zoo:
            q_semaine = q_semaine + int(mon_zoo[my_key].q_nourriture)
            
        print("Le zoo doit acheter par semaine " + str(q_semaine * 7) + "g de nourriture")
        
    elif (requette == '3'):
        count = 0
        """
            isinstance renvoie true si l'objet est bien une instance de la classe donnée
        
        """
        for my_key in mon_zoo:
            if (isinstance(mon_zoo[my_key], animal_marin) == 1):
                count = count + 1
                
        print("Nous avons dans notre zoo " + str(count) + " animal/animaux marin(s)")
    
    elif (requette == '4'):
    
        count = 0
        
        for my_key in mon_zoo:
            if (mon_zoo[my_key].regime_alimentaire == "Omnivore"):
                count = count + 1
                
        print("Il y a " + str(count) + " animal/animaux omnivores dans le zoo")
   
    elif (requette == '5'):
    
        pattes = 0
        
        for my_key in mon_zoo:
            pattes = pattes + int(mon_zoo[my_key].nbr_pattes)
                
        print("Il y a " + str(pattes) + " pattes dans le zoo")
        
    else:
        print("Mercie de votre visite")
    
    
    
    
    
    
    