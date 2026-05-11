
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
def alg_grs(product_list, user_input, search_argument = " "):
    # Hier wird die Produktliste durchlaufen und das Aggregat mit dem naheliegensten Preis oder Leistung t
    if search_argument == "pr":
        pass
    elif search_argument == "pw":
        pass
    else:
        pass





#MAIN-PROGRAME ---------------------------------------------------------------------------------------------------------------------------------------------
def main():
    print(question_1)
    user_search_argument = input()
    
    if user_search_argument == "pr":
        print("Bitte gebe den Preis ein. Das GRS sucht dir das Aggregat mit dem naheliegensten Preis aus unserer Produktliste.")
        user_input = str(input())
    if user_input == "pw":
        print("Bitte gebe die Leistung ein. Das GRS sucht dir das Aggregat mit der naheliegensten Leistung + einer Reserveleistung von 30% (pw + 30%) aus unserer Produktliste.")
        user_input = str(input())
        print("Suche nach Aggregat mit Leistung: " + user_input)
        alg_grs(all_gensets, user_input, "pw")
    else:
        pass
    
    print(question_2)
    print(question_3)
    print(question_4)
    print(question_5)
    print(question_6)
main()