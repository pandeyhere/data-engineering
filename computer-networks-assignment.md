
# Assignment 2

## Task 1: Use nslookup or dig to do a dns lookup on www.growthschool.io and see what is the response coming as. 

``` bash
mapandey@mapandeyGMD6R Downloads % nslookup www.growthschool.io
Server:		10.112.16.144
Address:	10.112.16.144#53

Non-authoritative answer:
www.growthschool.io	canonical name = proxy-ssl.webflow.com.
proxy-ssl.webflow.com	canonical name = proxy-ssl-geo.webflow.com.
Name:	proxy-ssl-geo.webflow.com
Address: 13.200.123.229
Name:	proxy-ssl-geo.webflow.com
Address: 65.0.79.182
Name:	proxy-ssl-geo.webflow.com
Address: 13.234.100.116
```


## Task 2:  Figure out how can you use nslookup to find name and IP address of SMTP server of gmail.com

``` bash
mapandey@mapandeyGMD6R Downloads % nslookup
> set type=MX
> gmail.com
Server:		10.112.16.144
Address:	10.112.16.144#53

Non-authoritative answer:
gmail.com	mail exchanger = 40 alt4.gmail-smtp-in.l.google.com.
gmail.com	mail exchanger = 10 alt1.gmail-smtp-in.l.google.com.
gmail.com	mail exchanger = 20 alt2.gmail-smtp-in.l.google.com.
gmail.com	mail exchanger = 5 gmail-smtp-in.l.google.com.
gmail.com	mail exchanger = 30 alt3.gmail-smtp-in.l.google.com.

Authoritative answers can be found from:
.	nameserver = c.root-servers.net.
.	nameserver = i.root-servers.net.
.	nameserver = j.root-servers.net.
.	nameserver = l.root-servers.net.
.	nameserver = e.root-servers.net.
.	nameserver = d.root-servers.net.
.	nameserver = a.root-servers.net.
.	nameserver = f.root-servers.net.
.	nameserver = b.root-servers.net.
.	nameserver = h.root-servers.net.
.	nameserver = k.root-servers.net.
.	nameserver = g.root-servers.net.
.	nameserver = m.root-servers.net.
j.root-servers.net	internet address = 192.58.128.30
a.root-servers.net	internet address = 198.41.0.4
m.root-servers.net	internet address = 202.12.27.33
g.root-servers.net	internet address = 192.112.36.4
K.root-servers.net	internet address = 193.0.14.129
D.root-servers.net	internet address = 199.7.91.13
c.root-servers.net	internet address = 192.33.4.12
l.root-servers.net	internet address = 199.7.83.42
B.root-servers.net	internet address = 199.9.14.201
```

## Task 3: Suppose you have a web server running on your network that is listening on port 80. Write a TCPdump command that captures all HTTP traffic coming to the server and saves it to a file called "http_traffic.pcap"

### I have assumed we need to save 1 file, capturing for 10 secs.

``` bash
tcpdump -s 96 -w http_traffic.pcap port 80 -G 10 -W 1
```