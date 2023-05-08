# The Triadically Functional Network Redistribution Protocol

The Triadically Functional Network Redistribution Protocol, TFNr for short, is a revolutionary new blackhole routing protocol devised by yours truly.

This protocol builds off of the current capabilities of MANETs, namely GPSR and AODV (2 of the most prominent). 

This repo contains the basis for a custom network partitioning schema in which networks are segemented in a need-based orientation. As traffic is being dynamically generated and passed through a central entity (in this case it'll be a Qube which I will get to in a second), a custom structural control flow algorithm will be deployed to sporadically analyze this traffic's entry and exit node calls.

The functionality of this is somewhat dependent on the "Tor way of thinking" in the sense that if an entity has corrupted either an entry node or an exit node to a network then they in fact have administrative control over all middle nodes. In this case, TFNr **IS** in fact the node with administrative control over the traffic flow.



----------------

As detailed in the [whitepaper above](./writeup.pdf), all traffic from a source node to a destination node can be tagged as either "forward" or "reverse" in polarity based on the retrospection and request tendencies of the traffic at hand. This traffic, respectively tagged as either *FERR*, or *RERR* is inherently stateless and deformed in nature. This means that for each outbound request is at always fragmented to some extent and never expects a return stream.
