===================
Sito web a casa tua
===================

.. note::

    Prerequisti: **PC oppure Raspberry, terminale. esperienza 'port forwarding'**
    
    Argomenti trattati: **HTTP, URL, DNS, livello di trasporto**
    
    Linguaggi per il web introdotti: **HTML, CSS, PHP**

    
    
.. Qui inizia il testo dell'esperienza


Sì, hai capito bene... proviamo a `hostare` un sito web a casa di ognuno di voi. Ovviamente sarà un compito per casa e avrà alcune condizioni...

L'esperienza si snoda in 3 fasi distinte:

#. installare un server web sul proprio dispositivo (PC/Raspberry)

#. configurare il port forwarding fra il vostro dispositivo e il router di casa

#. aggiungere un DNS dinamico al vostro router in modo da rendere semplicemente raggiungibile il sito


Fase 1: web server
==================

Per quanto riguarda la prima fare, se avete un Raspberry (oppure un computer con Linux) potete consultare la guida sul server web qui sopra.

Se avete solo un PC con Windows o Mac, potete installare un server web con **XAMPP** (https://www.apachefriends.org/index.html).

Nella pagina linkata ci dovrebbe essere anche un video di 90 secondi che spiega come si installa. Potete tranquillamente deselezionare tutte le opzioni possibili
(apache e php vengono installati per forza). Tutto qui!

Create una pagina web semplice e divertente e salvatela come *index.html* nella cartella *htdocs* dentro la cartella *xampp* (magari rinominando quella presente inizialmente).


Se davvero funziona...
----------------------

Controllate l'IP del dispositivo in cui avete installato il server web e provate a collegarvi con il vostro telefono (collegato al wifi di casa)
al sito **http://IP_del_dispositivo**.

E se davvero funziona... potete già cominciare ad essere soddisfatti di voi!



Fase 2: port forwarding
=======================

Per quanto riguarda il port forwarding dovete seguire la guida a proposito nella sezione del livello di trasporto ed esporre la porta 80 del dispositivo in cui
avete installato apache all'esterno.


Se davvero funziona...
----------------------

Controllate con un sito web tipo https://whatismyipaddress.com/ il vostro indirizzo pubblico e provate con il vostro telefono (non collegato al wifi) a collegarvi
al sito **http://vostro_IP_pubblico**. 

E se davvero funziona... fate sapere al prof quanto siete tosti!!!


Fase 3: Dynamic DNS
===================

Ultima fase... configurazione di un DNS dinamico per rendere il vostro sito raggiungibile con semplicità da chiunque!

Al di là di questa fase c'è lo zen delle conoscenze di rete, quindi non starò a spiegarvi molto se non a darvi due imbeccate:

#. nei router solitamente è già presente il supporto per il DNS dinamico. Provate a controllare nella sua interfaccia (lo avete già fatto per il port forwarding) e utilizzate uno dei servizi indicati lì.

#. i servizi di DNS dinamico forniscono gratuitamente, per un periodo limitato, host del terzo livello per alcuni servizi. Alcuni fra i più famosi siti per il DNS dinamico sono:

    - https://dyndns.it/
    
    - https://www.noip.com/
    
    - https://cloudns.net/

Fatelo! Se volete un posto in paradiso... fatelo!


Se davvero funziona...
----------------------

Collegatevi tramite il vostro telefono (non collegato al wifi) al sito **http://vostro.host.dinamico**.

E se davvero funziona... lasciate il dispositivo acceso per pavoneggiarvi a lezione con il prof estasiato e i vostri compagni ammirati.
