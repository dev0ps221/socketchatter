from socket import *

DEFAULT_SERVER_MAX_CLI = 10

class chatterSocket:
    config = {}
    def isServer(self):
        return self.config('isserver') == True
        

    def instanciate(self):
        self.socket = socket(AF_INET,SOCK_STREAM)
        if self.isServer():
            self.config('maxCli',DEFAULT_SERVER_MAX_CLI)
            self.bind()

    def config(self,key,val=None):
        if key in self.config and val is None:
            return self[key]
        if val is not None:
            return self.config[key] = val

    def __init__(self,host=gethostname(),port='',isserver=0):
        self.config('host',host)
        self.config('port',port)
        self.config('isserver',isserver)



class chatterServer(chatterSocket):

    def bind(host=False,port:80):
        host = host if host else self.config('host')
        port = port if port else self.config('port')
        self.socket.bind((host,port))
    
    def listen(self):
        maxCli = self.config('maxCli')
        self.socket.listen(maxCli)

    def __init__(self,host=gethostname(),port=''):
        super().__init__(host,port,1)




class chatterClient(chatteServerSocketrSocket): 
    def __init__(self,host=gethostname(),port=''):
        super().__init__(host,port)