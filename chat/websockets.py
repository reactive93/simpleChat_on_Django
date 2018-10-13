from tornado import websocket,web,ioloop
from multiprocessing import Process
import json
clients=[] #type:list[websocket.WebSocketHandler]

class WebSocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in clients:
            clients.append(self)
            print('connectet')

    def on_message(self, message):

        for client in clients:
            if client is not self:
                client.write_message(message)
        print(message)


    def on_close(self):
        clients.remove(self)
        print('remaining client: '+ str(len(clients)))

def run():

    app = web.Application(handlers=[
        (r'/ws',WebSocketHandler),
    ])
    app.listen(8888)
    ioloop.IOLoop.instance().start()

def run_tornado():

    process = Process(target=run)
    process.daemon=1
    process.start()
    print('process torando started')