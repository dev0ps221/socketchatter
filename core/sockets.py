from socket import *

class chatterSocket:

    def isServer(self):
        return self.isserver == True
        

    def instanciate(self):
        self.socket = socket(AF_INET,SOCK_STREAM)
        if self.isServer():
            self.bind()


    def __init__(self,ip='',port='',isserver=0):
        self.ip       =ip
        self.port     =port
        self.isserver =isserver



class chatterServer(chatterSocket):

    def bind(ip=False,port:80):
        ip = ip if ip else self.ip
        port = port if port else self.port
        self.socket.bind(ip,port)
        

    def __init__(self,ip='',port=''):
        super().__init__(ip='',port='',1)




class chatterClient(chatteServerSocketrSocket): 
    def __init__(self,ip='',port=''):
        super().__init__(ip='',port='')