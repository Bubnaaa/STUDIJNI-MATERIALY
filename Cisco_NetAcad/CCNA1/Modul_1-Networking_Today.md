# 1. Modul - Networking today
## Základní pojmy:
### Host, Server, Klient
-   **Host = koncové zařízení**, které komunikuje v síti (PC, telefon atd.).
-   Host má přidělenou **IP adresu** – identifikuje zařízení v síti.
-   **Server** = poskytuje služby (např. web, e-mail) klientům.
-   **Klient** = žádá o služby serveru (např. webový prohlížeč).
-   **Jeden počítač může být zároveň klient i server**, pokud má oba typy softwaru
### Peer-to-Peer (P2P)
-   P2P síť: Každé zařízení může být klient i server
-   Používá se často v domácnostech/malých firmách.   
-   **Výhody**: jednoduché, levné, nenáročné na zařízení.
-   **Nevýhody**: horší zabezpečení, bez centrální správy, špatně škálovatelné.
### Intermediary Devices
- Spojují end devices a směřují data sítí
- Např.: router, switch, firewall,... 
### Network Media
- Typy:
	- Kovové
	- Optické
	- Bezdrátové
## Topologie a komponenty
### Network Interface Card (NIC)
- Fyzicky připojuje zařízení do sítě
### Physical port
- Konektor na síťovém zařízení který připojuje zařízení do sítě
### Interface
- Porty na síťovém zařízení, které připojují do individuálních sítí

### Fyzická topologie
- Ukazuje fyzické umístění kabelů a zařízení
### Logická topologie
- Ukazuje zař., porty, IP adresy, MAC adresy,...

## Základní druhy sítí
### LAN
- Místní síť která propojuje zařízení (Doma, ve školách, ve firmách,...)
### WAN
- Propojení více LAN
### Internet
- Celosvětová síť sítí tvořená propojenými LAN a WAN
	- #### Orgranizace dohlížející na internet:
		- IETF
		- ICANN
		- IAB
### Intranet
- Soukromá síť organizace (propojení LAN a WAN v rámci jedné organizace)
### Extranet
- Rozšíření Intranetu pro externí uživatele, kteří potřebují přístup k některým datům organizace
- Funguje přes internet, s autentizací a šifrováním 
## Připojení k internetu
### Pro běžné uživatele
- DSL - Vysoká rychlost, přes telefonní linku
- Kabelové připojení - Přes TV, rychlé, stabilní
- Mobilní internet - Přes mobilní síť
- Satelitní internet - Pro místa bez kabelu, s vysokou latencí
- Dial-up - Zastaralé, pomalé
### Pro firmy
- Leased line - Vyhrazená linka, stabilní, drahá
- Metro Ethernet - Ethernet přes WAN
- Bussines DSL 
- Satelit - v odlehlých oblastech
### Konvergence sítí
- Vše po jednom kabelu
#### Dříve:
-   Samostatné sítě:    
    -   Telefonní        
    -   Datová        
    -   Video       
#### Dnes:
   -   Jedna síť přenáší hlas, video i data       
    -   Nižší náklady, jednodušší správa
    -   Vyžaduje jednotné standardy a protokoly
## Síťová architektura
- Kombinace fyz. infrastruktury a protokolů
- Pro správný provoz moderní sítě musí architektura splňovat:
	- Fault tolerance (odolnost vůči chybám)
	- Scalability (škálovatelnost)
	- Quality of services (QoS)
	- Security 
### Fault tolerance 
- Síť musí pokračovat v provozu i po výpadku
- Funguje díky redunanci - Více cestám k cíli 
- Pomáhá i packet switching, kde jsou data rozdělena do packetů a mohou jít různými cestami
### Scalability
- Síť se dá snadno rozšířit o nové uživatele nebo celé podsítě bez negativního dopadu na výkon
- Zajištěno díky protokolům a standardům
### QoS
- Důležitá pro přenos hlasových hovorů, videa nebo živého přenosu 
- Zajišťuje, že např. VoIP má přednost v síti před méně důležitými
### Security
#### Fyzická a síťová infrastruktura
- Zamezení neobrávněnému přístupu
- Ochrana přistupových bodů
#### Informace a data
- Ochrana dat před zneužitím, změnou, ztrátou
#### 3 základní pilíře bezpečnosti
- Confidentiality - Data jen pro oprávněné osoby
- Integrity - Data nebyla změněna
- Avivability - Služby jsou kdykoliv přistupné
## Trendy v sítích
### BYOD (Bring Your Own Device)
- Uživatelé používají vlastní zařízení na síťové připojení
- Výhodou je flexibilita a nižší náklady
### Online spolupráce
- Společná práce online
- Umožňuje týmovou práci na dálku
### Video komunikace
- Vyžadují QoS a vyšší šířku pásma
### Cloud computing
- Ukládání dat na vzdálených serverech
- Typy cloudů:
	- Public
	- Private
	- Hybrid
	- Community
### Smart Home Technologie
- Propojení domácích spotřebičů
- Ovládání hlasem nebo smartphonem
- Propojeno přes domácí síť
### Powerline networking
- Síť přes elektrické zásuvky
- Neplést s datovými sítěmi
### WISP a Wireless Broadband
- WISP - Připojení k internetu bez kabelu
- Wireless Broadband - Využití LTE/5G

## Bezppečnostní hrozby
### Externí
- Pochází z internetu nebo jiných vnějších sítí
### Interní
- Způsobené uživateli uvnitř organizace
## Bezpečnostní řešení
### Domácí sítě
- Antivirus, Spyware
- Základní firewall
### Firemní sítě
- Dedikovaný firewall
- ALC - Řízení přístupu podle IP adres
- IPS - Detekce a blokace pokročilých útokú
- VPN - Vzdálený přistup