from django.urls import path
from .import views

urlpatterns = [
    path('ourdiary/', views.ourdiary, name = 'ourdiary'),
    path('<int:ourdiary_id>/',views.detail, name="detail"),
    path('like/', views.post_like, name="post_like")
    
]