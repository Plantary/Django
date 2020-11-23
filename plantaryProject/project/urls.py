from django.conf.urls import url,include
from django.contrib import admin
#from ourdiary import views
import Main.views
import ourdiary.views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
#]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    path('account/', include('account.urls')),
    path('ourdiary/', include('ourdiary.urls')),
    path('', Main.views.home, name = 'home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
