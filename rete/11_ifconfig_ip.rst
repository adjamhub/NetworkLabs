============
ifconfig, ip
============

.. note::

    Prerequisti: **Linux, MacOS: terminale**
    
    Argomenti trattati: **Indirizzamento IP**
      
    
.. Qui inizia il testo dell'esperienza


Nell'esperienza **ipconfig** abbiamo visto come è possibile reperire informazioni sulla configurazione di rete
in un terminale Windows.

In questa esperienza faremo lo stesso nel caso dei terminali Linux e Mac. Ovviamente tutte le considerazioni qui fatte
funzionano anche su Raspberry.

Nella mia disamina ho deciso di spiegare le cose 2 volte, prima con il comando **ifconfig** e poi con il comando **ip**. La scelta di raddoppiare
il lavoro dipende da una serie di considerazioni che vado ad elencare:

- *ifconfig* è un utility più limitata rispetto alla più moderna *ip*

- Non sono sicuro che il comando *ip* sia disponibile su Mac (probabilmente sì...)

- In molte distribuzioni Linux potreste non trovare il (vecchio) comando *ifconfig*

- *ifconfig* è più vecchia e limitata ma più semplice

- *ip* è in grado di gestire praticamente tutte le configurazioni del livello di rete e inferiore, ma questo implica un diverso grado di complessità


Mettendo insieme tutti questi *statements* ho deciso di introdurre entrambi i tools. Vediamoli.

Nelle due trattazioni che seguono cercherò di dedurre la configurazione di rete di un generico dispositivo che ha una scheda di rete con cavo,
chiamata **eth0** e una scheda di rete wifi chiamata **wlan0**. Potrebbe essere un portatile, oppure un Raspberry, etc...
Indico qua le informazioni in modo tale che sia più semplice capire il funzionamento dei tool di rete, conoscendo in anticipo l'output che cerchiamo.

====================== ===================
Descrizione            Valore
====================== ===================
Rete                   10.0.0.0
Subnet mask            255.255.255.0
broadcast              10.255.255.255
Gateway                10.0.0.1
Server DNS             10.0.0.2
Server DHCP            10.0.0.3
IP scheda con cavo     10.0.0.51
IP scheda wifi         10.0.0.52
====================== ===================


ifconfig
========


Visualizzare informazioni sulle interfacce di rete

.. code:: bash

    $ ifconfig

    eth0:   flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 10.0.0.51  netmask 255.0.0.0  broadcast 10.255.255.255
            ether 54:53:ed:XX:XX:XX  txqueuelen 1000  (Ethernet)
            RX packets 95414  bytes 130702336 (124.6 MiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 43485  bytes 4338669 (4.1 MiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 4  bytes 240 (240.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 4  bytes 240 (240.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    wlan0:  flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 10.0.0.52  netmask 255.0.0.0  broadcast 10.255.255.255
            ether b8:76:3f:YY:YY:YY  txqueuelen 1000  (Ethernet)
            RX packets 7035  bytes 1837515 (1.7 MiB)
            RX errors 0  dropped 1496  overruns 0  frame 0
            TX packets 377  bytes 33009 (32.2 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

            

Imopostare un indirizzo (o cancellarlo) per una interfaccia di rete


.. code:: bash

    $ sudo ifconfig eth0 add 192.168.0.51
    $ sudo ifconfig eth0 del 192.168.0.51


    
Abilitare o disabilitare una interfaccia di rete


.. code:: bash

    $ sudo ifconfig wlan0 up
    $ sudo ifconfig wlan0 down

    
Visualizzare la tabella di routing (verificando il gateway predefinito). Con *ifconfig* non si può fare. In questo caso 
bisogna ricorrere al comando **route**:

.. code:: bash

    $ route -n4

    Kernel IP routing table
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    0.0.0.0         10.0.0.1        0.0.0.0         UG    100    0        0 eth0
    0.0.0.0         10.0.0.1        0.0.0.0         UG    600    0        0 wlan0
    10.0.0.0        0.0.0.0         255.0.0.0       U     100    0        0 eth0
    10.0.0.0        0.0.0.0         255.0.0.0       U     600    0        0 wlan0
    

Impostare il default gateway (oppure in caso di routing più complessi, aggiungere una route). Oppure rimuoverlo.
Ancora tramite l'utility *route*:


.. code:: bash

    $ sudo route add default gw 192.168.0.1 eth0
    $ sudo route del default gw 192.168.0.1 eth0
    
    
Visualizzare i server DNS in uso. Ancora una volta **non** si usano opzioni del comando *ifconfig* ma si può controllare direttamente
sul file ove sono scritti:

.. code:: bash

    $ cat /etc/resolv.conf
    
    nameserver 10.0.0.2


ip
==

Visualizzare informazioni sulle interfacce di rete


.. code:: bash

    $ ip a
    
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
        valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
        link/ether 54:53:ed:XX:XX:XX brd ff:ff:ff:ff:ff:ff
        inet 10.0.0.51/8 brd 10.255.255.255 scope global dynamic noprefixroute eth0
        valid_lft 80942sec preferred_lft 80942sec
    3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether b8:76:3f:YY:YY:YY brd ff:ff:ff:ff:ff:ff
        inet 10.0.0.52/8 brd 10.255.255.255 scope global dynamic noprefixroute wlan0
        valid_lft 80939sec preferred_lft 80939sec


Imopostare un indirizzo (o cancellarlo) per una interfaccia di rete


.. code:: bash

    $ sudo ip a add 192.168.0.51 dev eth0    
    $ sudo ip a del 192.168.0.51 dev eth0


    
Abilitare o disabilitare una interfaccia di rete


.. code:: bash

    $ sudo ip link set wlan0 up
    $ sudo ip link set wlan0 down


    
Visualizzare la tabella di routing (verificando il gateway predefinito).


.. code:: bash

    $ ip r

    default via 10.0.0.1 dev eth0 proto dhcp metric 100 
    default via 10.0.0.1 dev wlan0 proto dhcp metric 600 
    10.0.0.0/8 dev eth0 proto kernel scope link src 10.0.0.51 metric 100 
    10.0.0.0/8 dev wlan0 proto kernel scope link src 10.0.0.52 metric 600
    
    
Impostare il default gateway (oppure in caso di routing più complessi, aggiungere una route).
Oppure rimuoverlo.

.. code:: bash

    $ sudo ip r add 192.168.0.0/24 via 192.168.0.1 dev eth0
    $ sudo ip r del 192.168.0.0/24
    

Visualizzare i server DNS in uso. Qui anche l'utility *ip* non può arrivare perché il sistema di risoluzione degli indirizzi è diverso in
ambito UNIX (Linux/MAC) rispetto al corrispettivo Windows. Il consiglio è ancora una volta di controllare il file di configurazione:


.. code:: bash

    $ cat /etc/resolv.conf
    
    nameserver 10.0.0.2
