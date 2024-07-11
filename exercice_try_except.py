
fichier = input("Entrez un fichier à ouvrir: ")

try:
    with open(fichier, "r") as f:
        contenu = f.read()
        print(contenu)
except FileNotFoundError:
    print("Impossible d'ouvrir le fichier: fichier introuvable.")
except Exception as e:
    print(f"Impossible d'ouvrir le fichier: {e}")
