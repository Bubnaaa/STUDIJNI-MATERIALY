# Šifrování a útoky na dešifrování
## Klasické šifry
### Caesarova šifra
* Každé písmeno textu se posune o pevný počet míst v abecedě
* Každé písmeno se vždy nahrazuje stejným jiným písmenem
* Snadno prolomitelná, stačí vyzkoušet všech 25 posunů

Např.:
* Slovo KNIHA
* Posun: 3 
* K + 3 = N
* N + 3 = Q
* I + 3 = L
* H + 3 = K
* A + 3 = D 
* Výsledek šifry: NQLKD

### Vigenèrova šifra
* Šifra používá opakující se klíčové slovo, podle kterého se určuje posun jednotlivých písmen
* Vychází principem z Caesarovy šifry

Např.:
* Slovo: TAJNE
* Klíč: KLIC
* Opakovaný klíč na stejný počet písmen, jako slovo které chceme zašifrovat : KLICK
* Posuny: K=10 v abecedě, L=11, I=8, C=2  (A = 0)
* T + 10 = D
* A + 11 = L
* J + 8 = R
* N + 2 = P
* E + 10 = O
* Výsledek šifry: DLRPO

### Atbaš
* Každé písmeno se nahradí zrcadlovým protějškem
* A = Z, B = Y, C = X,...
* Tato šifra je velmi jednoduše prolomitelná

### Transpoziční šifra
* Nezaměňuje znaky, ale jejich pořadí ve slově 
* Možností pro algoritmus měnění pořadí je mnoho

Např.:
* Slovo: TAJNE
* Zašifrované slovo: JTENA

## Moderní kryptografie
### Symetrické šifrování
* Příjemce i odesílatel mají stejný klíč, který slouží pro šifrování a dešifrování
* Bezpečnost závisí na ochraně klíče
#### AES
*   Bloková šifra: zpracovává data po blocích (128 bitů)
*   Klíče mají 128, 192 nebo 256 bitů
*   Provádí řadu kol (např. 10 kol pro AES-128), každé kolo zahrnuje substituce, permutace, míchání a přidání klíče
*  Vysoká odolnost vůči útokům
* Použití: HTTPS, Wi-Fi (WPA2), VPN, diskové šifrování

#### DES / 3DES
* Dnes už se nepoužívá, nahrazen AES
* DES je 56bitový klíč, dnes není považován za bepečný
* 3DES aplikuje DES 3x

### Asymetrické šifrování
* Generují se dva druhy klíčů:
	* Veřejný klíč (pro šifrování)
	* Soukromý klíč (pro dešifrování)
* Je základem digitálních podpisů, certifikátů a šifrované komunikace

#### RSA 
* Je založen na složitosti součinu dvou velkých prvočísel
* Síla spočívá na velikosti prvočísel (běžně 2048 - 4096 bitů)
* Na klasickém počítači zatím neexistuje efektivní algoritmus, který by dokázal tak velká čísla rozložit na součin prvočísel (Kvantové počítače to dokážou prakticky okamžitě)
* Používá se téměř vždy jen k výměně symetrickkého klíče, ne k přímému šifrování zpráv

#### ECC
* je založena na obtížnosti logaritmického problému na eliptických křivkách nad konečnými tělesy
* Použití na zařízeních s omezeným výkonem: Mobily, IoT, čipy, karty,...
* Zatím neexistuje žádný efektivní algoritmus, stejně jako u RSA

## Útoky na symetrické šifry
### Brute force
* Útok, který zkouší všechny možné klíče
* Je náročný n a čas a výko
* Např. AES - 128 má 340 undeciliónů klíčů
### Lineární a diferenciální kryptoanalýza
* Využití toho, že šifry nejsou úplně náhodné
* Aplikováno na historický DES, kvůli tomu dnes není považován za bezpečný

### PBKDF2, bcrypt, scrypt, Argon2
* Odvození klíče pomocí pomalých funkcí
* Používají se u slabých hesel

## Útoky na asymetrické šifry

### Faktorizace RSA modulu n
* Cílem je najít původní prvočísla p a q
* Útoky:
	* Quadratic Sieve
	* GNFS - nejlepší známý algoritmus
* RSA 1024bit je na hraně bezpečnosti, dnes se používá minimálně 2048 bit

### Znovupoužití klíče, chyby ve faktorizaci RSA
* Pokud je veřejný exponent např. 3, a zpráva je krátká, může se dešifrovat i bez znalosti privátního klíče

### Útoky postranními kanály
#### Timing attack
* Sleduje, jak dlouho trvá dešifrování a z toho odhaduje klíčové bity
* Platí po RSA a ECC
#### Analýza spotřeby energie
* Sleduje se spotřeba elektřiny při dešifrování na čipové kartě PC
* Pomocí statistiky a fyziky se zjistí privátní klíč

## Kvantové útoky
### Shorův algoritmus
* Umí rychle faktorizovat velká čísla - proti RSA
* Umí vyřešit logaritmus na epileptické křivce - proti ECC

### Groverův algoritmus
* Umí zrychlit brute-force útok na symetrické šifry
