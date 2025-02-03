# Datové typy JS 2.1.0
## Příkaz Typeof
* Nám ukáže jaký datový typ proměnná je:
		
		let year = 1990;
		console.log(year) -> 1990;
		console.log(typeof year); -> Number


## Boolean
* Nabývá pouze dvou hodnot: **True** a **False**
	
		let isDataValid = True;
		console.log(isDataValid); -> True

*  Není to povinné, ale často se setkáme s příponou proměnné **is**, aby byl viditelný záměr určování **true** a **false**

## Number

* Hlavní číselný typ JS, který představuje jak zlomky, tak i celá čísla
* Umožňují základní číselné operace jako: 
	* Sčítání
	* Odčítání 
	* Násobení
	* Dělení

			const year = 1990;
			let area = (16*3,14);
			let halfarea = area/2;
			
			console.log(year); -> 1990
			console.log(typeof year); -> Number

* Čísla můžeme také psát v exponenciálním tvaru: místo **9000** -> **9e3**
* Také je můžeme zapisovat v různých číselných soustavách
* Používáme další tři speciální hodnoty: **Infinity**, **-Infinity** a **NaN** (Not a number)

## BigInt
* Nepoužívá se často
* Zapisujeme s příponou **n**
* Umožňuje nám zapisovat celá čísla prakticky libovolné délky 
* Fungují zde stejné Číselné operace jako u **Numbers**, ale rozdíl je při dělení, kdy výsledek je vždy zaokrouhlován **dolů** na nejbližší celé číslo


		let  big =  1234567890000000000000n;
		let  big2 =  1n;
		
		console.log(big);   -> 1234567890000000000000n
		console.log(typeof  big);   -> bigint
		console.log(big2);   -> 1n
		console.log(7n  /  4n);   -> 1n

* Nemůžeme kombinovat **BigInts** a **Numbers**
## String
* Představuje posloupnost znaků tvořících kus textu
* String jako takový je neměnný, pokud se o to pokusíme, vytvoříme úplně nový string

		let  country =  "Malawi";
		let  continent =  'Africa';
		
		console.log(country);   -> Malawi
		console.log(typeof  country);   -> string
		console.log(continent);   -> Africa
		console.log(typeof  continent);   -> string

### Řetězcová interpolace
* Umožňuje nám se stringem zacházet jako se šablonou, do které můžeme umístit hodnoty na vybraná místa
* Používáme znak **$** (Ctrl + Alt + ů) a za ním složené závorky
* V praxi to vypadá takto:


		let  country =  "Malawi";
		let  continent =  "Africa";
		let  sentence =  `  ${country}  is located in  ${continent}.`;
		console.log(sentence);  // -> Malawi is located in Africa.

### Metoda CharAt

* Tuto metodu voláme při vrácení jednoho znaku ze stringu:

		let  river =  "Labe";
		let  character = river.charAt(2);
		console.log(character);  // -> b

* Znaky ve stringu se samozřejmě počítají od nuly:

| L | A | B | E |
|--|--|--|--|
| 0 | 1 | 2 | 3 |

		str.length = 20

		str.slice(1,3) = "ABE"

		
## Undefined

* Má pouze jednu hodnotu -> **Undefined**
* Tuto hodnotu mají všechny proměnné po deklaraci, pokud jim nebyla přiřazena žádná hodnota:


		let declaredVar;
		console.log(typeof declaredVar); -> undefined

## Null

* Konkrétní hodnota, která říká, že daná hodnota neobsahuje **žádnou** hodnotu 
* Rozdíl mezi **Null** a **undefined**:
	* Undefined je přiřazena automaticky
	* Null přiřazujeme my, pokud chceme **podotknout**, že proměnná neobsahuje žádnou hodnotu 
