## NORMALIZACE DATABÁZE

= Proces, při kterém se databázové tabulky organizují tak, aby byla data co nejméně redundantní (aby se neopakovala) a zároveň aby byla zachována jejich konzistence (data jsou zapsána podle pravidel)  a integrita (data jsou správná, spolehlivá a platí zadané vztahy).

* Pomůže uspořádat data do více tabulek, které budou vzájemně propojené.
* Pomáhá aby byla databáze efektivní, rychlá a bez zbytečných chyb
* Snažší udržitelnost

### 1. První normální forma 
* Tabulka v databázi je ve 1NF, pokud jsou všechny sloupce atomické (každý sloupec obsahuje jen jednu hodnotu).
* Neobsahuje žádné seznamy a více dat v jednom poli

### 2. Druhá normální forma 
* Tabulka v databázi je ve 2NF pokud splňuje podmínky 1NF a zároveň každý neklíčový atribut závisí na primárním klíči. (Pokud má tabulka složený primární klíč (např. kombinace ID studenta a předmětu) všechny ostatní sloupce (např. známka) musí záviset na tomto klíči.)	

### 3. Třetí normální forma
* Tabulka v databázi je ve 3NF pokud splňuje podmínky 2NF a zároveň žádný neklíčový atribut není závislý na jiném neklíčovém atributu.


## Příklad
* 1NF Tabulka:

| ID studenta | Jméno | Předmět | Známka |
| -- | -- | -- | -- |
| 1 | Petr | Matematika | 2 |
| 1 | Petr | Chemie | 3 |
| 2 | Jana | Matematika | 2 |
| 2 | Jana | Chemie | 1 |
-----------
* 2NF Tabulky:

| ID Studenta | Jméno |
|--|--|
| 1 | Petr |
| 2 | Jana |



| ID studenta | Předmět | Známka |
| -- | -- | -- |
| 1 | Matematika | 2 |
| 1 | Chemie | 3 |
| 2 | Matematika | 2 |
| 2 | Chemie | 1 |
-----------
* 3NF Tabulky:

* Tabulka studentů 

| ID Studenta | Jméno |
|--|--|
| 1 | Petr |
| 2 | Jana |

* Tabulka předmětů

| Předmět | Jméno učitele |
|--|--|
| Matematika | Pan Polák |
| Chemie | Pan White |

* Tabulka zápisů

| ID Studenta | Předmět |
|--|--|
| 1 | Matematika |
| 2 | Chemie |
 
* Tabulka učitelů

| Učitel | Město učitele |
|--|--|
| Pan Polák | Varnsdorf |
| Pan White | Albuquerque |

-   **Tabulka studentů** obsahuje informace o studentech.
-   **Tabulka předmětů** obsahuje informace o předmětech a jejich učitelích.
-   **Tabulka zápisů** spojuje studenty a předměty.
-   **Tabulka učitelů** obsahuje informace o učitelích a jejich městech.
