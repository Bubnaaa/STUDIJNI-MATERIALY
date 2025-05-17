# 4. Modul - Fyzická vrstva (L1)
## Typy připojení
### Kabelové připojení
- Používá se např. v kancelářích na zařízení jako PC, tiskárny, jsou připojena ke switchi pomocí ethernet kabelu
- Vyžaduje Ethernet NIC
### Bezdrátové připojení
- Využívá rádiové vlny a připojuje zařízení pomocí bezdrátového přístupového bodu
- Vyžaduje WLAN NIC
## Fyzická vrstva
### Funkce
- Přijímá frame z linkové vrstvy (L2) a zákoduje ho do signálů
- Signály se odesílají přes elektrický nebo optický kabel nebo přes rádiové vlny
- Cílové zařízení dekóduje signály zpět do bitů a předá je linkové vrstvě
### Přenos
1. Data z aplikace jsou postupně zabalena do segmentu, IP packetu a do framu 
2. Fyzická vrstva převede frame na sérii bitů
3. Bity se přenesou po médiu (kabel, vzduch) 
4. Cílové zařízení zachytí bity, znovu složí do framu, IP packetu, segmentu a dat 
## Standardy L1
- ISO - Standardizační organizace
- TIA/EIA - Telekomunikační asociace
- ITU - T Mezinárodní telekomunikační unie
- ANSI - Institut elektrotechniky
## Fyzické komponenty
- Ethernet kabely (Cat5e, Cat6)
- Síťové karty
- Konektory RJ-45
- Porty na routerech nebo Switchích

## Kódování
- Převádí bity na vzory signálů, které lze přenést a rozpoznat
### Manchester kódování
-  0 -> vysoké napětí -> nízké napětí (Přechod v polovině bitu)
- 1 -> nízké napětí -> vysoké napětí 
- Používal se v 10BASE-T Ethernetu (10Mb/s)
- Dnešní sítě požívají složitější kódování, kvůli efektivitě
## Signálování
- L1 vytváří elektrické, optické nebo rádiové signály, které přestavují 1 nebo 0
- **Elektrický impuls** - Přes měděné kabely
- **Světelný impuls** - Optická vlákna 
- **Rádiové vlny **- U bezdrátových sítí
- Definice toho jak vypadá 1 a 0 jsou určeny standardem

## Bandwidth (Šířka pásma)
- Množství dat, které může přenést médium za jednotku času
- Měření:
- kbps, Mbps, Gbps
### Ovlivňující faktory:
- Typ a kvalita média
- Použité signálování
- Fyzikální vlastnosti

## Latency
- Časové zpoždění, kolik času trvá datům dostat se z bodu A do B
- Zvyšuje se se vzdáleností a počtem zařízení na cestě
## Troughput
- Skutečné množství dat přenesené za jednotku času
- Bývá nižší než teoretická šířka pásma
## Goodput
- Množství užitečných dat (Bez hlaviček, patiček,...)
- Vždy nižší než troughput

# Měděná kabeláž
### Signál
- Přenášen jako elektrické impulzy, při delší vzdálenosti zeslabují
- 
### Výhody
- Levný, snadno instalovatelný, nízký elektrický odpor
### Nevýhody
Omezená vzdálenost, náchylnost na rušení
### Rušení
- EMI a RFI (zářivky, motory, rádia)
- Crosstalk - Rušení mezi sousedními vodiči
### Ochrana proti rušení
- Stínění vodičů
- Zkroucené páry
- Správný návrh a instalace kabeláže 
## UTP Kabeláž
### Vlastnosti
- 4 páry měděných vodičů, kroucené dohromady
- Malý a flexibilní - Snadná instalace
- Bez stínění, spoléhá se na:
	- Kompensaci - Protisměrné magnetické pole se ruší
	- Různý počet zatočení u každého páru - Minimalizace crosstalku
### Standardy a Konektory
| Kategorie | Rychlost |
|--|--|
| Cat3 | Do 10 Mbps |
|Cat5|100 Mbps|
|Cat5e|1 Gbps|
|Cat6|10 Gbps|
|Cat7/8|10-40 Gbps|

- Konektor RJ-45:
	- Správné zapojení a zakončení je kritické-Degradace signálu
	- U správného konektoru: Plášť zasahuje do konektoru, páry jsou zkráceny jen minimálně
### Typy UTP kabeláže
#### Přímý
host->switch, switch->router
#### Křížený
host->host, switch->switch
- Dnes nahrazeno auto-MDIX
#### Rollover
- Pro konzolové připojení k Cisco zařízením
### Standardy T568A a T568B
- T568A
	- Zelený pár na pinech 1-2
- T568B
	- Oranžový pár na pinech 1-2
- Přímý kabel - Oba konce A-A nebo B-B
- Křížený kabel - Jeden konec A, Druhý B
## Fiber optic kabeláž
### Vlastnosti
- Nejvyšší rychlost a dosah ze všeh médií
- Imunní vůči EMI a RFI rušení
- Přenáší světelné impulsy -> Bitová data
- Jádro z čistého skla, velmi tenké
### Typy vláken
| Typ | Vlastnosti |Dosah|Světelný zdroj|
|--|--|-|-|
| SMF (Single-mode) | Malé jádro |100+km|Laser|
| MMF (Multi-mode)  | Větší jádro |Do 500km|LED|

## Patch kabely
- Pro jednoduché propojení mezi zařízeními
- Barvy plášťě:
	- Žlutá - single mode
	- Oranžová - multimode

## Bezdrátová média
- Přenáší elektromagnetické signály, které reprezentují binární dat
- Vysoká mobilita
### Nevýhody
- Dosah
- Rušení
- Bezpečnost
- Sdílené médium
### Typy
#### Wifi
- IEEE 802.11
- Bezdrátová LAN
- Využití CSMA/CA
#### Bluetooth
- IEEE 802.15
- Komunikace na 1-100m 
#### WiMAX
- 802.16
- Širokopásmový internet
#### Zigbee
- 802.15.4
- Nízká spotřeba, Pro IoT zařízení
