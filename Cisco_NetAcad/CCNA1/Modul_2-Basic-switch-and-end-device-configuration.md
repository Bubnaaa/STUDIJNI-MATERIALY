# 2. Modul - Basic Switch and End Device Configuratuion

## Operating system
- Program pro správu hardwaru a spouštění softwaru
- Dvě části:
	- Kernel - Komunikace přímo s hardwarem a správa zdroje
	- Shell - Rozhraní mezi uživatelem a Kernelem, Umožňuje zadávat přikazy a ovládat OS
## User interface
### CLI (Příkazová řádka)
- Nutnost znalosti příkazů
- Typické pro síťová zařízení
### GUI (Grafické rozhraní)
- Běžné operační systémy (Win, Linux, MacOS)

## Síťové OS
- Na Cisco zařízeních se používá Cisco IOS
### Připojení
- Přes Konzolový port
- Přes SSH, nebo Telnet

# Režimy příkazového řádku v Cisco IOS
## Primární příkazové režimy
### User EXEC mode (`>`) 
- Omezený přístup
### Privileged EXEC mode (`#`)
- Vyšší oprávnění, Přístup ke konfiguraci
## Konfigurační a podkonfigurační režimy
### Global Configuration Mode (`Switch(config)#`)
- Nastavení celého zařízení 
### Line Configuration Mode (`Switch(config-line#`)
- Konfigurace Console, SSH, AUX
### Interface Configuration Mode (`Switch(config-if)#`)
- Konfigurace síťového rozhraní

### Přepínání režimů
- Přechod z User do Privileged: `enable`
- Přechod z Privileged do User: `disable`
- Do global config: `configure terminal`
- Zpět do privileged EXEC: `end`
- O úroveň výš: `exit`
- Z global config do Line config: `line console 0`
- Z global config do interface config: `interface FastExthernet 0/1`
## Základní struktura IOS příkazů

    [prompt] command [keyword][argument]
   - Command - Např.: show, ping, configure
   - Keyword - Např.: ip, interface
   - Argument - Hodnota zadaná uživatelem (např. IP adresa)

## Základní konfigurace zařízení
### Jméno
- Pomocí `hostname`

    	Switch# configure terminal
		Switch(config)# hostname Sw-1
		Sw-1(config)#

### Heslo
- Pomocí `password <heslo>`

		Sw-1# configure terminal
		Sw-1(config)# line console 0
		Sw-1(config-line)# password cisco
		Sw-1(config-line)# login

### Heslo pro vstup do Privileged EXEC 
		Sw-1(config)# enable secret class

### Heslo pro vzdálený přístup
		Sw-1(config)# line vty 0 15
		Sw-1(config-line)# password cisco
		Sw-1(config-line)# login

### Šifrování hesel
- Bez šifrování jsou hesla vidět v `running-config` 

		Sw(config)# service password-encryption

### Banner MOTD

		Sw(config)# banner motd #Authorized Access Only#

## Konfigurační soubory
### Startup-config
- Uložený konfigurační soubor v NVRAM
- Používá se při spuštění nebo restartu zařízení

		Sw# show startup-config
### Running-config
- Aktuální konfigurace v RAM
- Změna se projeví okamžitě, ale po restartu se ztratí pokud nebyla uložena

		Sw# show running-config
### Uložení konfigurace
		Sw# copy running-config startup-config

## Manuální nastavení IP adresy
- Každé koncové zařízení potřebuje svou IP adresu pro komunikaci v síti 


	    Switch# configure terminal
	    Switch(config)# interface vlan 1
	    Switch(config-if)# ip address 192.168.1.20 255.255.255.0
	    Switch(config-if)# no shutdown
	    Switch(config-if)# exit
	    Switch(config)# ip default-gateway 192.168.1.1
