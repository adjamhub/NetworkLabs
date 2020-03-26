====
nmap
====

.. note::

    Prerequisti: **Windows, Linux, Mac**
    
    Argomenti trattati: **Protocolli di trasporto**
      
    
.. Qui inizia il testo dell'esperienza


Nmap è un software libero distribuito con licenza GNU GPL da Insecure.org (https://insecure.org) creato per effettuare port scanning, 
cioè mirato all'individuazione di porte aperte su un computer bersaglio o anche su range di indirizzi IP, in modo da determinare quali servizi di rete siano disponibili. 

Vediamo la sintassi di base:


.. code:: bash

    $ nmap OPTIONS TARGET


Il **TARGET** è il dispositivo o l'elenco di dispositivi che nmap deve scannerizzare per capire il tipo di dispositivo che ci troviamo davanti 
(produttore, sistema operativo, servizi attivi) e può essere uno tra questi:

- ``HOST``: ad esempio *ciccio*, oppure *192.168.1.1*

- ``RANGE``: ad esempio *192.168.1.1-20*

- ``SUBNET``: ad esempio *192.168.1.0/24*

Ricorda comunque che la scansione che nnap esegue richiede del tempo quindi occhio ad impostare RANGE o SUBNET troppo ampi...


Le **OPTIONS** disponibili sono tranquillamente un migliaio... noi qui ovviamente noi vediamo le più semplici e interessanti:

.. tip:: 

    nmap è un software molto *veloce* considerato quello che fa e come lo fa.
    
    Il problema è che impiega comunque un buon minuto per una scansione, quindi agli occhi
    delle persone normali risulta *lentissimo*.
    
    Fra le opzioni ne abbiamo anche una per la velocità: **-T4**. Spargetela un pò dove capita per velocizzare
    le operazioni di scansione!


L'opzione più veloce di scansione controlla solo le 100 porte più comuni:

.. code:: bash

    $ nmap -F TARGET

    
La scansione di default senza privilegi amministrativi viene fatta con il 3-way handshake (TCP scan):

.. code:: bash

    $ nmap -sT HOST


Se si hanno privilegi amministrativi è meglio procedere ad un SYN scan (più discreto e più veloce)

.. code:: bash

    $ sudo nmap -sS HOST


.. warning:: 
    
    **TCP scan vs SYN scan**
    
    Mentre un 3way handshake prevede l'invio e la ricezione di 3 pacchetti con l'attivazione di una connessione
    fra i 2 host e permette dunque al sistema target di *accorgersi* del dispositivo che lo scansiona, un SYN scan
    invia al TARGET solo il primo pacchetto dell'handshake e determina l'apertura di un servizio con la ricezione del
    pacchetto SYN+ACK, ma **non** risponde con un ACK ad esso, non aprendo la connessione sul target!


Le due precedenti scansioni ci elencano semplicemente le porte che rispondono o no al 3 way handshake.
Per determinare i servizi realmente attivi dietro alle porte attive:

.. code:: bash

    $ nmap -sV TARGET

    
Per cercare di capire il sistema operativo del dispositivo target (richiede privilegi amministrativi):

.. code:: bash

    $ sudo nmap -O TARGET


Per una scansione *generica* di quale potrebbe essere il sistema operativo e i servizi attivi:

.. code:: bash

    $ nmap -A HOST


Se si vuole capire quali sono gli host online in una rete:

.. code:: bash

    $ nmap -sn SUBNET

    
Porte scansionate
=================

Quando nmap scansiona le porte logiche di un dispositivo TARGET può ritornare risultati di 6 tipi:

===================== ===========================================================================
Classificazione Porta Descrizione
--------------------- ---------------------------------------------------------------------------
open                  Una porta che accetta connessioni
--------------------- ---------------------------------------------------------------------------
closed                Accessibile ma senza una applicazione in ascolto su di essa.
                      Permette di capire che un sistema è attivo e senza firewall.
--------------------- ---------------------------------------------------------------------------
filtered              Non si può determinare con esattezza se la porta sia aperta o no.
                      Le porte protette dai firewall sono così.
--------------------- ---------------------------------------------------------------------------
unfiltered            Una porta non protetta da firewall, ma che non si capisce se sia aperta
                      o meno. Un amministratore acuto si nasconde di solito dietro ad essa...
--------------------- ---------------------------------------------------------------------------
open|filtered         nmap è indeciso fra i 2 stati, ma è sicuro sia uno dei due.
--------------------- ---------------------------------------------------------------------------
closed|filtered       nmap è indeciso fra i 2 stati, ma è sicuro sia uno dei due.
===================== ===========================================================================
