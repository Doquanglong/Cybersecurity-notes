# 📚 Networking — General Knowledge

Foundational networking concepts explained in plain English. Each term has:
**what it is → why it matters (esp. for security) → a real-life example.**
Inspired by CompTIA Network+ fundamentals.

---

## Table of Contents

1. [What is a network?](#1-what-is-a-network)
2. [The OSI Model & TCP/IP Model](#2-the-osi-model--tcpip-model)
3. [IP Address](#3-ip-address)
4. [MAC Address](#4-mac-address)
5. [Ports & Protocols](#5-ports--protocols)
6. [TCP vs UDP](#6-tcp-vs-udp)
7. [DNS — the internet's phonebook](#7-dns--the-internets-phonebook)
8. [DHCP — automatic addressing](#8-dhcp--automatic-addressing)
9. [NAT — sharing one public address](#9-nat--sharing-one-public-address)
10. [Network devices: hub, switch, router](#10-network-devices-hub-switch-router)
11. [Firewalls](#11-firewalls)
12. [Client-Server vs Peer-to-Peer (P2P)](#12-client-server-vs-peer-to-peer-p2p)
13. [Putting it together: what happens when you visit a website](#13-putting-it-together-what-happens-when-you-visit-a-website)

---

## 1. What is a network?

**What it is:** Two or more devices connected so they can exchange data. Your home
Wi-Fi, an office LAN, and the entire internet are all networks — just different sizes.

- **LAN (Local Area Network):** devices in one location (home, office).
- **WAN (Wide Area Network):** networks connected across large distances; the
  **internet** is the biggest WAN.

**Why it matters for security:** The boundary between "inside" (trusted LAN) and
"outside" (untrusted internet) is where most defenses live — firewalls, monitoring,
segmentation. Attackers try to cross that boundary or move *laterally* once inside.

**Real-life example:** At home, your laptop, phone, and TV are on a LAN through your
router. When you stream a video, your request leaves the LAN, travels the WAN
(internet) to a server, and the video streams back.

---

## 2. The OSI Model & TCP/IP Model

**What it is:** A layered model that breaks networking into steps, so each layer
only worries about its own job and hands off to the next. The **OSI model** has 7
layers; the **TCP/IP model** is a simpler 4-layer version used in practice.

| OSI Layer | Name | Example |
|-----------|------|---------|
| 7 | Application | HTTP, DNS, your browser |
| 6 | Presentation | Encryption (TLS), encoding |
| 5 | Session | Keeping a connection open |
| 4 | Transport | TCP, UDP, ports |
| 3 | Network | IP addresses, routing |
| 2 | Data Link | MAC addresses, switches |
| 1 | Physical | Cables, Wi-Fi radio, signals |

> 🧠 Memory aid (7→1): **"All People Seem To Need Data Processing."**
> 🧠 Memory aid (1→7): **"Please Do Not Throw Sausage Pizza Away."**

**A better way to picture it — the 7-story building 🏢:** Imagine the network as a
seven-story building, and your data is a courier that has to travel between floors.
Each floor is its own little world with its own job and "language." When you send
something, the courier starts at the **top floor (Layer 7 — the app you're using)**
and walks *down* one floor at a time to reach the street (the physical wire). It
can't skip floors — it has to pass through every one.

**The key idea — encapsulation (envelopes inside envelopes):** at each floor going
down, a clerk wraps your data in a new "envelope" with extra delivery info. This
wrapping is called **encapsulation**, and the package even changes name at each layer:

| Going DOWN (sending) | What gets added | Package is now called |
|----------------------|-----------------|-----------------------|
| L7 Application | your actual data (the request) | data |
| L6 Presentation | encryption (TLS), formatting | data |
| L5 Session | keeps the conversation tracked | data |
| L4 Transport | port number + TCP/UDP | **segment** |
| L3 Network | source & destination **IP** | **packet** |
| L2 Data Link | source & destination **MAC** | **frame** |
| L1 Physical | turned into raw 1s and 0s | **bits** |

On the **receiving** device it runs in **reverse**: bits arrive at Layer 1 and travel
*up*, each floor stripping off its own envelope (**de-encapsulation**) until the
original data reaches the app on Layer 7. Same seven floors, opposite direction — like
a mail room unwrapping a package layer by layer to reveal the letter inside.

**Why it matters for security:** Attacks and tools map to specific layers, so naming
the layer tells you where to look and what defense applies:
- **L1 Physical** — cutting/tapping a cable, rogue Wi-Fi.
- **L2 Data Link** — MAC spoofing, ARP poisoning (man-in-the-middle).
- **L3 Network** — IP spoofing, DDoS floods, routing attacks.
- **L4 Transport** — SYN floods, port scanning.
- **L7 Application** — phishing, SQL injection, malware in web requests.

A firewall that only filters IPs/ports (L3/L4) won't catch a phishing email (L7) —
that's why you layer *different* defenses at *different* layers ("defense in depth").

**Real-life example:** Sending a letter. You write it (application), seal it in an
envelope (presentation/encryption), address it (network/IP), the post office sorts and
routes it (data link/physical). Each step doesn't care what the others do — it just
does its part and passes it along.

---

## 3. IP Address

**What it is:** A numeric label that identifies a device on a network, so data
knows where to go. Like a mailing address for a computer.

- **IPv4:** four numbers 0–255, e.g. `192.168.1.10`. Limited (~4 billion addresses).
- **IPv6:** much longer, e.g. `2001:0db8:85a3::8a2e:0370:7334`. Created because IPv4
  ran out.
- **Public IP:** reachable from the internet (assigned by your ISP).
- **Private IP:** used inside a LAN, not routable on the internet. Reserved ranges:
  `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.

**Why it matters for security:** IPs are how you identify who's talking. Firewalls
allow/block by IP, logs record source IPs, and attackers spoof or hide them (via
proxies/VPNs). Private vs public matters for what's exposed to the internet.

**Real-life example:** `192.168.1.x` addresses in your home are like apartment
numbers *inside* a building — meaningless to the outside world. Your router's public
IP is the building's street address that the mail carrier (internet) actually uses.

---

## 4. MAC Address

**What it is:** A hardware address burned into a device's network card, e.g.
`00:1A:2B:3C:4D:5E`. Unlike an IP (which can change), the MAC identifies the
physical device on a local network.

**IP vs MAC in one line:** IP = *where* you are (can change as you move networks);
MAC = *who* the physical device is (fixed). Local delivery uses MAC; long-distance
routing uses IP.

**Why it matters for security:** Attackers **spoof** MAC addresses to bypass
Wi-Fi filters or impersonate devices. **ARP spoofing** abuses the IP↔MAC mapping to
intercept traffic (a man-in-the-middle attack).

**Real-life example:** Think of the IP as the name on a package and the MAC as the
exact person's fingerprint. Within your local network (the mailroom), the switch
uses the fingerprint (MAC) to hand the package to the right device.

---

## 5. Ports & Protocols

**What it is:** A **port** is a numbered "door" on a device for a specific service,
so one machine can run many services at once. A **protocol** is the agreed language
two devices use. Ports range `0–65535`.

**Common ports to know:**

| Port | Protocol | Used for |
|------|----------|----------|
| 20/21 | FTP | File transfer |
| 22 | SSH | Secure remote login |
| 23 | Telnet | Remote login (insecure, plaintext) |
| 25 | SMTP | Sending email |
| 53 | DNS | Domain name lookups |
| 80 | HTTP | Web (unencrypted) |
| 443 | HTTPS | Web (encrypted with TLS) |
| 3389 | RDP | Windows remote desktop |

**Why it matters for security:** Port scanning (e.g. `nmap`) is often step one of an
attack — open ports reveal which services (and possible vulnerabilities) a target
runs. Defenders close unused ports to shrink the "attack surface."

**Real-life example:** A building (IP address) with many numbered doors (ports).
Deliveries go to door 443 for secure web, door 22 for admin/SSH. If a door you don't
use is left unlocked (open port), someone might sneak in.

---

## 6. TCP vs UDP

**What it is:** Two transport-layer protocols for actually moving data.

- **TCP (Transmission Control Protocol):** reliable. Establishes a connection
  (the **3-way handshake**: SYN → SYN-ACK → ACK), guarantees delivery and order,
  resends lost data. Slower but accurate.
- **UDP (User Datagram Protocol):** fast, "fire and forget." No connection, no
  guarantee of delivery or order. Great for speed-sensitive traffic.

| | TCP | UDP |
|--|-----|-----|
| Reliable? | Yes | No |
| Ordered? | Yes | No |
| Speed | Slower | Faster |
| Use | Web, email, files | Video calls, gaming, DNS |

**Why it matters for security:** The TCP handshake is abused in **SYN flood** DDoS
attacks (sending many SYNs, never finishing). UDP's connectionless nature makes it
easy to **spoof** and use in amplification attacks.

**Real-life example:** TCP is a phone call — you confirm the other person heard each
sentence ("did you get that?"). UDP is shouting across a room — fast, but you don't
check if every word landed. A laggy video call drops UDP frames rather than freezing.

---

## 7. DNS — the internet's phonebook

**What it is:** The **Domain Name System** translates human-friendly names
(`google.com`) into IP addresses (`142.250.72.14`) that computers actually use.

**How it works (simplified):**
1. You type `example.com`.
2. Your computer asks a **DNS resolver** (usually your ISP's or `8.8.8.8`).
3. The resolver walks the hierarchy: root → `.com` server → `example.com`'s server.
4. It returns the IP; your browser connects to it. The answer is **cached** for speed.

**Why it matters for security:** DNS is a huge target and tool. **DNS spoofing/
poisoning** sends you to a fake IP (phishing). Malware uses **DNS tunneling** to
sneak data out because DNS traffic (port 53) is often allowed through firewalls.

**Real-life example:** You know your friend's name but not their phone number, so you
look them up in contacts. DNS is that contacts app — you know `netflix.com`, DNS
finds the actual number (IP) to dial.

---

## 8. DHCP — automatic addressing

**What it is:** **Dynamic Host Configuration Protocol** automatically hands out IP
addresses (and gateway/DNS settings) to devices when they join a network, so you
don't configure each one by hand.

**The handshake (DORA):** **D**iscover → **O**ffer → **R**equest → **A**cknowledge.

**Why it matters for security:** A rogue DHCP server can hand out malicious settings
(e.g. point you to an attacker's DNS or gateway) — a **man-in-the-middle** setup.
DHCP logs also help trace which device had which IP at a given time.

**Real-life example:** Joining hotel Wi-Fi and instantly getting internet without
typing any settings — DHCP gave your phone an address and told it where the "exit"
(gateway) is, like a receptionist assigning you a room on arrival.

---

## 9. NAT — sharing one public address

**What it is:** **Network Address Translation** lets many private devices share a
single public IP. Your router rewrites the source address of outgoing traffic to its
public IP, and remembers who to send replies back to.

**Why it matters for security:** NAT gives a mild layer of hiding — outside hosts
can't directly reach your internal devices, since they only see the router's public
IP. (It's a side effect, not a real firewall, but it helps.)

**Real-life example:** An office where everyone shares one main phone number. Calls
go out under that number; the receptionist (router) routes incoming replies to the
right extension (internal device). Outsiders never see the individual extensions.

---

## 10. Network devices: hub, switch, router

**What they are:** Devices that connect and direct traffic, at different levels of
"smart."

- **Hub (dumb):** repeats incoming data out **every** port. Wasteful and insecure —
  everyone sees everyone's traffic. Largely obsolete.
- **Switch (smart, local):** learns which MAC is on which port and sends data **only**
  to the right device. Operates at Layer 2. The backbone of a LAN.
- **Router (connects networks):** moves traffic **between** networks using IP
  addresses (Layer 3). Your home router also usually does NAT, DHCP, and firewalling.

**Why it matters for security:** Switches limit who can see traffic (harder to
eavesdrop than a hub) — which is why attackers use tricks like ARP spoofing or MAC
flooding to defeat them. Routers are the gatekeepers between trusted and untrusted
networks.

**Real-life example:** A hub is a person shouting a message to a whole room. A switch
is handing a note directly to the one person it's for. A router is the mailroom that
sends notes to *other* buildings.

---

## 11. Firewalls

**What it is:** A device or software that filters network traffic based on rules,
allowing or blocking it. The primary gatekeeper between networks.

- **Packet-filtering:** decides based on IP/port/protocol (Layer 3/4).
- **Stateful:** tracks the state of connections (remembers what you initiated).
- **Next-gen (NGFW):** also inspects application-layer content, can detect malware,
  intrusion attempts, etc.

**Why it matters for security:** Firewalls enforce the "what's allowed in/out" policy.
Misconfigured rules (too open) are a top cause of breaches; overly strict ones break
legitimate traffic. Reading firewall logs is a core defensive skill.

**Real-life example:** A club bouncer with a guest list. Traffic (people) trying to
enter is checked against rules — on the list? come in. Not allowed? turned away. A
stateful firewall also remembers "this person already came in and just stepped out
for a moment," so it lets them back.

---

## 12. Client-Server vs Peer-to-Peer (P2P)

**What it is:** Two fundamental ways to organize how devices share resources.

- **Client-Server:** A central **server** provides resources/services; **clients**
  request them. The server is dedicated and always-on. Most of the internet works
  this way (websites, email, databases).
- **Peer-to-Peer (P2P):** Every device (a **peer**) is *both* client and server at
  once — they share resources directly with each other, with no central authority.
  Each peer can request from and provide to any other peer.

| | Client-Server | Peer-to-Peer (P2P) |
|--|---------------|--------------------|
| Control | Centralized (one server) | Decentralized (all peers equal) |
| Scaling | Server can bottleneck | More peers = more capacity |
| Single point of failure? | Yes — server goes down, all down | No — others keep going |
| Cost/setup | Needs a dedicated server | Cheap, no central server |
| Examples | Websites, Gmail, online banking | BitTorrent, blockchain, some VoIP |

**How P2P works (simplified):** Instead of everyone downloading from one server, each
peer downloads pieces of a file from *many* other peers and simultaneously uploads
the pieces it already has. The more people sharing, the faster it gets — the opposite
of a server that slows down under load.

**Why it matters for security:**
- **No central control** cuts both ways: there's no single server to take down
  (resilient), but also **no central authority to vet content** — P2P networks spread
  malware and pirated files easily, and you're connecting directly to strangers' machines.
- **Exposure:** as a peer, you're also acting as a server, so your IP is visible to
  every peer you connect to (privacy/attack-surface concern).
- **Botnets** often use P2P architecture specifically because there's no central
  command server for defenders to find and shut down — orders propagate peer to peer.
- **Blockchain** (Bitcoin, etc.) is P2P by design: no central bank, every node holds
  a copy of the ledger, making it very hard to tamper with or shut down.

**Real-life example:**
- *Client-Server* = a **library**. One central building (server) holds the books;
  everyone (clients) goes there to borrow. If the library closes, no one gets books.
- *Peer-to-Peer* = a **neighborhood book-swap**. Everyone keeps books at home and
  lends directly to each other. No central building to fail — but also no librarian
  checking that the books are safe or legit. This is exactly how **BitTorrent** works:
  you grab a movie in pieces from dozens of other users' computers at once, while
  sharing the pieces you already have back to them.

---

## 13. Putting it together: what happens when you visit a website

This is the single best exercise for tying networking together: **one everyday action
touches almost every concept in this file.** Let's follow it as a story.

> **The 10-second version:** Your computer looks up the site's address (DNS), gets a
> reliable connection to it (TCP), locks that connection with encryption (TLS), asks
> for the page (HTTP), and the server sends it back. Your router and firewalls handle
> the traffic along the way.

### The story, step by step 📖

Think of it like **ordering food from a restaurant you've only heard the name of.**

**Stage 1 — "What's the address?" (DNS)** 📖 *Section 7*
You type `example.com`, but computers don't understand names — they need an IP. So
your computer asks a DNS resolver, *"what's the number for example.com?"* and gets
back something like `93.184.216.34`.
> 🧠 Like Googling the restaurant's address before you can drive there.

**Stage 2 — "Do I even have a way out?" (DHCP + your own IP)** 📖 *Section 8*
This already happened when you joined the network: DHCP gave your device its own IP
address and told it where the exit (the router/gateway) is.
> 🧠 You already know your own home address and which road leads out of the neighborhood.

**Stage 3 — "Send the request out the door" (Router + NAT)** 📖 *Sections 9, 10*
Your request leaves your private network through the router. NAT swaps your private
IP for the router's single public IP, and remembers it was *you* who asked, so the
reply comes back to your device.
> 🧠 The whole office sends mail under one return address; the mailroom remembers who sent what.

**Stage 4 — "Knock on the right door" (Ports + TCP handshake)** 📖 *Sections 5, 6*
Your computer contacts the server's IP on **port 443** (the door for HTTPS) and does
the **3-way handshake** (SYN → SYN-ACK → ACK) to set up a reliable connection.
> 🧠 Calling the restaurant and both of you confirming "can you hear me?" — "yes, can you?" — "yes."

**Stage 5 — "Whisper, don't shout" (TLS encryption)** 📖 *OSI Layer 6*
Because it's HTTP**S**, the two sides negotiate encryption (TLS). From now on,
anything sent is scrambled — anyone snooping just sees gibberish.
> 🧠 Switching to a private language so eavesdroppers at the next table learn nothing.

**Stage 6 — "Here's my actual order" (HTTP request/response)** 📖 *OSI Layer 7*
Now your browser sends the real request: *"GET me the homepage."* The server replies
with the HTML, images, and scripts. Your browser assembles them into the page you see.
> 🧠 Finally telling the waiter your order, and the food arriving at your table.

**All along the way — security checkpoints (Firewalls / IDS / IPS)** 📖 *Section 11*
At several points, firewalls decide if the traffic is allowed, and intrusion systems
watch for anything suspicious (IDS alerts, IPS blocks).
> 🧠 Security guards and cameras checking people at every entrance along the route.

### How it maps to the OSI layers (why the model is practical)

The same request, as it goes *down* your device's layers (encapsulation from Section 2):

```
L7 Application   "GET / HTTP/1.1"  ← your browser's request
L6 Presentation  encrypt with TLS
L4 Transport     add port 443 + TCP → segment
L3 Network       add source/dest IP → packet
L2 Data Link     add MAC addresses  → frame
L1 Physical      send as 1s and 0s over Wi-Fi/cable
        │
        ▼  travels across the internet, and the server's device
           unwraps it in REVERSE (L1 → L7) to read your request.
```

**The takeaway:** every one of these stages is a place where something can be
**secured, monitored, or attacked** — spoof the DNS answer (Stage 1), sniff an
unencrypted connection (skip Stage 5), flood the handshake (Stage 4), inject into the
HTTP request (Stage 6). That's exactly why this networking foundation matters for
cybersecurity: **you can't defend or investigate a step you don't understand.**

---

> ✍️ **To extend this file:** keep the same pattern for each new term —
> **what it is → why it matters for security → real-life example** — so it stays
> consistent and easy to review.
