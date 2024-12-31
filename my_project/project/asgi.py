"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
import sys
import os
import django
from multiprocessing import Process
# Import the serve function from grpc_server/server.py
try:
    from grpc_server.server import serve
except ImportError:
    serve = None

from django.core.asgi import get_asgi_application
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_asgi_application()


if __name__ == "__main__":
    grpc_process = Process(target=serve)
    grpc_process.start()
    try:
        from uvicorn import run
        run("my_project.asgi:application",
            host="0.0.0.0", port=8000, log_level="info")
    finally:
        grpc_process.terminate()
        grpc_process.join()
