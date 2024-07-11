a = 10
b = 5

try:
    resultat = a / b
except ZeroDivisionError:  # a = 0
    print("Division par zero impossible.")
except TypeError:  # a = "0"
    print("La variable b n'est pas du bon type.")
except NameError as e:  # on récupére le message d'erreur dans une variable e
    print("Erreur:", e)
#  Erreur: name 'b' is not defined
else:  # le else va retourner un resultat juste si le try réussir
    print(resultat)
finally:  # finally sera éxécuté dans tous les cas
    print("Fin du bloc")

"""
On a une structure qui ressemble un peu à if-elif, mais avec plusieurs except à la place, 
un else pour exécuter le résultat de try et un finally qui sera exécuté dans tous les cas."

Explication
En Python, la structure try-except permet de gérer les exceptions (erreurs) de manière contrôlée. 
Voici une explication détaillée de cette structure :

try : La section où le code susceptible de provoquer une exception est placé.

except : Bloc de code exécuté si une exception se produit dans la section try.

else : Bloc de code exécuté si aucune exception ne se produit dans la section try.

finally : Bloc de code exécuté en tous les cas, que des exceptions se produisent ou non.

"""