# Kybernetická bezpečnost a kvantové počítače

## Kvantový počítač
* Je výpočetní zařízení, které využívá principy kvantové mechaniky pro zpracování informací
### Qubit
* Je základní jednotkou kvantových počítačů
* Dokáže existovat v jeden moment ve více stavech (může mít **hodnotu 0, 1, nebo kombinaci obou zároveň**)
* Díky této technologii dokáže kvantový počítač řešit extrémně složité úkoly v řádech minut / vteřin
* Funguje na principu **Superpozice**
![Qubit](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Bloch_Sphere.svg/220px-Bloch_Sphere.svg.png)
## Superpozice a její vliv na výpočty kvantového počítače
* **Superpozice** je kvantový jev, kdy **qubit** může existovat ve více stavech současně, než jen v jednom konkrétním stavu
* Umožňuje kvantovým počítačům provádět paralelní výpočty (klasický počítač zpracovává jeden požadavek po druhém)
### Změna stavu qubitu
* Pokud by byl změněn stav jednoho qubitu, okamžitě se změní i stav toho druhého i kdyby qubity byly vzdáleny miliony kilometrů 
* Zdá se, že tento jev porušuje některé zákony  fyziky, jako je přenos informací rychleji než světlo

## Entanglement (kvantové propletení)
* **Kvantové propojení** je stav, kdy jsou dva nebo více qubitů vzájemně propojené tak, že stav jednoho qubitu závisí na stavu druhého, bez ohledu na vzdálenost mezi nimi
* Umožňuje rychlý přenos informací mezi qubity
* Využívá se v kvantových algoritmech (např. Shorův a Groverův) 

## Shorův algoritmus a ohrožení současných kryptografických metod

* **Shorův algoritmus** je kvantový algoritmus, který dokáže rozložit složitá čísla na prvočísla ve velmi efektivním čase
* Je efektivnější než nejlepší známé klasické algoritmy
## Ohrožení bezpečnosti
### RSA
* Je jedním z nejznámějších a nejpoužívanějších algoritmů pro šifrování a digitální podepisování, který se používá k ochraně dat v digitálním světě
* Je velmi bezpečné, protože je obtížné faktorizovat velká čísla na prvočísla (klasickým počítačům by vyřešit tento problém trvalo velmi dlouhou dobu)
### ECC
* Je metoda šifrování, která využívá matematiku eliptických křivek k vytvoření veřejného a privátního klíče pro asymetrické šifrování, digitální podpisy a další kryptografické operace
### Využití kvantových počítačů
* Kvantové počítače mohou využít **Shorův algoritmus**, faktorizace čísel by byla téměř okamžitá
* Znamenalo by to prolomení bezpečnosti současných šifrovacích metod
* Mohlo by to mít obrovský dopad na bezpečnost online komunikace, bankovnictví, vládní tajemství, atd. 



## Groverův algoritmus a zrychlení hledání v nelineárních strukturách 
* **Groverův algoritmus** je kvantový algoritmus, který zrychluje hledání v neuspořádaných nebo nelineárních databázích
* Tento algoritmus dokáže hledání výrazně zrychlit

## Rizika kvantový počítačů pro RSA nebo ECC
* Kvantové počítače mohou použít algoritmy jako např. Shorův k prolomení šifrování založeného na složitosti fatorizace čísel **(RSA)**
* Dnes je RSA a ECC považována za bezpečná, protože prolomení šifrování by pro klasické počítače trvalo příliš dlouho

## Post-kvantové šifrování a algoritmy pro kvantově odolnou bezpečnost
* **Post-kvantové šifrování** je oblast kryptografie, která se zaměřuje na vývoj šifrovacích metod, které budou bezpečné i proti útokům kvantových počítačů
### Vývoj kryptografických algoritmů pro bezpečnost
* Vyvíjejí se algoritmy odolné např. proti **Shorově algoritmu**  jako jsou:
	* **Lattice-based** kryptografie
	* **Code-based** kryptografie
	* **Hash-based** šifrování
* Tyto metody nevyužívají faktorizaci čísel, nebo diskrétní logaritmy
* Jsou odolné proti kvantovým útokům

## IBM Quantum,  Google Quantum AI a Microsoft Quantum

* Existuje několik významných projektů zaměřených na vývoj kvantových počítačů
### IBM Quantum
* Vyvíjí kvantové počítače a umožňuje k nim přístup přes cloud své platformy **IBM Quantum Experience**
### Google Quantum AI
* Pracuje na kvantových počítačích
* Dosáhl významného pokroku s procesorem **Sycamore**, který v roce 2019 zvádl výpočet, který by klasickým počítačům trval tisíce let
### Microsoft Quantum
* Vyvíjí kvantovou technologii prostřednictvím **Azure Quantum** 
* Kombinuje různé kvantové technologie pomocí cloudu

## Výhody a nevýhody kvantových počítačů ve srovnání s klasickými počítači pro různé aplikace

### Výhody:
* Značné zrychlení řešení problémů (simulace molekul, optimalizace, kryptografie)
* **Superpozice** a **propletení** umožňuje zrychlit řešení problémů
### Nevýhody:
* Zatím nejsou dostatečně silné pro široké komerční využití
* Vyžadují extrémně nízké teploty
* Nákladnost
* Složitá technologie

## Vliv kvantové kryptografie (QKD) na budoucnost bezpečné komunikace 
### QKD 
* Využívá principy kvantové mechaniky k zabezpečení komunikačních kanálů
* Umožňuje dvěma stranám si bezpečně vyměnit šifrovací klíče, které jsou chráněny před pokusy o odposlech
* Jakýkoliv pokus o zachycení kvantového stavu během přenosu klíče by změnil jeho stav, což okamžitě odhalí pokus o útok

### Bezpečnost
* QKD nabízí neuvěřitelně silnou úroveň bezpečnosti, díky využití neporušitelných kvantových principů
* Je tudíž bezpečná i proti útokům ze strany kvantových počítačů

![Kvantový počítač](https://imgs.sector.sk/files/novinky/0/2018/1-10-14-8-92/ako-vyzera-kvantovy-pocitac-image-511.jpg)

**Zdroje:**
[Kvantový počítač – Wikipedie](https://cs.wikipedia.org/wiki/Kvantov%C3%BD_po%C4%8D%C3%ADta%C4%8D)
[Quantum key distribution - Wikipedia](https://en.wikipedia.org/wiki/Quantum_key_distribution)
[Google Quantum AI](https://quantumai.google/)
[Microsoft Quantum Overview – Quantum Machines | Microsoft Azure](https://azure.microsoft.com/en-us/solutions/quantum-computing/)
[ChatGPT](https://chatgpt.com/)
