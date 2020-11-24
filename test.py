from socket import *
import time

s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.sendto( b'{ "heading": 0 }',('255.255.255.255',1234))
time.sleep(3)
s.sendto( b'{ "heading": 90 }',('255.255.255.255',1234))
time.sleep(3)
s.sendto( b'{ "heading": 180 }',('255.255.255.255',1234))
time.sleep(3)
s.sendto( b'{ "heading": 270 }',('255.255.255.255',1234))
time.sleep(3)
s.sendto( b'{ "heading": 360 }',('255.255.255.255',1234))
