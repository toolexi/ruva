import socket
from fastapi import FastAPI
from ruva.utils.APIUtils import GetMethods, PostMethods

app = FastAPI()


def find_free_port(preferred_port, max_attempts=5):
    port = preferred_port
    for _ in range(max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError("No free ports found in range")


app.include_router(GetMethods.router)
app.include_router(PostMethods.router)
