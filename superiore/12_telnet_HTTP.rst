=============
Telnet e HTTP
=============

.. note::

    Prerequisti: **OS, terminale**
    
    Argomenti trattati: **Telnet, HTTP**
      
    
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



TELNET e HTTP
=============

Praticamente con telnet ci colleghiamo ad un server HTTP e poi possiamo provare a scrivere a mano una richiesta HTTP. Nell'esempio proviamo a connetterci 
al generico sito **www.esempio.com** e a chiedere la homepage con una richiesta GET.

.. code:: bash

    $ telnet www.esempio.com 80

    ... risposta ...
    
    GET / HTTP/1.1
    Host: www.esempio.com

    ... risposta ...
    HTTP/1.1 200 OK
    Date: Wed, 21 Jan 2004 22:13:05 GMT
    Server: Apache/1.3.12-Turbo
    Content-Type: text/html
    <html>
    <head>
    <title>Esempio</title>
    </head>
    <body>
    <h1>Esempio</h1>
    Hai capito?
    </body>
    <html>

Tutto qui... semplice, ma efficace! Secondo me, anche molto affascinante.

