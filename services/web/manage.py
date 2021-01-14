
import os
import sys
import importlib

import panel as pn

import config as c

#side-stepping '-' with importlib
sys.path.append(c.REPO_NAME) 
app = importlib.import_module('..app', c.REPO_NAME + '.subpkg')

def serve():
    """

    """
    address = os.getenv("DOCKER_ADDRESS", default="localhost")

    pn.serve(
        panels={'app':app.servable},
        #port=c.PORT,
        port=5100,
        #dev=False,
        title=c.SITE_NAME,
        #num_procs=1,
        #websocket_origin=f'{address}:{str(c.PORT)}',
        #websocket_origin=f'{address}:{str(1337)}',
        websocket_origin='192.168.99.103:1337',
        #use_xheaders=True,
    )

if __name__ == "__main__":
    serve()
