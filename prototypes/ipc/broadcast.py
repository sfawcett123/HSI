from socket import *
s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.sendto( b'this is testing',('255.255.255.255',1234))
