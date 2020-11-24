import socket
import logging
import application.config as CONFIG

class Listener():
     def __init__(self, address='' , port=1234 ):
         self._data = None
         self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         self.socket.bind(( address , port ))
         self.socket.setblocking(0)
         logging.info( "UDP listening on {address} {port}".format( address=address, port=port )  )
    
     def receive(self):
        try:
            data,address = self.socket.recvfrom(10000)
        except socket.error:
            pass
        else:
            logging.info( "Message Recieved from {address}".format( address=address )  )
            logging.debug( data )
            return data

     @property
     def data(self):
         return self._data

