# -*- coding: utf-8 -*-
#cours 3 python
import datetime
import random
import json

class animal :
    """
        Cette classe est la classe mère, toutes les classes filles
        héritent des attributs de cette classe
        
    """
    
    def __init__(self, name, year, month, day):
        self.name = name
        self.year = year
        self.day = day
        self.month = month  
        self.age = datetime.datetime(year=year, month=month, day=day)
        self.sexe = random.choice(["Mâle","Femelle"])
        
    def __str__(self):
        return "Un " + str(self.name) + ". Il est né en " + str(self.age) + " et c est un(e) " + str(self.sexe)
class Farm :

    def __init__(self, name):
        self.name = name
        self.Farm_animals = []
 
    def __str__(self):
        
        out = "Nous avons dans cette ferme\n"
        print (out)
        out=""
        for my_key in self.Farm_animals:
            out += str(my_key)+"\n"
            out += "_____________________________________\n"
            
        return out


if __name__ == "__main__":
    date_farm = datetime.datetime(year=2020, month=1, day=1)
    
    Farm_list = []
    Farm_list.append(Farm("Première ferme"))
    Farm_list.append(Farm("Deuxième ferme"))
    Farm_list.append(Farm("Troisième ferme"))
    Farm_list[0].Farm_animals.append(animal("Mouton", 2020, 3, 5))
    Farm_list[0].Farm_animals.append(animal("Chèvre", 2020, 3, 5))
    Farm_list[0].Farm_animals.append(animal("Serpent", 2020, 3, 5))
    Farm_list[1].Farm_animals.append(animal("Poule", 2020, 3, 5))
    Farm_list[1].Farm_animals.append(animal("Chien", 2020, 3, 5))
    Farm_list[1].Farm_animals.append(animal("Chat", 2020, 3, 5))
    Farm_list[2].Farm_animals.append(animal("Tigre", 2020, 3, 5))
    Farm_list[2].Farm_animals.append(animal("Lion(ne)", 2020, 3, 5))
    Farm_list[2].Farm_animals.append(animal("Dauphin", 2020, 3, 5))
    
    requette = int(input("Vous sélectionnez quelle ferme ?\n"))
    print(Farm_list[requette])
    
#    datetime_today = datetime.datetime.now()
#    print(datetime_today)
#    print(datetime_today.year)
    my_delta = datetime.timedelta(weeks = 0, days = 30, hours = 0, seconds = 0)
#    print("my delta : " + str(my_delta))
#    print("Time delta days : " + str(my_delta.days))
#    new_date = datetime_today + my_delta
#    print(new_date)
    i = 0
    while i < 20:
        Farm_list[0].Farm_animals[0].age = Farm_list[0].Farm_animals[0].age + my_delta
        i+=1
    if int(Farm_list[0].Farm_animals[0].age.year) - int(date_farm.year) >= 1:
            Farm_list[0].Farm_animals.append(animal("Serpent", 2021, 3, 5))
            
    print(Farm_list[requette])

