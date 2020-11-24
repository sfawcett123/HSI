import application.connectors.base as base
import json
import logging

class Broadcast( base.Listener )  :
    def __init__(self):
        super().__init__()
        logging.info( "Broadcast Listener Started"  )
        self._data = json.loads( "{}" )

    def receive( self ):
        data =  super().receive()
        if data:
            self._data = json.loads( data )
            logging.debug( "Json data {json}".format( json=type(self._data) )  )
            return  self._data 
