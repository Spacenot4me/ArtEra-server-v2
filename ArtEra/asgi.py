import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ArtEra.settings')
django_asgi_app = get_asgi_application()


# its important to make all other imports below this comment
import socketio
from chat.sockets import sio


application = socketio.ASGIApp(sio, django_asgi_app)
