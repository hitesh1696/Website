from django.conf.urls import url
from . import views


app_name = 'Music'

urlpatterns = [
    #Music
    url(r'^$', views.index, name='index'),

    #Music/1/123
    url(r'^(?P<album_id>[0-9]+)$', views.detail, name='detail'),

    # Music/1/123/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.detail, name='favorite'),
]
