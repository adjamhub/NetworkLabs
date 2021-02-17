======================
Collegamento da remoto
======================


.. note::

    Prerequisti: **OS, prompt, terminale**
    
    Argomenti trattati: **RDP, VNC, SSH**

    
    
.. Qui inizia il testo dell'esperienza



Un sistema operativo, virtuale o fisico, installato nel dispositivo davanti a noi o a milioni di chilometri di distanza può essere comandato semplicemente
con un collegamento **da remoto!**

I metodi più utilizzati per la connessione remota ad un dispositivo dipendono dal sistema operativo dello stesso, oltre che da quello del computer vicino a noi,
grazie al quale ci vogliamo connettere al computer remoto.
In questo elenco troviamo i protocolli più utilizzati per la connessione da remote con indicati i software server e client per determinati OS.
Se volete conoscere atri software dedicati a combinazioni di sistemi operativi diversi (ad esempio connettersi ad un PC con Windows 10 da un Mac), 
documentatevi su Internet sui client per la corrispondente tecnologia.


========== ========= =============== =================
Protocollo Tipologia Server (su RPI) Client (su Win10)
========== ========= =============== =================
RDP        Grafica   Xrdp            Remote Desktop
VNC        Grafica   vnc             VNC Viewer
SSH        Testuale  sshd            Putty
========== ========= =============== =================

.. warning:: 
    Qualsiasi metodo sceglierai, ricordati che avrai bisogno di conoscere il **nome** e/o l'**indirizzo IP** del dispositivo remoto!
    
    Cerca di capire **prima** come sia possibile ottenere (e magari modificare) queste informazioni!


RDP
===

**Remote Desktop Protocol** è un protocollo di rete proprietario sviluppato da Microsoft, che permette la connessione remota da un computer a un altro in maniera grafica. Il protocollo di default utilizza la porta TCP e UDP 3389.

I client RDP esistono per la maggior parte delle versioni di Microsoft Windows, Linux, Unix, macOS, Android, iOS. I server RDP ufficiali esistono per i sistemi operativi Windows nonostante ne esistano anche per i sistemi Unix-Like. 

.. tip:: 
    **Su Ubuntu**
    
    Installa il servizio xrdp:
    
    .. code-block:: bash

        $ sudo apt install xrdp
        
    Fatto questo, riavvia.

.. tip:: 
    **Su Windows**
    
    Non devi fare nulla! Ti basta cercare il software *Connessione a Desktop Remoto*


VNC
===

**Virtual Network Computing** è un protocollo per applicazioni software di controllo remoto, utilizzato per amministrare il proprio computer a distanza.
Può essere utilizzato anche per controllare in remoto server che non posseggono né monitor né tastiera.

Il protocollo di comunicazione usato a livello di trasporto è il TCP sulla porta di default 5900, oppure tramite interfaccia HTTP sulla porta 5800/tcp.

.. tip:: 
    **Su Ubuntu**
    
    Il server VNC si chiama vnc. Installa
        
    Fatto questo, riavvia.
    
.. tip:: 
    **Su Windows**
    
    Un client VNC gratuito è il VNC Viewer di RealVNC: https://www.realvnc.com/en/connect/download/viewer/windows/
    
    Scaricalo, installalo su Windows e provalo.


SSH
===

**Secure Shell** è un protocollo che permette di stabilire una sessione remota cifrata tramite interfaccia a riga di comando con un altro host di una rete informatica. 
È il protocollo che ha sostituito l'analogo, ma insicuro, Telnet, perché basato su una comunicazione **non** cifrata.

A livello server utilizza la porta 22, sia tramite TCP che UDP.


.. tip:: 
    **Su Ubuntu**
    
    Il server SSH è disponibile di default, ma va abilitato (come???)
    
    Fatto questo, riavvia.
    
.. tip:: 
    **Su Windows**
    
    Ti basta scaricare Putty e usarlo senza neanche installarlo!
    
    Il sito ufficiale è: https://www.putty.org/

