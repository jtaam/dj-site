from django.conf.urls import url
from .views import posts_list, posts_detail, posts_create, posts_update, posts_delete

urlpatterns = [
    url(r'^$', posts_list),
    url(r'^create/$', posts_create),
    url(r'^(?P<slug>[\w-]+)/update/$', posts_update),
    url(r'^(?P<slug>[\w-]+)/delete/$', posts_delete),
    url(r'^(?P<slug>[\w-]+)/$', posts_detail),
]
