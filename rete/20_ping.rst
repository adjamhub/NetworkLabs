====
ping
====

.. note::

    Prerequisti: **Windows, command prompt**
    
    Argomenti trattati: **Indirizzamento IP**
      
    
.. Qui inizia il testo dell'esperienza


ping è un software di diagnostica di rete, implementato in tutti i sistemi operativi, che misura il tempo (in millisecondi) impiegato 
da uno o più pacchetti ICMP a raggiungere un altro dispositivo di rete e tornare indietro.

Tecnicamente ping invia un pacchetto ICMP di echo request e rimane in attesa di un pacchetto ICMP di echo response in risposta. Solitamente infatti la parte di OS dedicata alla gestione delle reti (stack di rete) è impostata per rispondere automaticamente con un pacchetto echo response alla ricezione di un pacchetto di echo request.

Il comando ping su Windows è impostato per inviare 4 pacchetti ICMP, attendere 4 risposte e poi calcolare le statistiche di ricezione e velocità.
La sintassi del comando ping è la seguente:


.. code-block:: bash

    $ ping [opzioni] host


Evitiamo di addentrarci nel discorso delle opzioni del comando ping e vediamo semplicemente il funzionamento e l'utilità dello stesso.


.. image:: images/ping.png


Come si vede, basta scegliere un target host (tramite IP o hostname) e lanciare il comando. Al termine dell'esecuzione bisogna osservare i pacchetti ritornati e
le statistiche di viaggio degli stessi per valutare la salute e le performance della rete stessa.


.. warning::

    Il comando ping su Windows è impostato automaticamente ad interrompersi dopo l'invio di 4 pacchetti.
    
    In ambienti Linux o Mac invece, il comando ping continua indefinitamente ad inviare pacchetti finché non
    lo si interrompe con un comando **CTRL + C** (mela + C su Mac). Quando viene interrotto l'invio vengono 
    generate le statistiche.
    

Il comando ping insieme ai comandi ipconfig e traceroute sono un ottimo strumento di diagnostica e sono semplicissimi da utilizzare. 
L'importante è ragionare sui risultati che si ottengono e formulare deduzioni appropriate. 

Chiedi al prof di fare alcuni esempi a proposito.

