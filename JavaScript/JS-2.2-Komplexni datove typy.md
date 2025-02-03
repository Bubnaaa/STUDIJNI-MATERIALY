# Komplexní datové typy JS 2.2

## Objekty
* Jednou z nejzákladnějších funkcí objektu je **record**
* 
### Record
* Kolekce pojmenovaných polí
* Každé pole má svůj název (nebo klíč) a hodnotu 
* Umožňují nám na jedno místo uložit více hodnot různých **typů** 
* Zápis pomocí **složených závorek**

		let  testObj = {};
		console.log(typeof  testObj);   -> object

* V objektu můžeme definovat další **pole** s jejich hodnotami:

		let testObj = {
		nr: 600,
		str: "text"
		};

* Pole v objektu printujeme takto: 

		console.log(testObj.nr); -> 600
		console.log(testObj.str); -> text
