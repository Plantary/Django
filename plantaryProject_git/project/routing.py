# mysite/routing.py
from channels.routing import ProtocolTypeRouter,URLRouter
import care.routing
from channels.auth import AuthMiddlewareStack
application = ProtocolTypeRouter({
    # (http->django views is added by default)
     'websocket': AuthMiddlewareStack(
        URLRouter(
            care.routing.websocket_urlpatterns
        )
    ),
})