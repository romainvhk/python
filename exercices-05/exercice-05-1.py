# exo 5.1
# Ajoutez de la documentation à la fonction suivante et vérifiez
# qu'elle s'affiche correctement en utilisant la fonction help()

# réponse 5.1
def multiplication(a: float, b: float) -> float:
    """Cette fonction multiplie a par b.
    
    a: float ce paramètre indique que le premier nombre est un flottant
    b: float ce paramètre indique que le deuxième nombre est un flottant
    renvoie un flottant
    """
    return a * b
  
help(multiplication)
