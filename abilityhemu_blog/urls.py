from django.conf.urls import url
from .import views
from django.conf.urls.static import static

urlpatterns =[
    url(r'^$', views.post_list, name ='post_list'),
    url(r'^menu$',views.menu_show, name="menu_show"),
    url(r'^lipalater$', views.lipalater, name='lipalater'),
]