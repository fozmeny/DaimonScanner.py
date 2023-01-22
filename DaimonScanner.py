#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket

def daimon_scanner():
    open_ports = []
    ip_range = input("Taramak istediğiniz IP aralığını virgül ile ayırarak girin: ").split(',')
    port_range = input("Taramak istediğiniz port aralığını virgül ile ayırarak girin: ").split(',')
    port_range = list(map(int, port_range))
    for ip in ip_range:
        for port in port_range:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
    return open_ports

open_ports = daimon_scanner()
print("Açık portlar: ", open_ports)


# In[ ]:




