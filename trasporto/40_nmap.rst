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
    
    Fra le opzioni ne abbiamo anche una per la velocità, con 5 possibilità: 
    **-T0 (più lento ed accurato), -T1, -T2, -T3, -T4, -T5 (più veloce e potenzialmente impreciso)**. 
    
    Sta a voi decidere se e quale usare se l'attesa diventa insopportabile :)
    


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
===================== ===========================================================================
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




Nmap Scripting Engine (NSE)
===========================

.. warning::

    Da un grande potere deriva una grande responsabilità
    
    *(zio Ben)*

La caratteristica migliore di nmap è la possibilità di aumentare a dismisura le sue capacità di scanning grazie al meccanismo degli script e al suo NSE ovvero
il software in grado di eseguirli.

Sono presenti centinaia di script per le scansioni più disparate, organizzati nelle seguenti categorie:


=============== ===========================================================================
Categoria       Descrizione
=============== ===========================================================================
auth 	        Script per l'autenticazione e i privilegi utente.
broadcast 	    Network discovery basato su broadcast.
brute 	        Attacchi di tipo brute-force per indovinare le credenziali di accesso.
default         Gli script più popolari e considerati più utili.
discovery 	    Network, Service and Host discovery
dos             Attacchi di tipo \\"Denial of service\\"
exploit 	    Service exploitation on different CVEs
external        Scripts che si appoggiano a servizi o dati esterni per funzionare
fuzzer 	        Attacchi di tipo *fuzzing* ad app, servizi, reti.
intrusive 	    Attacchi aggressivi che potrebbero danneggiare il funzionamento della rete.
malware 	    Malware detections and exploration scripts
safe 	        Safe and non-intrusive/noisy scripts
version 	    OS, service and software detection scripts
vuln 	        Vulnerability detection and exploitation scripts
=============== ===========================================================================


Viste le categorie complete, sappiate che un elenco completo degli script disponibili con una descrizione esplicativa accanto si trova sul sito https://nmap.org/nsedoc/.

Per quanto riguarda il nostro corso, diciamo che prima di poter utilizzare gli script è bene assicurarsi che essi siano presenti, aggiornati all'ultima versione
disponibile e catalogati nel database del sistema. Si ottiene questo risultato eseguendo il comando:

.. code:: bash

    $ sudo nmap --script-updatedb
    
Fatto questo, la sintassi per eseguire gli script è molto semplice e si basa sull'opzione *--script*: ho fatto alcuni esempi per capire il funzionamento.

.. code:: bash

    // SINTASSI GENERALE
    $ sudo nmap --script=QUALCOSINA TARGET
    
    // Per eseguire tutti gli script di default verso un TARGET 
    sudo nmap --script=default TARGET
    
    // Per eseguire gli script dei gruppi broadcast e discovery verso un TARGET
    sudo nmap --script=broadcast,discovery TARGET
    
    // come sopra, esattamente equivalente
    sudo nmap --script="broadcast or discovery" TARGET
    
    // Per eseguire tutti gli script relativi ad HTTP verso un target
    sudo nmap --script=http* TARGET

    // Per eseguire lo script chiamato dhcp-discover verso un target
    sudo nmap --script=dhcp-discover TARGET

    // Per eseguire solo gli script relativi ad HTTP del gruppo discovery verso un target
    sudo nmap --script="http* and discovery" TARGET



Esempi ed Esercizi
==================


Nel primo esempio proveremo ad interrogare il server DHCP per ottenere le informazioni di rete,
fingendo di essere un client DHCP (con un MAC inventato) e visualizzando le informazioni ottenute
senza realmente applicarle.

.. code:: bash

    // l'opzione -sU indirizza la scansione sul protocollo UDP
    // l'opzione -p 67 individua la porta del server DHCP: velocizza la scansione
    // lo script si chiama dhcp-discover
    $ sudo nmap -sU -p 67 --script dhcp-discover IP_SERVER_DHCP


Nel secondo esempio proviamo ad elencare le cartelle condivise da un generico PC con Windows, per
ottenere informazioni su cartelle condivise eventualmente accessibili.

.. code:: bash

    // opzione (-sU) per scansione UDP, opzione (-sS) per scansione TCP SYN
    // Le porte elencate (137/udp e 139/tcp) servono per velocizzare le operazioni
    // lo script si chiama smb-enum-shares
    $ sudo nmap -sU -sS -p U:137,T:139 --script smb-enum-shares IP_SERVER_SMB


Nel terzo esempio proviamo ad ottenere informazioni dettagliate sul PC Windows che ci interessa
studiare.

.. code:: bash

    // opzione (-sU) per scansione UDP, opzione (-sS) per scansione TCP SYN
    // Le porte elencate (137/udp e 139/tcp) servono per velocizzare le operazioni
    // lo script si chiama smb-system-info
    $ sudo nmap -sU -sS -p U:137,T:139 --script smb-system-info IP_SERVER_SMB


Nel quarto esempio faremo fare a nmap una scansione tipo traceroute di tutti gli hop attraversati 
con la localizzazione geografica delle posizioni di ognuna.

.. code:: bash

    $ sudo nmap --traceroute --script traceroute-geolocation TARGET

    
Nel quinto esempio simuleremo un attacco (di 10 minuti) ad un server DNS allo scopo di testare
la qualità della rete e del servizio DNS di quest'ultima. Attenzione...

.. code:: bash

    $ sudo nmap -sU --script dns-fuzz TARGET


Nel sesto e ultimo esempio utilizzeremo uno script di tipo brute per tentare di indovinare nome
utente e password di un utente collegato ad un Mac. Anche questo script ha ovviamente l'unico scopo
di scoraggiare l'utilizzo di nomi utente e password semplici da indovinare.

.. code:: bash

    $ sudo nmap -p 548 --script afp-brute IP_COMPUTER_MAC


