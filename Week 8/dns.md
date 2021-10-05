# Domain Name System

This **APPLICATION LAYER** protocol is what makes the internet possible.

## What does it do?

It maps names, called *domains*, like google.com, to IP addresses.

## How does it work?

[Super helpful short video](https://www.youtube.com/watch?v=72snZctFFtA)

When we visit a website like `www.google.com`, what we're actually searching for is: `www.google.com.`

There is a hidden dot at the end!

This is known as the root of the internet's namespace. **What does that mean??**

I could spend the time explaining it here, but honestly, the video I linked above explains it much better than I can, and in a fun way. I'd just be re-writing what the video shows which isn't very helpful. Trust me, it's a great video.

## DNS uses UDP. Why?? 

When we send data over the internet, sometimes referred to as "sending over IP", we know we can use transport layer protocols **TCP** and **UDP**.

We know UDP is unreliable but a lot faster than TCP, it also doesn't use a time-consuming [three-way handshake](https://www.guru99.com/tcp-3-way-handshake.html) procedure to establish a connection and transfer data. This means UDP, apart from being MUCH MUCH faster, can support many more clients simultaneously due to this lack of connection state.

From [CloudNS](https://www.cloudns.net/blog/dns-use-udp/), "In the DNS world, we are trying to cut the resolving time as much as possible. Seconds is an eternity, we want to reduce the time to just a few milliseconds".

## Useful Commands

### Dig

The `dig` command, "Domain Information Groper", in linux is used to perform DNS Lookup.

It sends DNS Queries to name servers listed in `/etc/resolf.conf`. These "name servers" are just servers which contain DNS records which look as follows:

```bash
[user$sahara ~]$ dig google.com
```

OUTPUT

<pre>
; <<>> DiG 9.16.21 <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 25133
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		235	IN	A	142.250.66.238

;; Query time: 0 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Tue Oct 05 11:22:07 AEDT 2021
;; MSG SIZE  rcvd: 55
</pre>

The result of this DNS query can be found in the "ANSWER SECTION". 

Let's break down the only answer: `google.com.		235	IN	A	142.250.66.238`

* 235 - TTL: time to live (seconds) before the record expires
* IN - Class: meaning Internet
* A - Type: IPv4 address
* 142.250.66.238 - Data: the IPv4 address of google.com

Also from the output, we can see a few other things:

The DNS Server we queried was `8.8.8.8`, which is Google's public DNS server.

## What is the HOSTS file??

I think [this](https://vitux.com/linux-hosts-file/) site has some cool examples on how to use it!

Very simply, the hosts file, located at `/etc/hosts` on linux and `C:\Windows\System32\drivers\etc` on Windows, contains lines of text which translate hostnames (e.g., google.com) to IP addresses. 

> NOTE: When you change and save this file, the [DNS Cache](https://www.lifewire.com/what-is-a-dns-cache-817514) is instantly updated.
