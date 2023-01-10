# scope ou la portée des variables

foo = 123 # scope global

def bar ():
    foo = 42 # scope local
    print(foo)

print(foo) # scope global = 123
bar() # scope local de la fonction = 42
print(foo) # scope global = 123

def baz () :
    print(foo)
    lorem = 'ipsum'

baz() # n'ayant pas de foo dans le scope local, python recherch dans le scope global = 123
print(lorem) # appel dans le scope global mais la variable est dans le local de baz()

