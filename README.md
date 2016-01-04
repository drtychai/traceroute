# traceroute

Simple multithreaded traceroute replica.

## Overview

The tracer.py utility prints a list of each NEXT_HOP router from localhost to target IP address or Host.

## Example

To trace the path from your local host to the target host, simply run the trace_route.py file with the target host as an argument. As shown below, we will trace the path from our local host to www.ust.hk, the web server at Hong Kong University of Science and Technology.

Note: Due to the use of an ICMP socket, the scipt requires superuser privilige. 

```bash
$sudo python trace_route.py www.ust.hk
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

## Getting Started




## License

Please see https://en.wikipedia.org/wiki/Traceroute

You are hereby granted a non-exclusive, worldwide, royalty-free license to use, copy, modify, and distribute this software in source code or binary form.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
