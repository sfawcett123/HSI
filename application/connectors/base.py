import socket

class Listener():
     def __init__(self, address='' , port=1234 ):
         self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         self.socket.bind(( address , port ))
         self.socket.setblocking(0)
    
     def receive(self):
        try:
            data,address = self.socket.recvfrom(10000)
        except socket.error:
            pass
        else:
            print( data )
