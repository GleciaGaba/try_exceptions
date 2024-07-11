# LBYL / EAFP

# LBYL  - LOOK BEFORE YOU LEAP

# Demander une verification pour une ligne de code qui peut retourner un erreur


"""if "cle" in dict:
    print(dict["cle"])"""

"""
LBYL est un acronyme anglais qui signifie « Look Before You Leap » que l'on pourrait
traduire en français par « Regarde avant de sauter ».

Cet acronyme représente une façon de développer dans laquelle on préfère s'assurer qu'une
 expression ne causera pas d'erreurs avant de l'exécuter, notamment à l'aide de structures conditionnelles.

Ce style va ainsi à l'encontre du style EAFP.

Par exemple, si on souhaite récupérer la valeur associée à une clé dans un dictionnaire :


"""
data = {213: 45000}

if 214 in data:
    print("Salaire de l'employé 214:", data[214])
else:
    print("L'employé #214 n'existe pas")

# -----------------------------------------------------------------------------------------------------------------

#  EAFP - EASIER TO ASK FOR FORGIVENESS THAN PERMISSION

# Mode de gerer les exceptions

"""try:
    print(dict["cle"])
except:
    pass"""

"""
EAFP est un acronyme anglais qui signifie « Easier to Ask for Forgiveness than Permission »,
 que l'on pourrait traduire en français par « Il est plus facile de demander pardon que de demander la permission ».

Cet acronyme représente une façon de développer selon laquelle on considère que le code est valide,
 puis on gère les erreurs si ce n'est pas le cas. Elle va ainsi à l'encontre du style LBYL couramment
  utilisés dans des langages tels que le C.

Voici un exemple de code en style EAFP :

"""

data = {213: 45000}
try:
    salaire_employe = data[214]
except KeyError:
    print("L'employé #214 n'existe pas")

#  Ex:
"""liste = [2, 7, "texte", 4]
total = sum(liste)"""

# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Ici on boucle sur les éléments pour vérifier s'ils sont des nombres, si la boucle trouve un élément qui
# ne pas un nombre il sera supprimé avec la méthode remove()
liste1 = [2, 4, "texte", 4]
for i in liste1:
    if not str(i).isdigit():
        liste1.remove(i)
total1 = sum(liste1)
print(total1)

# EX TRY_EXCEPT

# Ici il n'existe pas la correction du erreur TypeError, mais le code ne va pas retourner un erreur

liste2 = [2, 4, "texte", 4]
try:
    total2 = sum(liste2)
except:
    total2 = 0
print(total2)