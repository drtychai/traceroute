# traceroute

Simple multithreaded traceroute replica.

## Overview

The trace_route.py utility prints a list of each NEXT_HOP router from localhost to target IP address or Host.

## Example

To trace the path from localhost to the target host, simply run the trace_route.py file with the target host as an argument. As shown below, we will trace the path from localhost to www.ust.hk, the web server at Hong Kong University of Science and Technology.

Note: Due to the use of an ICMP socket, the scipt requires superuser privilige. 

```bash
$ sudo python trace_route.py www.ust.hk
1       192.168.1.1 : 192.168.1.1
2       23.28.194.1 : d28-23-1-194.dim.wideopenwest.com
3       76.73.172.181 : dynamic-76-73-172-181.knology.net
4       24.236.73.13 : user-24-236-73-13.knology.net
5       75.76.35.14 : dynamic-75-76-35-14.knology.net
6       75.76.35.13 : dynamic-75-76-35-13.knology.net
7       77.67.77.213 : xe-0-0-3.was14.ip4.gtt.net
8       141.136.110.169 : xe-5-0-0.tyo10.ip4.gtt.net
9       89.149.186.66 : xe-2-0-0.hkg11.ip4.gtt.net
10      * * * Request timed out
11      183.182.80.222 : wharf-gw.ip4.gtt.net
12      * * * Request timed out
13      115.160.187.110 : 115.160.187.110
14      203.188.117.130 : 203.188.117.130
15      202.14.80.153 : 202.14.80.153
16      * * * Request timed out
17      143.89.14.2 : www.ust.hk
```

Whenever a ```* * * Request timed out``` is printed, the program either did not receive an ICMP reply from a router or the route is blocked by a firewall. Below is an exmaple of a trace to Google's Public DNS server, 8.8.8.8. The route from my localhost is blocked by a firewall. 

```bash
$ sudo python trace_route.py 8.8.8.8
1	192.168.1.1 : 192.168.1.1
2	23.28.194.1 : d28-23-1-194.dim.wideopenwest.com
3	76.73.172.181 : dynamic-76-73-172-181.knology.net
4	76.73.167.65 : 76-73-167-65.knology.net
5	76.73.166.126 : 76-73-166-126.knology.net
6	76.73.166.125 : 76-73-166-125.knology.net
7	69.73.0.139 : static-69-73-0-139.knology.net
8	75.76.35.10 : dynamic-75-76-35-10.knology.net
9	75.76.35.6 : dynamic-75-76-35-6.knology.net
10	* * * Request timed out
11	* * * Request timed out
12	* * * Request timed out
13	* * * Request timed out
14	* * * Request timed out
15	* * * Request timed out
16	* * * Request timed out
17	* * * Request timed out
18	* * * Request timed out
19	* * * Request timed out
20	* * * Request timed out
21	* * * Request timed out
22	* * * Request timed out
23	* * * Request timed out
24	* * * Request timed out
25	* * * Request timed out
26	* * * Request timed out
27	* * * Request timed out
28	* * * Request timed out
29	* * * Request timed out
30	* * * Request timed out
31	* * * Request timed out
```

We see that our program stops receiving ICMP replys and attempts to querry the next-hop router in the path to 8.8.8.8. It continues this until a maximum hop length is reached. 


## Getting Started

You can download this program and begin tracing immediately with python 2.7 as shown above. If, like me, you prefer a shorter command, an alias can be made for *nix systems by adding ```alias trace_route="sudo /path/to/file.py"``` to your ```~/.bash_profile``` or ```~/.bashrc```. With this addition, you can simply run the program as ```trace_route hostname```, where ```hostname``` is replaced by a domain name or IP address. 


## License

Please see https://en.wikipedia.org/wiki/Traceroute

You are hereby granted a non-exclusive, worldwide, royalty-free license to use, copy, modify, and distribute this software in source code or binary form.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
