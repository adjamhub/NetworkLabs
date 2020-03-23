=============
Telnet Mail *
=============

.. note::

    Prerequisti: **Windows, terminale**
    
    Argomenti trattati: **Telnet, SMTP, POP, IMAP**
      
    
.. Qui inizia il testo dell'esperienza


TELNET e SMTP


telnet: > telnet mx1.example.com smtp

telnet: Trying 192.0.2.2...
telnet: Connected to mx1.example.com.
telnet: Escape character is '^]'.
server: 220 mx1.example.com ESMTP server ready Tue, 20 Jan 2004 22:33:36 +0200

client: HELO client.example.com

server: 250 mx1.example.com

client: MAIL from: <sender@example.com>

server: 250 Sender <sender@example.com> Ok

client: RCPT to: <recipient@example.com>

server: 250 Recipient <recipient@example.com> Ok

client: DATA

server: 354 Ok Send data ending with <CRLF>.<CRLF>

client: From: sender@example.com
client: To: recipient@example.com
client: Subject: Test message
client: 
client: This is a test message.
client: .

server: 250 Message received: 20040120203404.CCCC18555.mx1.example.com@client.example.com

client: QUIT

server: 221 mx1.example.com ESMTP server closing connection




TELNET e POP3


telnet: > telnet pop.example.com pop3

telnet: Trying 192.0.2.2...
telnet: Connected to pop.example.com.
telnet: Escape character is '^]'.
server: +OK InterMail POP3 server ready.

client: USER MyUsername

server: +OK please send PASS command

client: PASS MyPassword

server: +OK MyUsername is welcome here

client: LIST

server: +OK 1 messages
server: 1 1801
server: .

client: RETR 1

server: +OK 1801 octets
server: Return-Path: sender@example.com
server: Received: from client.example.com ([192.0.2.1])
server:        by mx1.example.com with ESMTP
server:        id <20040120203404.CCCC18555.mx1.example.com@client.example.com>
server:        for <recipient@example.com>; Tue, 20 Jan 2004 22:34:24 +0200
server: From: sender@example.com
server: Subject: Test message
server: To: recipient@example.com
server: Message-Id: <20040120203404.CCCC18555.mx1.example.com@client.example.com>
server: 
server: This is a test message.
server: .

client: DELE 1

server: +OK

client: quit

server: +OK MyUsername InterMail POP3 server signing off.



TELNET e IMAP


telnet: > telnet imap.example.com imap

telnet: Trying 192.0.2.2...
telnet: Connected to imap.example.com.
telnet: Escape character is '^]'.
server: * OK Dovecot ready.

client: a1 LOGIN MyUsername MyPassword

server: a1 OK Logged in.

client: a2 LIST "" "*"

server: * LIST (\HasNoChildren) "." "INBOX"
server: a2 OK List completed.

client: a3 EXAMINE INBOX

server: * FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
server: * OK [PERMANENTFLAGS ()] Read-only mailbox.
server: * 1 EXISTS
server: * 1 RECENT
server: * OK [UNSEEN 1] First unseen.
server: * OK [UIDVALIDITY 1257842737] UIDs valid
server: * OK [UIDNEXT 2] Predicted next UID
server: a3 OK [READ-ONLY] Select completed.

client: a4 FETCH 1 BODY[]

server: * 1 FETCH (BODY[] {405}
server: Return-Path: sender@example.com
server: Received: from client.example.com ([192.0.2.1])
server:         by mx1.example.com with ESMTP
server:         id <20040120203404.CCCC18555.mx1.example.com@client.example.com>
server:         for <recipient@example.com>; Tue, 20 Jan 2004 22:34:24 +0200
server: From: sender@example.com
server: Subject: Test message
server: To: recipient@example.com
server: Message-Id: <20040120203404.CCCC18555.mx1.example.com@client.example.com>
server: 
server: This is a test message.
server: )
server: a4 OK Fetch completed.

client: a5 LOGOUT

server: * BYE Logging out
server: a5 OK Logout completed.





