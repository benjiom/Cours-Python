import sys

def write(nom_fichier):
    fichier = open(nom_fichier, "w+")
    fichier.write("Hello word")
    fichier.close();

def read(nom_fichier):
    fichier = open(nom_fichier, "r")
    l = fichier.read()
    print (l)
    fichier.close();

if __name__ == "__main__":
    nom_fichier = input(sys.argv[0])
    write(nom_fichier)
    read(nom_fichier)
    

