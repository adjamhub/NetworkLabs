===========
DHCP Server
===========

.. note::

    Prerequisti: **Linux: terminale**
    
    Argomenti trattati: **DHCP, DNS, Indirizzamento IP**
      
    
.. Qui inizia il testo dell'esperienza



In questo capitolo andremo ad installare un server DHCP su un dispositivo con OS Linux.
Questo dispositivo monta una versione di Linux con package manager **apt**, quindi potrebbe
essere un RaspberryPi oppure una installazione di Ubuntu Server.

Se avete studiato il protocollo DHCP, sapete che per far funzionare un server DHCP c'è bisogno di un dispositivo
con un indirizzo statico. Il capitolo sul **Networking** spiega come ottenere questo risultato.

Il server DHCP che andiamo ad installare si chiama **KEA** (https://www.isc.org/kea/).
KEA è un server DHCP open source sviluppato dall'Internet Systems Consortium come (futuro)
sostituto dello storico *ISC DHCP SERVER*. Se volete saperne di più... 
leggete dal sito che ho linkato o guardate Wikipedia ;)

Per installare il server DHCP KEA, relativo al protocollo IPv4 sul nostro OS, 
dopo un aggiornamento generale dei pacchetti installati, ci basterà fare un semplice:


.. code:: bash

    $ sudo apt install kea-dhcp4-server
    

Il file di configurazione dello stesso si trova nella directory */etc/kea*.
Noi dobbiamo modificare il file *kea-dhcp4.conf*. Poiché in esso trovate una marea di commenti e spiegazioni
a tutti i parametri possibili e immaginabili, ho provato a scriverne una versione *light*, mettendo in evidenza
SOLO i parametri importanti o indispensabili

.. code::

    // Va modificato in questi 3 punti (leggilo TUTTO per trovarli):
    // - cambia il nome della tua interfaccia di rete in cui vuoi attivare il server DHCP
    // - cambia lo SCOPE degli indirizzi che vuoi servire tramite DHCP
    // - cambia le impostazioni di rete, come GW e DNS da inviare ai client
    //
    // Salva il file modificato su /etc/kea/kea-dhcp4.conf (richiede privilegi amministrativi per farlo)
    // In bocca al lupo... e buona lettura!
    
    {
    
    "Dhcp4": {
        "interfaces-config": {
            "interfaces": [ "eth0" ]
            
            // USEFUL FOR RELAY
            // "dhcp-socket-type": "udp"
        },
    
        // NON TOCCARE ;)
        "control-socket": {
            "socket-type": "unix",
            "socket-name": "/tmp/kea4-ctrl-socket"
        },
    
        // KEA può utilizzare diversi database per mantenere i propri lease
        // - "memfile" : un semplice file CSV salvato da qualche parte
        // - "mysql", "postgres", "cassandra": database esterni (complicato)
        // Per saperne di più, cerca su internet "KEA LEASE STORAGE"
        "lease-database": {
            "type": "memfile",
            "lfc-interval": 3600
        },
    
        
        // PARAMETRI AVANZATI PER IL LEASE
        // meglio non toccare anche qui...
        "expired-leases-processing": {
            "reclaim-timer-wait-time": 10,
            "flush-reclaimed-timer-wait-time": 25,
            "hold-reclaimed-time": 3600,
            "max-reclaim-leases": 100,
            "max-reclaim-time": 250,
            "unwarned-reclaim-cycles": 5
        },
    
    
        // LEASE TIMER(s) 
        "renew-timer": 900,
        "rebind-timer": 1800,
        "valid-lifetime": 3600,
    
    
        // PARAMETRI ADDIZIONALI
        "option-data": [
        
            // DNS
            {
                "name": "domain-name-servers",
                "data": "192.0.2.1, 192.0.2.2"
            },
    
    
            // NOME DI DOMINIO DELLA RETE
            // ("completa" il nome di un pc, come un "cognome". 
            // Il PC chiamato PC1, nella rete sarà conosciuto come PC1.adjam.org)
            {
                "name": "domain-name",
                "data": "adjam.org"
            },
    
    
            // DOMINIO DI RICERCA
            // se questo parametro vale "pippo.com" e tu cerchi tramite DNS un nome
            // semplice, tipo "ciccio", prova a risolvere sia "ciccio" che "ciccio.pippo.com"
            {
                "name": "domain-search",
                "data": "mydomain.example.com, example.com"
            },
    
    
            // Giuro... non ho mai capito. Lasciamoli stare...
            {
                "name": "boot-file-name",
                "data": "EST5EDT4\\,M3.2.0/02:00\\,M11.1.0/02:00"
            },
    
            {
                "name": "default-ip-ttl",
                "data": "0xf0"
            }
    
        ],
    
    
        // LA SOTTORETE CHE CONTIENE LO SCOPE 
        // (per ogni sottorete ci può essere un solo scope)
        "subnet4": [
            {
                // LA SUBNET INTERA
                "subnet": "192.0.2.0/24",
    
    
                // LO "SCOPE" degli indirizzi assegnabili tramite DHCP per la subnet precedente
                "pools": [ { "pool": "192.0.2.1 - 192.0.2.200" } ],
    
    
                // IL GATEWAY ("router" nella terminologia DHCP)
                "option-data": [
                    {
                        "name": "routers",
                        "data": "192.0.2.1"
                    }
                ],
    
    
                // PRENOTAZIONI
                // indirizzi FUORI dallo SCOPE assegnati a precisi client per motivi...
                // (se non volete usare le prenotazioni, potete cancellare il segmento fino al segno)
                "reservations": [
    
    
                    // PRENOTAZIONE semplice CON MAC/IP
                    {
                        "hw-address": "1a:1b:1c:1d:1e:1f",
                        "ip-address": "192.0.2.201"
                    },
    
                    // PRENOTAZIONE con parametri alterati. 
                    // Solo questo client avrà una configurazione dedicata
                    {
                        "hw-address": "1a:1b:1c:1d:1e:12",
                        "ip-address": "192.0.2.203",
                        "option-data": [ {
                            "name": "domain-name-servers",
                            "data": "10.1.1.202, 10.1.1.203"
                        } ]
                    },
    
                ]
                // FINE PRENOTAZIONI
            }
        ],
    
    
    // Logging configuration.
    // Direi che va IGNORATA e LASCIATA così com'è...
        "loggers": [
        {
            "name": "kea-dhcp4",
            "output_options": [
                {
                    // IL FILE DOVE POTRETE SFROGIARE I LEASE...
                    "output": "/var/log/kea-dhcp4.log"
                }
            ],
            
            // Può valere: FATAL, ERROR, WARN, INFO, DEBUG
            // Ogni valore comprende TUTTI i precedenti. Lasciatelo a INFO
            // E bravi per essere arrivati a leggere fino a qui!
            "severity": "INFO",
    
            // Un numero da 0 (poche info) a 99 (un botto di info)
            "debuglevel": 0
        }
      ]
    }
    }
    

Come vedete, viene lungo uguale... però potete scaricare una copia `qui </_static/files/kea-dhcp4.conf>`_ .


Fatto quanto richiesto e salvato il file, attiviamo (o riattiviamo) il servizio *kea-dhcp4*.


.. code:: bash

    $ sudo systemctl (re)start kea-dhcp4
    

Da questo in momento in poi, se non ci sono errori, il servizio DHCP è attivo :)

