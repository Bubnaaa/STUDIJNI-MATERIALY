# Wireshark
* Je nejpoužívanější open-source nástroj pro analýzu síťového provozu
* Umožňuje zachytávat s zkoumat packety, které procházejí sítí
## Základní funkce 
* Zachytávání živého síťového provozu
* Filtrování paketu podle protokolů (IP, porty, MAC adresy,..)
* Rekonstrukce TCP komunikace
* Analýza šifrovaných protokolů
* Export a import zachycených dat
* Barevné zvýraznění zachycených packetů pro snadnou orientaci 
### Podporované protokoly:
* Je jich více než 2000:
	* Např.: IP, TCP, UDP, ICMP, SMTP, HTTP, HTTPS, FTP, DNS, DHCP, ARP,...
## Princip fungování
* **Zachytávací modul** - používání knihovny **libpcap** na Linuxu, **WinPcap/Npcap** na Windows

* **Dekódovací modul** - Rozpoznává strukturu a význam dat paketů

## Použití Wiresharku
#### Síťová diagnostika
* Zjišťování příčin zpomalení sítě
*   Analýza ztráty paketů nebo chyb v přenosu
    

####  Bezpečnostní analýza

*   Odhalování neobvyklého nebo podezřelého provozu
*   Detekce sniffingu, spoofingu, útoků typu MITM
*   Analýza malware komunikace

#### **Forenzní analýza**

-   Rekonstrukce událostí při bezpečnostním incidentu
-   Export zachycené komunikace pro vyšetřování
    

####  Výuka a testování

*   Učení principů síťových protokolů
*   Simulace reálných situací a útoků
