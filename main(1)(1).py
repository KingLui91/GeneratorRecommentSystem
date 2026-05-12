
#KONSTANTEN --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Fragen des Programms an den Anwender
question_1 = "Hallo, wilkommen beim GRS, Genset Recomment System. Nach welchem Kriterium möchtest du dein Aggregat suchen? Die Kriterien sind Preis (pr), Leistung (pw)."
question_2 = "Dies ist das Aggregat entsprechend deiner Preisvorstellung. Möchtest du ein Aggregat entsprechend einer Leistungsangabe suchen? Ja (y) oder nein (n)"
question_3 = "Dies ist das Aggregat, das deinen Leistungsvorstellungen enspricht. Möchtest du einen Vorschlag anhand des Preis-Leistungs-Verhältnises haben? Ja (y) oder nein (n)"
question_4 = "Das sind die Vorschläge, die das GRS mit unserer Produktliste dir anbieten kann."
question_5 = "Dies ist das Aggregat entsprechend deiner Leistungsvorgabe + Reserveleistung 30%. Möchtest du ein Aggregat entsprechend einer Preisvorstellung suchen? Ja (y) oder nein (n)"
question_6 = "Dies ist das Aggregat, das deinen Preisvorstellungen enspricht. Möchtest du einen Vorschlag anhand des Preis-Leistungs-Verhältnises haben? Ja (y) oder nein (n)"

# Liste in der alle Aggregate enthalten sind [name, price, power]
product_list = [["name 1", 100, 1], ["name 2", 100, 1], ["name 3", 100, 1]]
# 
all_gensets = []
for genset in product_list:
    new_genset = Genset_node()
    new_genset.name = genset[0]
    new_genset.price = genset[1]
    new_genset.power = genset[2]
    all_gensets.append(new_genset)
    #all_gensets.sort(key=lambda x: x.name)

# Ende des Programms
pgr_fin = "Ende des Programms. Danke für die Nutzung das GRS"

#Anwender-Parameter
user_search_argument = ""

#DEFINITION DER FUNKTIONEN, KLASSEN UND ALGORITHMEN -------------------------------------------------------------------------------------------------------------------------------
# Die Klasse Genset definert die Eigenschaften eines Aggregats
class Genset_node:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.power = 0


# Funktion des Algorithmus der die Produktliste durchsucht anhand der übergebenen Suchkritärien
def alg_grs(product_list, user_input = 0, search_argument = " "):
    # Hier wird die Produktliste durchlaufen und das Aggregat mit dem naheliegensten Preis oder Leistung t
    liste = []
    if search_argument == "pr":
        for gen in product_list:
            c = user_input / gen.price
            if c >= 0.9 and c <= 1.1:
                liste.append(gen.name)
            else:
                pass    
        return liste

    elif search_argument == "pw":
        for gen in product_list:
            c = (user_input*1.3) / gen.power
            if c >= 0.9 and c <= 1.1:
                liste.append(gen.name)
            else:
                pass    
        return liste
    elif search_argument == "pp":
        print("pp Funktion muss noch implementiert werden.")
    else:
        pass
        
    




#MAIN-PROGRAME ---------------------------------------------------------------------------------------------------------------------------------------------
def main():
    print(question_1)
    user_search_argument = input()
    
    if user_search_argument == "pr":
        print("Bitte gebe den Preis ein. Das GRS sucht dir das Aggregat mit dem naheliegensten Preis aus unserer Produktliste.")
        user_input = int(input())
        print("Suche nach Aggregat mit dem Preis[€]: " + user_input)
        alg_grs(all_gensets, user_input, "pr")
        print(question_2)
        user_input = input()
        if user_input == "n":
            print(pgr_fin)
            pass
        else:
            print("Das GRS sucht dir das Aggregat mit der naheliegensten Leistung + einer Reserveleistung von 30% (pw + 30%) aus unserer Produktliste.")
            alg_grs(all_gensets,"pp")
            print(question_3)
            user_input = input
            if user_input == "n":
                print(pgr_fin)

    if user_input == "pw":
        print("Bitte gebe die Leistung ein. Das GRS sucht dir das Aggregat mit der naheliegensten Leistung + einer Reserveleistung von 30% (pw + 30%) aus unserer Produktliste.")
        user_input = int(input())
        print("Suche nach Aggregat mit der Leistung[kW]: " + user_input)
        alg_grs(all_gensets, user_input, "pw")
        print(question_5)
        user_input = input()
        if user_input == "n":
            print(pgr_fin)
            pass
        else:
            print("Das GRS sucht dir das Aggregat mit dem naheliegendsten Preis aus unserer Produktliste.")
            
            print(question_6)
            user_input = input
            if user_input == "n":
                print(pgr_fin)

    else:
        pass
    print(question_4)
    print(pgr_fin)
    

    
    
main()