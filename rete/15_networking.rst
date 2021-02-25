==========
Networking
==========


.. note::

    Prerequisti: **Linux, MacOS. Terminale**

    Argomenti trattati: **Indirizzamento IP**

    
.. Qui inizia il testo dell'esperienza


In questo capitolo vado a riassumere alcuni concetti in maniera veloce su come
verificare e/o impostare la configurazione di rete in un ambiente UNIX-like (Linux, MacOS) da terminale.


Configurazione di rete
======================

Ricordate che per la configurazione di rete di un dispositivo, ovvero per permettergli
di accedere alla rete Internet, occorre che esso conosca:

* **il suo Indirizzo IP e la sua subnet mask**. Questo gli permette di conoscere la sua
  rete, l'indirizzo della sua rete di appartenenza, il suo indirizzo di broadcast e di 
  riconoscere quali dispositivi appartengono alla sua stessa rete. Un dispositivo con
  queste informazioni può comunicare 1 a 1 con un altro dispositivo della propria rete
  o fare broadcast e dunque utilizzare protocolli come ad esempio ARP.
  
* **il suo gateway**. L'indirizzo del dispositivo della propria rete di appartenenza
  che gli consente di collegarsi all'esterno di essa. Con questa informazione, più le
  precedenti, un dispositivo può connettersi a qualunque dispositivo remoto raggiungibile
  tramite la rete Internet.
  
* **Almeno un IP relativo ad un dispositivo che esponde un servizio DNS**, solitamente
  ne vengono forniti due per motivi di tolleranza agli errori, dato che DNS utilizza il
  protocollo UDP.
  
Queste informazioni possono essere fornite in due modi al dispositivo:

#. tramite **configurazione statica**, ovvero inserendo manualmente le informazioni
   necessarie.

#. tramite **configurazione dinamica**, ovvero ricorrendo all'utilizzo del protocollo DHCP.



Configurazione di rete attuale
==============================


Con le seguenti istruzioni saremo in grado di visualizzare la configurazione di rete attuale di un dispositivo UNIX-like
tramite terminale.

Per visualizzare la configurazione attuale:

.. code-block:: bash

    $ ip a
    
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
        link/ether 54:05:db:XX:XX:XX brd ff:ff:ff:ff:ff:ff
        inet 192.168.1.7/24 brd 192.168.1.255 scope global dynamic noprefixroute eth0
           valid_lft 84568sec preferred_lft 84568sec
        
Nella seguente configurazione vediamo la presenza di 2 interfacce:

#. l'interfaccia chiamata **lo**, ovvero l'interfaccia di loopback, avente indirizzo **127.0.0.1**

#. l'interfaccia chiamata **eth0**, avente indirizzo (inet) **192.168.1.7** e subnet mask **255.255.255.0** (/24)

Ovviamente quella che ci interessa è la seconda. Per visualizzare la tabella di routing e determinare il gateway facciamo:


.. code-block:: bash

    $ ip r
    
    default via 192.168.1.1 dev eth0 proto dhcp metric 100 
    192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.7 metric 100 


Chiaramente (almeno spero) il gateway è l'indirizzo IP **192.168.1.1**. Ultima informazione da desumere sono gli indirizzi dei DNS.
Sono scritti nel file */etc/resolv.conf*:


.. code-block:: bash

    $ cat /etc/resolv.conf
    
    nameserver 1.1.1.1
    nameserver 8.8.8.8


Ecco qua le informazioni necessarie :D


Configurazione di rete statica (temporanea)
===========================================


Con le seguenti istruzioni saremo in grado di impostare una configurazione statica
temporanea, ovvero che sarà resettata dopo il prossimo riavvio.

Facciamo l'ipotesi di voler configurare l'interfaccia di rete chiamata **eth0**, con le seguenti informazioni di rete:


============ ================
IP           192.168.0.10
------------ ---------------- 
SUBNET MASK  255.255.255.0
------------ ---------------- 
GW           192.168.0.1
------------ ---------------- 
DNS          1.1.1.1, 9.9.9.9
============ ================


Vediamo i passaggi commentati uno per uno:


.. code-block:: bash

    # questo è un commento
    questo è un comando
    
    # TUTTI I COMANDI QUI SOTTO VANNO ESEGUITI CON PRIVILEGI AMMINISTRATIVI
    # QUINDI SONO PRECEDUTI DALL'ISTRUZIONE sudo
    
    # attiva l'interfaccia eth0
    sudo ip link set eth0 up
    
    # imposta IP e SUBNET MASK
    sudo ip a add 192.168.0.10/24 dev eth0
    
    # imposta il GW
    sudo ip r add default via 192.168.0.1

   
Al termine di questi comandi abbiamo impostato IP, SUBNET MASK e GATEWAY. 
Se casualmente ti capita di combinare qualcosa tale per cui vuoi resettare 
la configurazione e ricominciare daccapo:


.. code-block:: bash

    # resetta la configurazione
    sudo ip a flush eth0
    
    # spegne l'interfaccia
    sudo ip link set eth0 down
    

Per inserire il DNS basta aprire il file */etc/resolv.conf*, 
cancellare il suo contenuto e scriverci dentro *nameserver 1.1.1.1* e a 
capo *nameserver 9.9.9.9*. 
Salvare e chiudere.


.. code-block:: bash

    sudo nano /etc/resolv.conf
    
    # cancella tutto il contenuto, scrivici solo
    nameserver 1.1.1.1
    nameserver 9.9.9.9
    
    # salva e chiudi


Finito!!!


Configurazione di rete statica (netplan)
========================================


Questa configurazione che vediamo qui funziona solo su **Ubuntu Server**, che utilizza uno
strumento di configurazione chiamato **netplan**.

La configurazione va scritta in un file *yaml* da creare nella cartella */etc/netplan*
eventualmente eliminando ogni ulteriore configurazione.


.. code-block:: bash

    # Andiamo nella cartella /etc/netplan
    cd /etc/netplan
    
    # visualizziamo il suo contenuto
    ls
    
    00_default.yaml
    

Come vedete c'è un solo file attualmente chiamato **00_default.yaml**. Va rinominato
per disattivarlo


.. code-block:: bash

    # rinomino il file precedente
    sudo mv 00_default.yaml 00_default.old
    

Adesso creo il nuovo file *99_config.yaml* con le seguenti istruzioni:


.. code-block:: bash

    sudo nano 99_config.yaml
    
    # adesso scriveteci dentro ESATTAMENTE questo (attenti anche all'indentazione)
    
    network:
        version: 2
        renderer: networkd
        ethernets:
            eth0:
                addresses:
                    − 192.168.0.10/24
                gateway4: 192.168.0.1
                nameservers:
                    addresses:  [ 1.1.1.1 , 9.9.9.9 ]

    # poi salva e chiudi
    

Adesso per applicare le impostazioni:


.. code-block:: bash

    sudo netplan apply



Configurazione di rete dinamica (netplan)
=========================================


Se per qualche motivo il vostro server non necessita un IP statico potete usufruire della comodità
del protocollo DHCP con pochi passi.

Come prima, dovete eliminare ogni file dalla cartella */etc/netplan*, ricrearne uno con la configurazione corretta
e riapplicare le modifiche. Le cose da scrivere nel file 99_dynamic.yaml sono:


.. code-block:: bash

    network:
        version: 2
        renderer: networkd
        ethernets:
            eth0: 
                dhcp4: true

                                
Salvate e applicate ancora con:


.. code-block:: bash

    sudo netplan apply


Bridge
======


I bridge sono periferiche virtuali di livello 2 (il livello inferiore, relativo alla distinzione dei dispositivi tramite indirizzo MAC) che non può
ricevere o trasmettere nulla finché non viene collegato ad una o più periferiche reali.

La sua utilità sta nel fatto che può collegare a livello inferiore 2 periferiche senza intaccare in alcun modo il livello di rete soprastante. 

* Se entrambe le due periferiche sono reali, il bridge serve per la conversione a livello fisico dei pacchetti SENZA un instradamento 
  (che richiederebbe una nuova conversione in digitale).

* Se almeno una delle due periferiche è virtuale (ad esempio con una macchina virtuale) il bridge può essere utilizzato per connettere fisicamente la periferica
  virtuale alla rete su cui è esposta la periferica reale, permettendo alla macchina virtuale di essere esposta sulla rete a cui la periferica fisica appartiene


Per creare un bridge:


.. code-block:: bash
    
    # nell'esempio che segue: 
    # il bridge si chiamerà bridge0
    # la periferica fisica si chiamerà phisdev0
    # la periferica virtuale si chiamerà virtdev0
    
    # creare il bridge e attivarlo
    sudo ip link add name bridge0 type bridge
    sudo ip link set bridge0 up

    # aggiungere le due periferiche al bridge
    sudo ip link set phisdev0 master bridge0
    sudo ip link set virtdev0 master bridge0



TUN/TAP devices
===============

Le interfacce TUN/TAP sono 2 tipologie di interfacce virtuali inventate per permettere operazioni di rete virtuali. A metà tra l'informatica e la magia nera, le 2 interfacce hanno
scopi specializzati:

* Le periferiche **TUN** servono per connettere **a livello di rete** 2 software allo stesso modo in cui una interfaccia di rete REALE connette 2 dispositivi.
  Questa cosa fa pensare ai 2 software (che stanno in realtà nello stesso dispositivo) di trovarsi in 2 dispositivi diversi.
  
* Le periferiche **TAP** servono per connettere **a livello inferiore** 2 software allo stesso modo in cui una interfaccia fisica connette 2 dispositivi. In questo
  modo la periferica realizza un bridge virtuale fra i 2 software, che pensano di trovarsi in 2 dispositivi diversi.
  
La ovvia differenza fra le 2 periferiche virtuali è che una lavora a livello di rete e quindi può servire come punto di connessione ad un altro dispositivo posizionato ovunque
sulla rete Internet (mai sentito parlare di VPN? Si realizzano tramite periferiche TUN), mentre l'altra lavora a livello inferiore, quindi può servire a connettere al livello di rete
un livello fisico non... tanto fisico (mai sentito parlare di macchine virtuali? Hardware... non tanto hard).


.. code-block:: bash

    # per creare una interfaccia TUN, indicando CHI può usarla
    sudo ip tuntap add tun0 mode tun group users
    sudo ip link set tun0 up

    # per creare una interfaccia TAP, indicando CHI può usarla
    sudo ip tuntap add tap0 mode tap group users
    sudo ip link set tap0 up

