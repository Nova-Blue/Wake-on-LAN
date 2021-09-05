import socket
import ipaddress

class WOL:

    _PORT = 9
    _MAC_REPEAT_COUNT = 16
    _PAYLOAD_HEX_PREFIX = "FFFFFFFFFFFF"

    def __init__(self, ip_address, net_mask, mac_addr):
        # ip_address can be any valid address on the network
        # mac_addr specifies the target device
        self._ip_address = ip_address
        self._net_mask = net_mask
        self._mac_addr = mac_addr
        self._broadcast_addr = self._get_broadcast_addr()
        
    def wake(self, burst_size = 5):
        # attempts to wake the device on the local network
        # burst_size is how many WOL packets to send
        
        payload_bytes = self._create_payload()

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        for i in range(burst_size):
            sock.sendto(payload_bytes, (self._broadcast_addr, WOL._PORT))

        sock.close()


    def _get_broadcast_addr(self):
        # uses ip address and subnet mask to determine broadcast address
        
        interface = ipaddress.IPv4Interface(self._ip_address + "/" + self._net_mask)
        broadcast_addr = interface.network.broadcast_address
        return broadcast_addr.exploded
         

    def _create_payload(self):
        # a WOL packet's payload starts with a prefix followed by the
        # target device's MAC address a specified number of times
        
        payload_bytes = bytearray.fromhex(WOL._PAYLOAD_HEX_PREFIX)   
        mac_bytes = bytes.fromhex(self._mac_addr.replace(":", ""))
        
        for i in range(WOL._MAC_REPEAT_COUNT):
            payload_bytes.extend(mac_bytes)
                
        return payload_bytes
