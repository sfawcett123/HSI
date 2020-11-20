from socket import *
s=socket(AF_INET, SOCK_DGRAM)
s.bind(('',1234))
while(1):
    m=s.recvfrom(4096)
    print( 'len(m)='+str(len(m)) )
    print( 'len(m[0])='+str(len(m[0]))    ) 
    print( m[0] )

    print( 'len(m[1])='+str(len(m[1]))  )   
    print( m[1]   )
