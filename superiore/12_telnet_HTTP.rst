===============
Telnet e HTTP *
===============

.. note::

    Prerequisti: **Windows, terminale**
    
    Argomenti trattati: **HTTP**

    
.. Qui inizia il testo dell'esperienza





TELNET e HTTP


telnet: > telnet www.example.com http

telnet: Trying 192.0.2.2...
telnet: Connected to www.example.com.
telnet: Escape character is '^]'.

client: HEAD /example/example.shtml HTTP/1.1
client: Host: www.example.com
client: Connection: close
client: 

server: HTTP/1.1 200 OK
server: Date: Wed, 21 Jan 2004 22:13:05 GMT
server: Server: Apache/1.3.12-Turbo
server: Connection: close
server: Content-Type: text/html

// ---------------------------------------------------------------------------------------------------------

telnet: > telnet www.example.com http

telnet: Trying 192.0.2.2...
telnet: Connected to www.example.com.
telnet: Escape character is '^]'.

client:  GET / HTTP/1.1
client: Host: www.example.com
client: Connection: close
client: 

server: HTTP/1.1 200 OK
server: Date: Wed, 21 Jan 2004 22:13:05 GMT
server: Server: Apache/1.3.12-Turbo
server: Connection: close
server: Content-Type: text/html

