# Sniffing & spoofing
## Sniffing
### Definice:
* Technika, při níž útočník zachytává a analyzuje síťový provoz
* Cílem je získat cenné informace (např.: přihlašovací údaje, e-maily, web requesty,...) 
### Typy sniffingu:
* **Pasivní sniffing**
	* Útočník jen naslouchá a monitoruje provoz, nijak jej neovlivňuje
	* Tento typ je účinný pouze v sítích s hubem, který posílá provoz všem zařízením
* **Aktivní sniffing**
	* Útočník manipuluje sítěmi (např. přes ARP spoofing) aby provoz přesměroval skrze sebe přes switch
### Nástroje sniffingu
* **Wireshark** - Analyzátor síťového provozu
* **tcpdump**- Linuxový terminálový nástroj
*  **Ettercap** - Kombinace sniffingu a spoofingu
* **dsniff** - Nástroj pro zachytávání hesel
## Spoofing
### Definice: 
* Podvodná technika, při níž útočník maskuje svou identitu, aby se vydával za jiný subjekt (ID, MAC, DNS,...)
* Jeho cílem je přesměrovat provoz a tím získat důvěrné údaje, nebo vytvořit DoS útok
### Typy spoofingu:
* **IP spoofing** - Mění se IP adresa v odchozích packetech
* **ARP spoofing** - Zfalšovaná ARP odpověď, která přesměruje provoz
* ** MAC spoofing** - Mění se MAC adresa zařízení
* **DNS spoofing** - Útočník upraví DNS odpovědi vedoucí na podvodné servery
* **E-mai spoofing** - Padělání e-mailové adresy odesílatele
* **Web spoofing** - Vytvoření padělaného webu napodobující skutečný
### Nástroje pro spoofing
-   **Ettercap** – Snadné ARP spoofování a MITM útoky
    
-   **Cain & Abel** – Sniffing a spoofing v jednom
    
-   **arpspoof** – Součást balíku dsniff pro ARP spoofing
    
-   **Bettercap** – Moderní nástroj pro MITM, sniffing a spoofing

## MITM (Man In The Middle) - útoky
### Definice:
* Kombinace sniffingu a spoofingu, kde útočník "sedí" mezi dvěma zařízeními a monitoruje provoz, nebo mění data mezi nimi
### Příklady: 
* Přihlašování na nezabezpečené WiFi - Útočník odposlechne přihlašovací údaje
* Online bankovnictví - Útočník změní cílový účet v přenášených datech
