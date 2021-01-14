
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
        port=c.PORT,
        dev=False,
        title=c.SITE_NAME,
        num_procs=1,
        websocket_origin=f'{address}:{str(c.PORT)}',
        show=True
    )

if __name__ == "__main__":
    serve()
