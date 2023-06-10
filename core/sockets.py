from socket import *

class chatterSocket:

    def isServer(self):
        return self.isserver == True

    def instanciate(self):
        self.socket = socket(AF_INET,SOCK_STREAM)

    def __init__(self,ip='',port='',isserver=0):
        self.ip       =ip
        self.port     =port
        self.isserver =isserver

class chatterServer(chatterSocket):
    def __init__(self,ip='',port=''):
        super().__init__(ip='',port='',1)


class chatterClient(chatteServerSocketrSocket): 
    def __init__(self,ip='',port=''):
        super().__init__(ip='',port='')