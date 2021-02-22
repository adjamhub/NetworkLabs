=============
Ubuntu Server
=============


.. note::

    Prerequisti: **VirtualBox.**

    
.. Qui inizia il testo dell'esperienza


In questo capitolo andremo ad installare una copia di Ubuntu (una sua configurazione chiamata **Ubuntu Server**) su VirtualBox. Chiaramente dovete aver già
provveduto ad installare VirtualBox sulla vostra macchina. Poi si può procedere all'installazione di Ubuntu Server.

Ubuntu Server non è altro che una versione di Ubuntu (https://www.ubuntu.com) in cui sono state tolte le maggiori funzionalità grafiche e sono proposte durante l'installazione
stessa del sistema operativo opzioni riguardanti l'installazione di software comuni per le reti quali un server HTTP, un server DNS, un server DHCP, un server SSH, etc...


Installazione
=============

Per l'installazione di Ubuntu su VirtualBox dovete creare una macchina virtuale con VirtualBox, caricare la ISO di Ubuntu come se fosse un CD e poi avviare l'installazione.

Se avete bisogno di aiuto potete seguire la guida ufficiale di Ubuntu: https://ubuntu.com/tutorials/install-ubuntu-server#1-overview

Buon lavoro!

Al termine dell'installazione potete approfondire i seguenti prossimi argomenti.



Il terminale Linux
==================

Adesso vogliamo dedicare un pò di tempo a prendere confidenza con il terminale Linux. Utilizzare l'interfaccia testuale può essere molto vantaggioso in diversi
casi:

* Tutti i sistemi Linux hanno la stessa interfaccia testuale, ma le interfacce grafiche sono potenzialmente tutte diverse

* La connessione remota ad un dispositivo in modalità testuale è veloce, sicura e facile da stabilire

* L'interfaccia testuale è molto potente. Pensate all'interfaccia grafica del vostro Sistema Operativo preferito:
    
    * Come si fa a controllare l'IP della macchina?
    
    * Come si fa a cercare un file all'interno di tutto il computer?
    
    * Come si fa a disintallare un programma? Arrestare un servizio? 
    
Tutte queste operazioni costano un unico comando, una riga di codice con l'interfaccia testuale. E richiedono un secondo o poco più per l'esecuzione.


Adesso che ho attirato la vostra attenzione sull'utilizzo della linea di testo, vediamo alcuni semplici comandi organizzati per utilizzo:


Muoversi fra i file
    =======  ============================================
    Comando  Descrizione
    =======  ============================================
    ls       Elenca i file nella directory corrente (list)
    cd       Cambia Directory.
    pwd      Directory corrente
    =======  ============================================

    
Manipolazione del testo    
    =======  ============================================
    Comando  Descrizione
    =======  ============================================
    cat      Concatena i file e ne manda il contenuto nello standard output
    less     Visualizza il contenuto di un file
    nano     Editor testuale
    =======  ============================================


Gestione di file e directory
    =======  ============================================
    Comando  Descrizione
    =======  ============================================
    mkdir    Crea una directory, una cartella
    touch    Crea un file 
    cp       Copia un file o una directory
    mv       Sposta un file o una directory
    rm       Rimuove un file o una directory
    =======  ============================================

    
Sistema
    ========  ============================================
    Comando   Descrizione
    ========  ============================================
    shutdown  Inizia la procedura di spegnimento
    reboot    Riavvia il sistema
    ========  ============================================


Utilities
    =======  ============================================
    Comando  Descrizione
    =======  ============================================
    history  Elenca la cronologia dei comandi digitati
    man      Apre il manuale richiesto
    =======  ============================================

    
.. note::
    Il comando **sudo** permette di eseguire qualsiasi comando con privilegi amministrativi.
    
    Basta precedere *sudo* a qualsiasi comando per fare come se fosse l'amministratore del sistema
    ad eseguirlo.
    
    .. image:: images/sudo.png
        :align: center
        :alt: sudo examples


    
Gestione software
=================

L' **Advanced Packaging Tool** (conosciuto con l'acronimo APT) è il gestore standard di pacchetti software della distribuzione Debian e di tutte le sue derivate. 
In particolare vale la pena di ricordare Ubuntu e Raspberry come derivate di punta.

Questo sistema di gestione dei pacchetti è in grado di cercare, scaricare, installare qualsiasi software disponibile nei repository indicati nei file 
di configurazione per renderli disponibile all'istante!

.. warning::
    Poiché il comando APT si occupa di operazioni amministrative, deve essere sempre preceduto dal comando sudo.

Vediamo via via le opzioni di APT più importanti:

.. code-block:: bash

    $ sudo apt update
    
Aggiorna l'elenco del software presente nel repository. In questo modo APT saprà qual è l'ultima versione del software disponibile online.


.. code-block:: bash

    $ sudo apt upgrade

Sincronizza il software di sistema con quello presente nel repository. Praticamente permette di aggiornare tutto il software all'ultima versione disponibile.


.. code-block:: bash

    $ sudo apt search package

Cerca il termine "package" fra i pacchetti software disponibili nel repository. Funziona anche senza sudo.


.. code-block:: bash

    $ sudo apt install package

Scarica "package" e lo installa nel sistema, rendendolo disponibile all'utente.


.. code-block:: bash

    $ sudo apt remove package

Rimuove "package" dal sistema.
