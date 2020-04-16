=======
netstat
=======

.. note::

    Prerequisti: **Windows, Linux, Mac: linea di comando**
    
    Argomenti trattati: **Protocolli di trasporto**
      
    
.. Qui inizia il testo dell'esperienza


L'utility di rete **netstat** permette di esaminare le connessioni attive, individuando le porte attive nel proprio dispositivo e quelle disponibili
a ricevere dati in ingresso.

Permette inoltre (cose che a noi interessano meno) di visualizzare statistiche relative a connessioni di rete, tabelle di routing, interfacce di rete, 
masquerading e multicasting.

Vediamo le principali opzioni:

=================== ======================= ==========================================================================
Opzione per Windows Opzione per Linux e Mac Significato
------------------- ----------------------- --------------------------------------------------------------------------
-a                  -a                      Visualizza tutte le connessioni, attive e non
-n                  -n                      Visualizza i dati (IP e porta) in forma numerica, senza risoluzione
-o                  -p                      Visualizza il PID (identificatore) del processo che occupa quella porta
-p TCP              -t                      Visualizza tutte (e solo) le connessioni TCP
-p UDP              -u                      Visualizza tutte (e solo) le connessioni UDP
=================== ======================= ==========================================================================

Provate a combinare le varie opzioni, seguendo la sintassi del sistema operativo che state utilizzando, osservando i risultati.
