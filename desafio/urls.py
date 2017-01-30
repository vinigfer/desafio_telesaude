from django.conf.urls import patterns, url

from desafio import views

urlpatterns = [
    url(r'^$', views.solicitante_list, name='solicitante_list'),
    url(r'^new$', views.solicitante_create, name='solicitante_new'),
    url(r'^edit/(?P<pk>\d+)$', views.solicitante_update, name='solicitante_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.solicitante_delete, name='solicitante_delete'),
]