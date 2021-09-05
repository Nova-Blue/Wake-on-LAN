# Wake-on-LAN

A simple Wake-on-LAN client that can be used to wake devices on the local network.

## Usage

Usage is very simple:

```python
from WOL import WOLClient

#               Valid Local IP    Subnet Mask       MAC Address
wol = WOLClient('192.168.1.12', '255.255.255.0', '3C:54:61:88:C1:E4')
wol.wake()

```
It is important to note the the WOL protocol specifies that the packet be sent to the network's broadcast address. Supplying the IP and subnet mask in the above example is for the sole purpose of calculating the broadcast address only. This means that the supplied IP address does not need to belong to the target device, and can be any valid IP on the network. The provided MAC address will determine which device should process the message.



## Disclaimer

This code is fully functional, however, it was developed for learning purposes and may not offer the full functionality or error handling as may be seen in other software.