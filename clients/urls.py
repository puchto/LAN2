from django.conf.urls import url, include
from clients import views

urlpatterns = [
    url(r'^$', views.main_view, name='main_view'),
    url(r'^client_list/$', views.clients_list, name='clients_list'),
    url(r'^client/info/(?P<pk>[0-9]+)/$', views.client_info, name='client_info'),
    url(r'^client/info_fw/(?P<pk>[0-9]+)/$', views.client_info_fw, name='client_info_fw'),
    url(r'^client/edit/(?P<pk>[0-9]+)/$', views.client_edit, name='client_edit'),
    url(r'^client/edit_Client_fw/(?P<pk>[0-9]+)/$', views.client_edit_Client_fw, name='client_edit_Client_fw'),
    url(r'^clients_search/$', views.clients_search, name='clients_search'),
    url(r'^clients_arp/$', views.clients_arp, name='clients_arp'),
    url(r'^client_found/$', views.clients_found, name='clients_found')
]