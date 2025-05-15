# 3. Modul - Protocols and Models
## Základy komunikace
- 3 základní prvky:
	- Sender (Kdo zprávu odesílá) 
	- Reciever (Kdo zprávu přijímá)
	- Channel (Prostředek, kterým zpráva cestuje)
## Komunikační protokoly
- Určují:
	- Jak se zpráva kóduje
	- Jak se zpráva formátuje
	- Velikost zprávy
	- Načasování
	- Způsob doručení (unicast, broadcast, multicast)
### Typy:
|Typ protokolu  | Popis |
|--|--|
| Network Comunnications Protocols | IP, TCP, HTTP - Umožňují komunikovat v sítích |
|Network Security Protocols|SSH, SSL, TLS - Zajišťují bezpečí dat|
|Routing Protocols|OSPF, BGP - Umožňují routerům si vyměňovat zprávy o cestách co nejvhodnějších pro data|
|Service Discovery Protocols|DHCP, DNS - Automatická detekce nových zařízení, nebo překládání IP adres|

### Funkce:
- Adressing - Identifikuje odeílatele a příjemce zprávy
- Reliability - Zajišťuje spolehlivé doručení dat do cíle
- Flow control - Zajišťuje efektivitu datového toku
- Sequencing - Označování segmentu dat pro následné správné sestavení
- Application interface - Informace pro komunikaci mezi procesy síťových aplikací
-  Error Detection - K určení, zda během přenosu nedošlo k požkození dat

## Protokolové sady
- Sada vzájemně pracujících protokolů které zajišťují síťovou komunikaci
### TCP/IP
| Vrstva | Protokoly |
|--|--|
| Aplikační | HTTP, DNS, FTP, DHCP, SMTP, POP3, HTTP, HTTPS |
|Transportní|TCP, UDP|
|Síťová|IPv4, IPv6, ICMP, OSPF, BGP, EIGRP|
|Data-link|Ethernet, ARP, WLAN|

### Komunikační proces TCP/IP
- Odesílání 
	- HTTP vytvoří zprávu
	- TCP přidá informace o doručení
	- IP přidá adresy sendera a recievera
	- Ethernet připraví data k přenosu
- Přijímání
	- Ethernet zpracuje frame
	- IP zjistí adresy
	- TCP obnoví zprávu
	- HTTP zobrazí obsah v prohlížeči

## Otevřené standardy a organizace
- Veřejně dostupná pravidla pro výrobce, aby jejich zařízení spolu mohla komunikovat
### Organizace
- ISOC
- IAB
- IETF
- IRTF
- IESG
- ICANN
- IANA
- IEEE
- EIA
- TIA
- ITU-T

## Vrstvené Modely
- ISO/OSI, TCP/IP
- Pomáhají nám si představit jak funguje komunikace
### ISO/OSI
- 7 vrstev
	- Fyzická
	- Data-link
	- Síťová
	- Transportní
	- Relační
	- Prezenční
	- Aplikační
### TCP/IP
- 4 vrstvy
	- Network access
	- Internetová
	- Transportní
	- Aplikační
### PDU (Protocol Data Units)
- Na každé vrstvě se data zabalují do jiné "krabice"
- Fyzická - Bity
- Data-link - Frame
- Síťová - Packet
- Transportní - Segment(TCP) / Datagram(UDP)
- Aplikační - Data
### Zapouzdření 
- Proces přidávání informací(hlaviček) na každé vrstvě při odesílání dat
