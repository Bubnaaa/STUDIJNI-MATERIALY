
Tahák pro programovaní v pythonu 

-------------------------------------------------- 

Proměnné, konstanty, Uložení hodnoty 

x = float(5) ←deklarace proměnné x 
b = 59 ←uložení hodnoty 59 do proměnné b 
x, y, z = 4, 9.3, “Martin” ←uložení floatu, integer a stringu do proměnných x, y, z   

-------------------------------------------------- 

Datové typy 

str ←textové řetězce, “pes”, “auto” 
int ←celá čísla, 8, 54, 13, –7 
float ←desetinná čísla(s . místo ,), 2.5, -6.4, 13.95 
bool ←pravdivostní hodnoty, True, False 

-------------------------------------------------- 

Aritmetické operace 

x + y # sčítání 
x - y # odčítání 
x * y # násobení 
x / y # dělení 
x // y # celočíselné dělení 
x % y # dělení se zbytkem 
x ** y # umocňování 

-------------------------------------------------- 

Logické operace 

x == y ←rovno, x == y 
x != y ←nerovno 
x > y ←větší 
x < y ←menší 
x >= y ←větší nebo rovno 
x <= y ←menší nebo rovno 

and ←vypíše True pokud jsou oba výroky pravdivé, 4 < 5 and 4 < 10   
or ←vypíše True pokud je jeden výrok pravdivý, 6 < 5 or 6 < 10  
not ←obratí výsledek, vypíše False pokud je výsledek true, not(4 < 5 and 4 < 10) 

------------------------------------------------- 

Podmínky if, else, elif 

if ←pokud něco, tak vykonej 
elif ←pokud předešlá podmínka nebyla splněna, tak zkus tuto 
else ←skoro stejný princip jako elif 
if b > a: 
  print(b je větší)  

elif a == b: 
  print(a, b jsou stejná)  

else b < a: 
  print(a je větší) 

------------------------------------------------- 

Cykly while, for, break 

For ←od startu opakuj příkazy krok po kroku dokud platí podmínka 
While ←dokud platí podmínka dělej příkazy 
Break ←vyskočí z cyklu a pokračuje dál v programu za cyklem 

------------------------------------------------- 

Seznamy 

list/ výstup print 

print ←vypíše zpravů na obrazovku 
listy ←uspořádané soubory hodnot,  

zvírata = [“pes", “myš”, “býk”] 
print(zvirata) ←vypíše zvířata 
print(zvirata[3]) ←vypíše třetí zvíře 

zvirata[2] = "kočka" 
print(zvirata) ←vymění myš za kočku 

seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5] 
seznam.sort() 
print(seznam) ←seřadí 

------------------------------------------------- 

Def – funkce 
funkce ←pojmenovaný blok příkazů, kterému něco zadáme a pak si ho můžeme zpátky zavolat, 

def funkce(auto = “škodovka”):  
print(“Mám auto “ + auto) 
funkce() 

