from django.urls import path
from django.conf.urls import url
from .import views, forms


urlpatterns = [
    path('ourdiary/', views.ourdiary, name = 'ourdiary'),
    path('<int:ourdiary_id>/',views.detail, name="detail"),
    path('like/', views.post_like, name="post_like"),
    #path('detail/<int:ourdiary_id>/comment', views.add_comment, name='add_comment'),
    url(r'^(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    
]