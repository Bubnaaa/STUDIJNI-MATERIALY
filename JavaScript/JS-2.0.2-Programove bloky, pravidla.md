# Programové bloky a jejich pravidla JS 2.0.2
* Rozsah proměnné závisí na tom, kde je deklarována 	
* Programové bloky používáme, když chceme aby se sada příkazů nacházela někde nezávisle ke zbytku kódu 
		
		let  counter;
		console.log(counter);  // -> undefined
		{
			counter =  1;
			console.log(counter);  // -> 1
		}
		counter = counter +  1;
		console.log(counter);  // -> 2

* Programové bloky lze do sebe vnořovat:

		let  counter;
		console.log(counter);  // -> undefined
		{
			counter =  1;
			{
				console.log(counter);  // -> 1
			}
		}
		counter = counter +  1;
		console.log(counter);  // -> 2

* **Odsazování** v JS vůbec nezáleží, avšak zvyšuje čitelnost kódu

## Pravidla

### let a const
* Pokud deklarujeme jakoukoli proměnnou pomocí **let** nebo **const** mimo bloky kódu, proměnné budou **globální** (budou viditelná v celém rozsahu kódu (i uvnitř bloků))

		let  height =  180;
		{
			let  weight =  70;
			console.log(height);  // -> 180
			console.log(weight);  // -> 70
		}
		console.log(height);  // -> 180
		console.log(weight);  // -> Uncaught ReferenceError: weight is not defined

*  Pokud deklarujeme jakoukoli proměnnou pomocí **let** nebo **const** v bloku kódu, proměnná bude **lokální** a bude viditelná pouze uvnitř bloku kódu (její obsah je omezen blokem)

### var
* Pokud deklarujeme proměnnou **var** uvnitř nebo mimo blok, bude **vždy globální**


## Funkce (základ)
* Používáme, když potřebujeme část kódu použít víckrát
* Zapisujeme: 

		function testFunction() {
			console.log("hello");
			console.log("world!");
		}

### var
* Pokud deklarujeme proměnnou var uvnitř funkce, její rozsah bude omezen pouze na vnitřek této funkce (lokálně ve funkci)
