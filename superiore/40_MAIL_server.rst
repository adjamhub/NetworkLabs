===========
Mail Server
===========

.. note::

    Prerequisti: **Raspberry, terminale linux**
    
    Argomenti trattati: **SMTP, POP, IMAP, URL, DNS**
      
    
.. Qui inizia il testo dell'esperienza


L'idea è quella di implementare un Mail Server completo su Raspberry, con un MTA per il protocollo SMTP, un server POP e un server IMAP per la
ricezione, l'invio e lo smistamento della posta elettronica.

Prima di andare avanti, ricordiamoci di aggiornare il sistema, ripulire e riavviare.

.. code-block:: bash

    $ sudo apt update
    $ sudo apt upgrade
    $ sudo apt autoremove
    $ sudo reboot


Configurare l'hostname
======================

La prima cosa da fare per raggiungere il nostro obiettivo è di sistemare **l'FQDN (Fully Qualified Domain Name)** del nostro computer.
Nel mio esempio esso sarà:

- HOSTNAME: **raspberrypi** 

- DOMAIN NAME: **scuola.lan** 

l'FQDN che identifica il sistema sarà dunque **raspberrypi.scuola.lan** con il servizio di posta installato in esso a servire il dominio
**@scuola.lan**.

.. note::
    Se durante l'esperienza di gestione della posta si vuole configurare anche il DNS, ricordatevi che dovete creare una zona autoritativa per
    il primo livello **.lan** e configurare in essa almeno i seguenti record:

    Record A: scuola.lan. 
        Punta l'IP del Raspberry.

    Record A: raspberrypi.scuola.lan.
        Punta l'IP del Raspberry.

    Record MX: scuola.lan.
        Punta il record A raspberrypi.scuola.lan

    Volendo è possibile aggiungere anche i terzi livelli *mail*, *pop*, *imap* (su record A) tutti che puntano l'IP del Raspberry.


Per impostare FQDN come desiderato, eseguiamo i seguenti compiti:

#. Modifica così il file ``host.conf``

.. code:: bash

    $ sudo nano /etc/host.conf

    order hosts,bind
    multi on

#. Modifica hostname completo (FQDN)

.. code:: bash

    $ sudo hostnamectl set-hostname raspberrypi.scuola.lan


#. Modifica file ``hosts``

.. code:: bash

    $ sudo nano /etc/hosts

    127.0.0.1       localhost

    127.0.1.1       raspberrypi.scuola.lan  raspberrypi
    

Riavvia il Raspberry e poi controlla il risultato con:

.. code:: bash

    $ hostname --short
    raspberrypi

    $ hostname --domain
    scuola.lan

    # hostname --fqdn
    raspberrypi.scuola.lan



Installare Postfix
==================


L'installazione è (come al solito) una riga di codice:

.. code:: bash

    $ sudo apt install postfix

Al termine dell'installazione c'è una fase iniziale di configurazione in cui verranno poste due domande:

#. il target del sistema di posta: selezionare **INTERNET**

#. il nome di host del sistema di posta: inserire il nome di dominio. Nel nostro esempio: **scuola.lan**.


Fatto questo vanno configurati alcuni file per il nostro caso specifico:

.. code:: bash

    $ sudo cp /etc/postfix/main.cf /etc/postfix/main.cf.BACKUP
    $ sudo nano /etc/postfix/main.cf

    smtpd_banner = $myhostname ESMTP $mail_name (Raspbian)
    biff = no

    # appending .domain is the MUA's job.
    append_dot_mydomain = no
    readme_directory = no

    # defaults to 2 on fresh installs
    compatibility_level = 2

    # TLS parameters
    smtpd_use_tls=no

    # general
    myhostname = raspberrypi.scuola.lan
    mydomain = scuola.lan

    alias_maps = hash:/etc/aliases
    alias_database = hash:/etc/aliases

    mydestination = $mydomain, $myhostname, localhost
    relayhost = 
    mynetworks = 127.0.0.0/8 172.25.37.0/24
    mailbox_size_limit = 0
    recipient_delimiter = +
    inet_interfaces = all
    inet_protocols = ipv4

    # use Maildir instead of mbox
    home_mailbox = Maildir/

Sistemate i valori delle variabili ``myhostname``, ``mydomain`` e ``mynetworks`` in base alle vostre necessità.


.. warning::

    **MAILDIR vs BOX**

    Nell'ultima riga del file abbiamo impostato il sistema Maildir di gestione della casella
    di posta invece del metodo di default chiamato mbox.
    
    In questo modo il sistema sistemerà la posta degli utenti nella cartella *Maildir* di ogni
    home, con evidenti vantaggi per l'amministratore (basta creare un utente per assicurargli anche
    una casella di posta) e per la sicurezza (nessun file esterno alla propria home a cui dover accedere).

    
Fatto questo siamo pronti per il primo step, l'avvio dell'MTA Postfix:

.. code:: bash

    $ sudo systemctl start postfix
    $ sudo systemctl status postfix



Aggiungere utenti
=================

Ogni utente che aggiungeremo al sistema operativo che ospita l'MTA avrà una casella di posta della forma `user@scuola.lan`.

Nei nostri test a scuola io aggiungo di solito una ventina di utenti con nome utente e password uguali a `studXX` con XX che va da 01 a 20 (o 25, o 30, a seconda
della quinta...).

Per fare un esperimento che ha senso occorre aggiungere almeno due utenti. Per farlo decidete i nomi e poi eseguite per ogni utente l'utitlity **adduser** come
amministratore, così:

.. code:: bash

    $ sudo adduser NOME_UTENTE_DA_CREARE

Poi rispondete a tutte le domande che vengono poste. Oppure saltatele tutte premendo INVIO, meno quelle sulla password (da inserire 2 volte).

Tutto qui!



Server POP e IMAP
=================

Per i server POP e IMAP si usa spesso la soluzione modulare **dovecot**, un software che contiene come moduli tutti i software di supporto ad un MTA.
A noi servono i server POP e IMAP e l'installazione è semplice come al solito.

.. code:: bash

    $ sudo apt install dovecot-pop3d dovecot-imapd


La configurazione di entrambi i moduli si basa su pochi file che dobbiamo modificare per il funzionamento *classico* che ci interessa.


Primo file, il file di configurazione principale `dovecot.conf` che va impostato per accettare tutte le connessioni in ingresso:

.. code:: bash

    $ sudo nano /etc/dovecot/dovecot.conf

    listen = *

    
Secondo file, quello che specifica quale tipo di contenitore di posta utilizza l'MTA

.. code:: bash

    $ sudo nano /etc/dovecot/conf.d/10-mail.conf

    mail_location = maildir:~/Maildir

    
Terzo e ultimo file, quello che configurare l'accesso senza cifratura

.. code:: bash

    $ sudo nano /etc/dovecot/conf.d/10-auth.conf
    
    disable_plaintext_auth = no
    auth_mechanisms = plain login


Salvato tutto, basta avviare e controllare:

.. code:: bash

    $ sudo systemctl start dovecot
    $ sudo systemctl status dovecot



Mail Test
=========

Per fare un test approfondito dell'ambaradan che abbiamo messo su occorrerebbe testare il sistema con almeno 3 MUA (Mail User Agent), di cui almeno 2 configurati
per la ricezione con IMAP (per testare la possibilità di ritrovare la mail in entrambi) e almeno uno con POP verificando successivamente con uno dei client IMAP 
che la posta è effettivamente scomparsa.

Si può inoltre provare anche l'esperienza **Telnet e Mail** da qualche parte in questo stesso sito.

Per quanto riguarda i MUA provo a suggerirvi alcuni software da testare da soli:

- le web applications ``squirrelmail`` (http://squirrelmail.org) oppure ``rainloop`` (https://rainloop.net). Necessitano entrambe di un server web con PHP. Sono entrambe forzatamente client IMAP

- l'applicazione ``E-Mail`` dello smartphone, che contiene sia un client IMAP che POP, ma che è chiaramente ottimizzata per un utilizzo con IMAP.

- l'applicazione desktop ``Mozilla Thunderbird`` (https://www.thunderbird.net/) che ovviamente contiene sia un client IMAP che POP.


**Buon divertimento!**





