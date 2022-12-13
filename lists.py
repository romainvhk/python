fruits = ['ananas','banane','cerise']
print(fruits)

# Accès en lecture au 0ème élément de la liste.
print(fruits[0])

my_fruit = fruits[0]
print(my_fruit)

# Accès en écriture au 0ème élément de la liste
fruits[0] = 'abricot'
print(fruits)
print(fruits[0])

my_count = len(fruits)

index = 0
if index < my_count:
    print(fruits[index])

index += 1

if index < my_count:
    print(fruits[index])
    print(f'{index =}')

index += 1

if index < my_count:
    print(fruits[index])
    print(f'{index =}')

index += 1

if index < my_count:
    print(fruits[index])
    print(f'{index =}')

# Il est toujours possible d'obtenir la taille d'une liste avec la fonction len().
# Le dernier index d'une liste est taille de la liste -1.

# Ajouter un élément
fruits = ["ananas","banane","cerise","mangue"]
fruits.append("datte")
print(fruits)

# Supprimer un élément sans le récupérer
del fruits[0]
print(fruits)

fruits.remove(0)
print(fruits)

# Supprime et renvoie le dernier élément
last_element = fruits.pop()
print(last_element)

# Supprime et renvoie le premier élément
first_element = fruits.pop(0)
print(first_element)

# Insérer un élément
fruits.insert(1, 'kiwi')
print(fruits)
