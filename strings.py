#heredoc string, il s'agit d'un texte multi-ligne.
my_text1 = """Texte
multi-ligne
abc
foo
bar"""

print(my_text1)

my_text2 = "Texte\nmulti-ligne\nabc\nfoo\nbar"

print(my_text2)

# interpolation avec une f-string
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

# afficher des accolades dans une heredoc f-string
my_texte5 = f"""
{{foo}}
{{bar}}
"""
print(my_texte5)

# Concaténation de chaîne de caractères
my_number2 = 3.14
my_texte6 = "Le nombre PI est " + str(my_number2) + "\nEt le nombre d'or est 1.618"
print(my_texte6)

# Tronquer un float dans une interpolation
# :.4f veut dire 4 chiffres après la virgule
my_number3 = 1 / 3
my_texte7 = f"1 / 3 ~= {my_number3:.4f}"
print(my_texte7)

# Les interpolations acceptent les expressions
# les expressions renvoient un bout de code, des calculs, etc.
my_texte8 = f"1 + 1 = {1 + 1}"
print(my_texte8)

# L'écriture de documentation pour une fonction
def hello(name: str) -> None:
    """Cette fonction dit bonjour à quelqu'un

    name str ce paramètre indique le nom de la personne à saluer
    return None
    """
    print(f"Salut {name}")
