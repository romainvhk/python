# exo 5.1
# Ajoutez de la documentation à la fonction suivante et vérifiez
# qu'elle s'affiche correctement en utilisant la fonction help()

# réponse 5.1
def multiplication(a: float, b: float) -> float:
    """Cette fonction multiplie deux nombres.
    
    a: float est le premier nombre à multiplier
    b: float est le deuxième nombre à multiplier.
    return float est le résultat de la multiplication
    """
    return a * b
  
help(multiplication)
