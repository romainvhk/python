# 2. Entiers consécutifs
# 198, 199, 200, 201 et 202 sont des entiers consécutifs dont la somme est égale à 1000.
# Trouvez d'autres entiers consécutifs dont la somme vaut 1000.

my_list = []
somme = 0 

for i in range (1, 500):
    my_list.append(i)
    somme = sum(my_list)

    while somme > 1000:
        my_list.pop(0)
        somme = sum(my_list)

    if somme == 1000:
        print(my_list)


# Division euclidienne

def euclidienne (dividende, diviseur) :
    my_list = []
    quotient = 0
    reste = 0
    
    for i in range (1, dividende) :
        while i*diviseur <= dividende:
            my_list.append(i)
            i +=1
    
        quotient = my_list[-1]
    
        multiple = quotient * diviseur
        reste = dividende - multiple

    return quotient, reste

print(euclidienne(85, 4));

