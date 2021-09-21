# Important Protocols

## [DHCP](https://www.logitrain.com.au/blog/the-dhcp-explained-simple-and-easy.html)

<figure>
    <img src="https://www.logitrain.com.au/wp-content/uploads/2021/09/DHCP-explained-simple-and-easy.jpg
" style="height:50%;width:50%;">
    <figcaption><a href=https://www.logitrain.com.au/blog/the-dhcp-explained-simple-and-easy.html>Logitrain</a></figcaption>
</figure>

This protocol is used to *dynamically assign* IP addresses to devices in a network.

When you're computer connects to your home wifi (via your WiFi router), here's what happens:

1. One of the first things that happens is your computer sends a **DHCP Discover**. This is a [broadcast](https://www.ionos.com/digitalguide/server/know-how/broadcast-address/) message which the DHCP server (the software running on the router, in this case) receives.
2. The DHCP server then sends back a **DHCP Offer** message, which contains an IP address, subnet mask, default gateway, and lease duration (how long it can be used for).
3. Your computer then sends back a **DHCP Request** message, asking to use the offered IP address.
4. The DHCP server finally sends back **DHCP Acknowledge**, an acknowledgement packet, which basically says, "I confirm you have accepted my offered IP address, welcome to the network".

This is known as **DORA** (Discover, Offer, Request Accept). 

> It's important to note that the DHCP server only offers IP addresses in a configured range, e.g., 192.168.56.1/24

## [ARP](https://study-ccna.com/arp/)

Let's say you and your brother, Josh, decide to talk to each other over the internet from the comfort of your own rooms (i.e. you're in the same LAN). His computer knows your computer's IP address, but it doesn't know the [MAC address](https://www.javatpoint.com/what-is-mac-address). 

> The MAC Address is the unique ID that belongs to your computer, this is more like the name of your computer whereas the IP address is the like the home address (which can change). As you saw before, the DHCP protocol doesn't guarantee you get the same IP address.

Josh's computer will first, check it's ARP Cache, which is just a table, maintained by your operating system, which records all the matching IP and MAC addresses.

* if there is **NO** matching MAC address for your IP address in his cache, his device will send an ARP (**address resolution protocol**) request which is just another broadcast (**remember:** broadcasts go to everyone on the network) asking who has the matching MAC address to the known IP address. Basically, it's saying, "Hey, I've got this IP address, who has the matching MAC address?".

    <img src="arp.png">

If there **IS** a match, this means either:
* someone's device replied with, "Yes that's me! Here's my MAC address: xxxx", then Josh's computer will update it's cache, OR
* there was a row in the cache containing a MAC address which matched the IP address

When the MAC address is found, Josh's device will proceed to attach the IP and MAC address to the message he wants to send, then send it off to the router to send to you. 

> [Here's](https://blog.ine.com/why-do-we-need-both-ip-addresses-and-mac-addresses) a site which explains why we need both MAC and IP addresses.

## NAT

Network Address Translation is an extremely important protocol that is happening CONSTANTLY, it is most definitely happening right now in your home.

As I said before, devices on a network have their own IP address distributed via the DHCP server (which is usually just your home router). But when we want to talk to the Internet (when I say Internet, I mean the entire WAN spanning the globe), we can't use these IP addresses. 

When I google something from my phone, the packet containing my phone's IP will go to my [default gateway](https://www.lifewire.com/what-is-a-default-gateway-817771) (usually just my home router) which will swap out my IP address for the address of the gateway itself. This swapping out is known as NAT.

We are translating our local IP address to our gateway's IP. **WHY?**

* This allows us to re-use IP addresses. Think about it: If we gave EVERY device it's own IP address and used that to send information over the internet, we'd be using up one IP address per device, right? Instead, we give each gateway (or home router for which each house typically has ONE) it's own IP address and allow devices in that LAN to re-use whatever IP it wants, we only spend one IP address per household (on average).
* Makes routing MUCH simpler. We are essentially reducing the amount of work routers have to do by limiting the number of calculations and hops ("jumps from router to router") they would need to make.
* Security reasons. Can act as sort of a firewall by hiding internal IP addresses. 