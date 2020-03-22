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

nella nostra prova sarà raspberrypi.scuola.lan

$ sudo nano /etc/host.conf

order hosts,bind
multi on


$ sudo hostnamectl set-hostname raspberrypi.scuola.lan

$ sudo nano /etc/hosts

127.0.0.1       localhost

127.0.1.1       raspberrypi.scuola.lan  raspberrypi

Riavviare

Controlla con:

$ hostname --short
raspberrypi

$ hostname --domain
scuola.lan

# hostname --fqdn
raspberrypi.scuola.lan



Installare Postfix
==================

$ sudo apt install postfix

Seleziona Internet

Scegli l'hostname impostato prima

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


Warning MAILDIR vs BOX

e poi

$ sudo systemctl start postfix
$ sudo systemctl status postfix


Aggiungere utenti
=================

$ sudo adduser NOME

(poi rispondi alle domande. Oppure saltale tutte premendo INVIO, meno quelle sulla password)


Server POP e IMAP
=================

$ sudo apt install dovecot-pop3d dovecot-imapd


$ sudo nano /etc/dovecot/dovecot.conf

listen = *


$ sudo nano /etc/dovecot/conf.d/10-mail.conf

mail_location = maildir:~/Maildir


Mail (web) client
=================

squirrelmail





