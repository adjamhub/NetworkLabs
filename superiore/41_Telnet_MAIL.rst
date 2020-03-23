=============
Telnet e Mail
=============

.. note::

    Prerequisti: **OS, terminale**
    
    Argomenti trattati: **Telnet, SMTP, POP, IMAP**
      
    
.. Qui inizia il testo dell'esperienza


Introduzione
============

Telnet è un piccolo client da terminale, disponibile su ogni sistema operativo, che serve per simulare connessioni in chiaro a qualsiasi socket desideriamo.
La sua utilità sta nel fatto che permette di *dialogare* con qualunque protocollo del livello superiore che utilizza
testo semplice per le sua sintassi.

A pensarci bene, tutti i protocolli del livello superiore che abbiamo studiato (o che studieremo) utilizzano dati codificati
in ASCII, quindi... telnet può essere un semplice strumento per provare ad analizzarli!

La sua sintassi è semplicissima:

.. code:: bash

    $ telnet HOST PORT
    
Da dopo l'avvenuta connessione bisogna scrivere.. nella lingua del servizio con cui vogliamo dialogare, ovvero bisogna usare le specifiche del protocollo!


Telnet e SMTP
=============

Per estrema semplicità simulerò semplicemente una connessione ad un MTA generico, di cui elenco le caratteristiche:

- host: **scuola.lan**

- porta: **25**

- user1: **pippo**

- pass1: **attentialcane**

- user2: **ciccio**

- pass2: **pescegatto**

Tramite telnet l'utente *pippo* proverà ad inviare una mail all'utente *ciccio*. 


.. code:: bash

    $ telnet scuola.lan 25
    
    ... risposta ...

    HELO pippo
    
    ... risposta ...

    MAIL FROM: pippo@scuola.lan
    
    ... risposta ...

    RCPT TO: ciccio@scuola.lan
    
    ... risposta ...

    DATA

    ... risposta ...

    Subject: Titolo
    Una mail con testo qualsiasi che termina quando
    andate a capo, scrivete un punto e riandate a capo.
    .
    
    ... risposta ...

    QUIT
    

Se avete scritto tutto bene (lo capite osservando le risposte) avete inviato una mail scrivendo *a mano* le istruzioni SMTP per l'MTA!!!
Avete notato che non avete mai inserito la password???


TELNET e IMAP
=============

Adesso proviamo a consultare la mail dell'utente *ciccio* per trovare la mail che ha ricevuto. Facciamo prima con IMAP così il messaggio rimane
sul server e proviamo successivamente provare con POP ;)


.. code:: bash

    $ telnet scuola.lan 143

    ... risposta ...
    
    a1 LOGIN ciccio pescegatto
    
    ... risposta ad a1 ...

    a2 LIST "" "*"

    ... risposta ad a2 ...
    
    a3 EXAMINE INBOX

    ... risposta ad a3 ...
    
    a4 FETCH 1 BODY[]

    ... risposta ad a4 ...

    a5 LOGOUT


Ecco qua! Avanti...



TELNET e POP3
=============

Adesso proviamo a consultare la mail dell'utente *ciccio* con POP, cancellando il messaggio alla fine della consultazione.


.. code:: bash

    $ telnet scuola.lan 110

    ... risposta ...

    USER ciccio
    
    ... risposta ...

    PASS pescegatto

    ... risposta ...

    LIST

    ... risposta ...

    RETR 1

    ... risposta ...

    DELE 1

    ... risposta ...

    QUIT

    
Come avete intuito leggendo i comandi, vi siete connessi al server POP con le credenziali di *ciccio*, avete elencato i suoi messaggi,
avete letto (e poi cancellato) il messaggio numero 1. 





