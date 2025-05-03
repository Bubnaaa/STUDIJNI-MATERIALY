# Penetrační testování
* Je simulovaný kybernetický útok provedený na počítačový systém, sít, nebo web, za účelem identifikace zranitelnosti
* Cílem není uškodit, ale najít slabiny dříve, než je najde někdo jiný
* Pentest provádí White hat a výstupem tohoto testování je technická zpráva, ve které se uvádí, zda našel nějaké slabiny, nebo doporučení pro opravu
## Typy pentestů
### BlackBox
* Tester nemá žádné interní informace
* Probíhá jako simulace klasického útočníka zvenku
### WhiteBox
* Tester má plný přístup k dokumentaci, kódu a systémům
### GrayBox
* Kombinace white a black boxu
* Tester má informace jako běžný uživatel
## Fáze pentestu
### Plánování a dohoda
* Identifikace rozsahu útoku a jeho cílů
* Stanovení pravidel (co se testuje, kdy, ...)
* Podepsání smlouvy
### Sběr informací
* **Pasivní** - WHOIS, DNS, Google hacking
* **Aktivní** - Skenování portů, fingerprintig systémů
### Skenování
* Mapování sítí a služeb
* Získávání verzí SW, banner grabbing
* Vyhledávání zranitelností
### Získání přístupu
* Zneužití nalezené zranitelností
* Webové útoky - SQL injection, XSS, CRSF, RCE
* Síťové útoky, SMP, FTP, SSH brute-force
* Slabá hesla
### Udržení přístupu
* Instalace backdooru, vytvoření nového uživatele
* Přístup k citlivým datům
### Odstranění stop
* Odstranění všech logů, vytvořených během testu
* Nezanechání žadné škody
### Zpráva a doporučení
* Dokumentace nálezů, závažnost nálezů 
* Návrh nápravných opatření

## Nástroje
### Sběr informací
* WHOIS, nslookup, theHarvester
* Shodan
* Maltego
### Skenování
* Nmap - Sken portů
* Masscan
* Nikto
### Exploity
* Metasploit Framework
* ExpoitDB - Databáze exploitů
* Burp Suite - Testování webových aplikací 
### Hesla
* John the Ripper, Hashcat - crack hesel
* Hydra - Bruteforce útoky na SSH, FTP,...
### WIFI
* Aircrack-ng, Wifite, Reaver - WPA/WPA2

## Co se testuje
### Webové aplikace
* SQL injection
* Cross-site Scripting
* File Inclusion
* Broken Authentication
### Síť
* Neaktualizový SW
* Porty 
* Slabá hesla
* Nešifrovaná komunikace
### Mobilní aplikace
* Špatné šifrování
* Vystavení API klíčů
* Obcházení autorizace
