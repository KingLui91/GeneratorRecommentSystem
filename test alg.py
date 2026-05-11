class Genset_node():
    name = "test"
    price = 50
    power = 100

gens_1 = Genset_node()
gens_1.name = "Genset A"

gens_2 = Genset_node()
gens_2.name = "Genset B"
gens_2.price = 55

gens_3 = Genset_node()
gens_3.name = "Genset C"
gens_3.price = 150

gens_4 = Genset_node()
gens_4.name = "Genset D"
gens_4.price = 50

product_list = [gens_1,gens_2,gens_3,gens_4]

def alg(product_list, price):
    liste = []
    for gen in product_list:
        c = price / gen.price
        if c >= 0.9 and c <= 1.1:
            liste.append(gen.name)
        else:
            pass
            
    return liste
    
print(alg(product_list,50))
