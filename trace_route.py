#!/usr/bin/env python2.7
"""
    Simple traceroute replica

    @author: Justin Angra
    @created: Jan 3, 2016
    
    last modified: Jan 4, 2016
    
"""

import socket
import struct
import sys
import threading

def main(target_name):
    # resolve host name to ip
    try:
        target_addr = socket.gethostbyname(target_name)
    except socket.error as e: # invalid IP or host entered
        print " * * * Error: %d, %s" % (e.errno, e.strerror)
        sys.exit()
    
    target_port = 36789 # set target port to arbitrary registered port
    max_hops = 30
    ttl = 1 # set inital time-to-live for first-hop router
    is_target = False
    
    while True:
        # initialize loop variables  
        current_addr = None
        current_name = None
        current_host = None
        
        # establish UDP and ICMP sockets for sending and receiving respectively
        udp_send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        icmp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    
        udp_send_socket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl) # set TTL field 
        icmp_recv_socket.settimeout(0.5) # set timeout socket
        icmp_recv_socket.bind(('', target_port)) # bind to local interface 
        udp_send_socket.sendto('',(target_addr,target_port)) # send UDP packet
        
        try:
            data, addr = icmp_recv_socket.recvfrom(512) # recv ICMP packet
            current_addr = addr[0] # pull current IP address  

            icmp_header = data[20:28]  # pull ICMP header from packet 

            # check ICMP type and code fields for Dest. Port Unreachable
            icmp_type = struct.unpack("bbHHh", icmp_header)[0]    
            icmp_code = struct.unpack("bbHHh", icmp_header)[1]    
            
            if ((icmp_type,icmp_code) == (3,3)): # arrived at target host
                is_target = True 
            
            # resolve IP into host name
            try:
                current_name = socket.gethostbyaddr(current_addr)[0] 
            except socket.error as e:
                if isinstance(e,socket.herror): # no host name found
                    current_name = current_addr # set host name to IP address
                else:
                    print " * * * Error: %d, %s" % (e.errno, e.strerror) 
                    sys.exit()
            current_host = ("%s : %s") % (current_addr, current_name)      
        except IOError as e:
            if isinstance(e, socket.timeout): # no ICMP message received
                current_host = ("* * * Request timed out")
            elif isinstance(e, socket.error): # non timeout error raised
                print " * * * Error: %d, %s" % (e.errno, e.strerror)
                sys.exit() 
        finally:
            # close sockets under all circumstances
            udp_send_socket.close()
            icmp_recv_socket.close()
            
        print "%d\t%s" % (ttl, current_host)
        
        # exit loop when target host reached or ttl exceeds maximum allowed hops
        if (is_target) or (ttl > max_hops):
            break
        
        ttl += 1  # increment TTL for next-hop router
       

if __name__ == '__main__':
    # start threading on main
    thread_handler = threading.Thread(target=main,args=(str(sys.argv[1]),))
    thread_handler.start()
