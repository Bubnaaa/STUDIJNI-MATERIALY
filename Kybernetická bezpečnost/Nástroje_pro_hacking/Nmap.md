 # Nmap
- Je nástroj pro:
	- Skenování portů
	- Zjištění služeb a operačního systému
	- Detekce zranitelnosti (NSE scripty)
- Příkaz pro instalaci je: sudo apt install nmap

## Základní příkazy
| Příkaz | Funkce |
|--|--|
| nmap 192.168.1.1 | Základní sken IP adresy |
| nmap -sS 192.168.1.1 | Poloskrytý TCP SYN sken (nejčastější) |
| nmap -sV 192.168.1.1 | Zjistí verze služeb (např. Apache 2.4.49) |
| nmap -O 192.168.1.1 | Pokusí se zjistit OS |
| nmap -p 22,80,443 192.168.1.1 | Sken pouze vybraných portů |
| nmap -p- 192.168.1.1 | Sken všech 65535 portů |
| nmap -A 192.168.1.1 | Agresivní sken: verze, OS, traceroute, skripty |
| nmap --script vuln 192.168.1.1 | Spustí skripty pro detekci známých zranitelností |
| nmap -oN vysledek.txt 192.168.1.1 | Uložení výsledků |

## Skenování portů
- je proces, při kterém se zjišťuje, které síťové porty na cílovém zařízení jsou otevřené a dostupné pro komunikaci
