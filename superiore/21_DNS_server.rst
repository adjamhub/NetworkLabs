==========
DNS Server
==========


.. note::

    Prerequisti: **OS, terminale**
    
    Argomenti trattati: **DNS, URL**
    
    
.. Qui inizia il testo dell'esperienza

In questo capitolo andremo ad installare un server DNS su un dispositivo con OS Linux. Questo dispositivo monta una versione di Linux con package manager **apt**, 
quindi potrebbe essere un RaspberryPi oppure una installazione di Ubuntu Server.

Il server DNS che andiamo ad installare si chiama **BIND** (https://www.isc.org/bind/). Bind è un server DNS open source sviluppato dall’Internet Systems Consortium e
che rappresenta il server DNS in assoluto più utilizzato sulla rete Internet. Credo che molti (se non tutti i) server DNS della root zone siano implementati con Bind
e così molti dei server autoritativi esistenti. Per quanto riguarda il mercato dei resolver invece... il problema si allarga.

Per installare il server DNS BIND sul nostro OS, dopo un aggiornamento generale dei pacchetti installati, ci basterà fare un semplice:


.. code:: bash

    $ sudo apt install bind9


I file di configurazione dello stesso si trovano nella directory `/etc/bind`. Il file principale si chiama `named.conf` che non contiene altro che riferimenti agli altri file che
organizzano in questo modo la configurazione del server a blocchi indipendenti.

Il file contiene già nella sua installazione un elenco degli IP dei server della **DNS root zone**: il file `/usr/share/dns/root.hints`, quindi tecnicamente
è già pronto a partire e funzionare come resolver per qualunque sito: avrà bisogno solo di un pò di tempo (e richieste) per costruire la sua cache e velocizzarsi.

Avviatelo, eventualmente configuratelo come vostro server DNS e testatelo.


.. mancano:
    - la creazione di una zona per cui questo server è autoritativo
    - un test di SOA
    - una prova di DNS poisoning
