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
