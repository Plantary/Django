from django.contrib import admin
from django.urls import path, include
import main.views
from ourdiary import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    path('', main.views.home, name="home"),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('ourdiary/', views.ourdiary, name="ourdiary"),
    path('ourdiary/<int:ourdiary_id>', views.detail, name="detail"),
    #path('like/<int:ourdiary_id>/', views.post_like, name="post_like"),
    path('like/', views.post_like, name="post_like"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

