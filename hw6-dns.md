HW6:: DNS lookup
========================

_Author_: Shreyas

_Email_ : shreyas@ischool.berkeley.edu

1. What series of IPs would a recursive DNS server use to find the address of m.yelp.com?

    - command
```
$ traceroute m.yelp.com
```

| IP | Remarks | 
|:---|:--------|
| 10.142.136.1 | Local Area Network IP Gateway |
| 128.32.0.86, 128.32.0.66 | Arpa Domain Name pointer -- Berkeley's DNS local caching|
| 137.164.50.16, 137.164.22.25, 137.164.47.174, 198.32.251.154 | CENIC links |
| 198.32.251.154, 64.125.31.66, 64.125.30.126, 64.125.26.61, 209.66.115.62 | Above.net that provides routing services and fiber optics |
| 199.255.189.234 | `m.sfo1.yelp.com` which refers to m.yelp.com  |

- overall output

```
traceroute: Warning: m.yelp.com has multiple addresses; using 199.255.189.234
traceroute to m.yelp.com (199.255.189.234), 64 hops max, 52 byte packets
 1  xe-1-2-0-502.inr-341-mulcev.1918.berkeley.edu (10.142.136.1)  1.450 ms  1.454 ms  1.613 ms
 2  t5-5.inr-202-reccev.berkeley.edu (128.32.0.86)  1.644 ms  1.454 ms  1.380 ms
 3  xe-5-1-0.inr-001-sut.berkeley.edu (128.32.0.66)  7.117 ms  7.666 ms  2.021 ms
 4  dc-sfo-agg-1--ucb-10ge.cenic.net (137.164.50.16)  2.080 ms  2.467 ms  2.050 ms
 5  oak-agg2--sfo-agg1-10g.cenic.net (137.164.22.25)  6.507 ms  4.910 ms  7.621 ms
 6  dc-paix-px1--oak-core1-ge.cenic.net (137.164.47.174)  4.365 ms  4.282 ms  4.231 ms
 7  abovenet--paix-px1.cenic.net (198.32.251.154)  4.197 ms  4.468 ms  4.875 ms
 8  xe-3-0-0.cr1.sjc2.us.above.net (64.125.31.66)  5.051 ms  5.050 ms  5.053 ms
 9  xe-0-0-0.cr2.sjc2.us.above.net (64.125.30.126)  5.172 ms  5.453 ms  5.733 ms
10  xe-0-1-0.mpr4.sfo7.us.above.net (64.125.26.61)  8.413 ms  22.002 ms  6.468 ms
11  209.66.115.62.t01325-02.above.net (209.66.115.62)  6.276 ms  6.530 ms  6.454 ms
12  m.sfo1.yelp.com (199.255.189.234)  6.444 ms  6.371 ms  6.509 ms
```

2. What are the IP addresses of m.yelp.com?

- command

```
$ host m.yelp.com
```

```
m.yelp.com has address 199.255.189.234
m.yelp.com has address 198.51.132.34
m.yelp.com has address 199.255.189.34
m.yelp.com has address 198.51.132.234
```

3. Do IP packets leave the Berkeley network when traveling to amplab.cs.berkeley.edu? Include the command and output.

_No_

```
$ traceroute amplab.cs.berkeley.edu
```

```
traceroute to www-research2.cs.berkeley.edu (128.32.37.248), 64 hops max, 52 byte packets
 1  xe-1-2-0-502.inr-341-mulcev.1918.berkeley.edu (10.142.136.1)  1.887 ms  1.268 ms  1.350 ms
 2  t5-5.inr-202-reccev.berkeley.edu (128.32.0.86)  1.389 ms  1.373 ms  1.344 ms
 3  reccev-eecs-br-10ge.eecs.berkeley.edu (128.32.255.58)  2.398 ms  1.848 ms  2.004 ms
 4  soda-10g-edge.eecs.berkeley.edu (169.229.59.242)  2.341 ms  5.435 ms  2.258 ms
 5  www-research2.cs.berkeley.edu (128.32.37.248)  1.804 ms !Z  1.642 ms !Z  1.641 ms !Z
```
