# Proměnné JS 2.0.1
* JS rozlišuje velká a malá písmena proměnných tudíž např.: **Test**, **test**, **TEST** - každou z nich bude JS považovat za jinou

* Existuje sada vyhrazených slov, které nelze použít jako název proměnné
## Deklarování proměnných
* Používáme příkaz: **var** nebo **let** např.:

			var height;
			console.log(height);	-> undefined
			console.log(weight);	-> Uncaught ReferenceError: weight is not defined

* **let** nám zabraňuje deklarovat jinou proměnnou se stejným názvem, naopak **var** nám tuto deklaraci umožňuje

## Přiřazování hodnot k proměnným

* Používáme operátor **=** např.:

		let height = 180;
		let anotherHeight = height;
		let weight;
		weight = 70;
		console.log(height);	-> 180
		console.log(anotherHeight);	-> 180
		console.log(weight);	-> 70

## Změna hodnot proměnných
* Zapisuje se:

		let steps = 100;
		console.log(steps); -> 100

		steps = 120;
		console.log(steps); -> 120

		steps = steps + 40;
		console.log(steps); ->160

* Můžeme také skládat proměnné do sebe: 

		let greeting = "Hello!";
		let counter = 100;
		greeting = greeting + counter;
		console.log(greeting); -> Hello!100

## Konstanty

* Příkazem **const** vytvoříme jakýsi "kontejner" podobných proměnným
* Používají se pro ukládání hodnot, ale jakmile do nich byly hodnoty zadány při přiřazování hodnot, už je nelze upravovat

		const  greeting = "Hello!";

Ale tento příkaz:

		const  greeting;
		greeting = "Hello!"
			-> Uncaught SyntaxError: Missing initializer in const declaration
