# Uppgift 1
# Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.
# def funktions_namn(variabel_namn: datatyp) -> returtyp:
# Exempel: def is_odd(x: int) -> bool:
# Förklaring: Funktionens namn är is_odd och tar en parameter x av datatypen int. Funktionen returnerar en bool.

def is_odd(x: int) -> bool:
    return x % 2 != 0 #När x delas med 2 räknar den ut resten. ! betyder inte lika med i detta sammanhang


print(is_odd(10))  
print(is_odd(5))   
print(is_odd(15))  
print(is_odd(-5))
print(is_odd(-2)) 




