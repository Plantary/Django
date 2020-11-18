from django.urls import path
from .import views

urlpatterns = [
    path('ourdiary/', views.ourdiary, name = 'ourdiary'),
    path('<int:ourdiary_id>/',views.detail, name="detail"),
    path('like/', views.post_like, name="post_like"),
    path('new/', views.new, name = 'new'),
    path('create/',views.create, name = 'create'),
    path('mylist/',views.mylist, name = 'mylist'),
    path('<int:ourdiary_id>/update',views.update, name = 'update'),
    path('<int:ourdiary_id>/delete',views.delete, name = 'delete'),
    
]