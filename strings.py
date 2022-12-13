#heredoc string, il s'agit d'un texte multi-ligne.
my_text1 = """Texte
multi-ligne
abc
foo
bar"""

print(my_text1)

my_text2 = "Texte\nmulti-ligne\nabc\nfoo\nbar"

print(my_text2)

# interpolation avec une f-string.
my_number1 = 123
my_texte3 = f"Nombre = {my_number1}"

print(my_texte3)

# interpolation avec une heredoc f-string. Le f-string permet d'afficher la valeur d'une variable.
my_texte4 = f"""
Le nombre
est {my_number1}
foo
"""
print(my_texte4)

# afficher des accolades dans une heredoc f-string.
my_texte5 = f"""
{{foo}}
{{bar}}
"""
print(my_texte5)

# Concaténation de chaîne de caractères.
my_number2 = 3.14
my_texte6 = "Le nombre PI est " + str(my_number2) + "\nEt le nombre d'or est 1.618"
print(my_texte6)

# Tronquer un float dans une interpolation.
# :.4f veut dire 4 chiffres après la virgule.
my_number3 = 1 / 3
my_texte7 = f"1 / 3 ~= {my_number3:.4f}"
print(my_texte7)

# Les interpolations acceptent les expressions.
# les expressions renvoient un bout de code, des calculs, etc.
my_texte8 = f"1 + 1 = {1 + 1}"
print(my_texte8)

# Définition d'une fonction (fonction utilisateur).
# Exemple d'écriture de documentation pour une fonction.
def hello(name: str) -> None:
    """Cette fonction dit bonjour à quelqu'un

    name str ce paramètre indique le nom de la personne à saluer
    return None
    """
    print(f"Salut {name}")

# Appel d'une fonction.
hello('Toto')

# Affiche la documentation d'une fonction.
#help(hello)

# Longueur d'une str, nombre de caractères
my_texte9 = "Lorem ipsum dolor sit ipsum amet consectetur adipisicing elit."
my_number4 = len(my_texte9)
print(my_number4)

# Trouve la position d'une str dans une autre str
my_number5 = my_texte9.find('ipsum')
print(my_number5)


my_number5 = my_texte9.find('ipsum', my_number5 + 1)
print(my_number5)

# Compter le nombre d'occurence d'une str dans une autre str.
my_number6 = my_texte9.count('ipsum')
print(my_number6)

# Remplacer du texte. 
# Attention la variable originelle n'est pas modifiée. Il faut écraser la variable originelle
print(my_texte9.replace('Lorem','Foo'))
my_texte9 = my_texte9.replace('Lorem', 'Foo')
print(my_texte9)

# Eclate une str en liste en utilisant les espaces comme caractère de séparation des éléments.
my_list1 = my_texte9.split()
print(my_list1)

# La fontion len() peut aussi être utilisée avec des lists pour compter le nombre d'éléments.
print(len(my_list1))