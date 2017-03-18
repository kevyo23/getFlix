from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.queryIndexView.as_view(), name='index'),
    #url(r'^profile/$', views.profile, name='profile'),

]
