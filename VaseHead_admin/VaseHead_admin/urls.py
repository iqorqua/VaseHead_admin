from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import ListView, DeleteView
from app.models import Good
import app.forms
import app.views
import threading

# Uncomment the next lines to enable the admin:
from VaseHead_admin.VaseHeadSite import Bot
from django.conf.urls import include
from django.contrib import admin
from app.views import BasicUploadView
admin.autodiscover()



urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^analytics$', app.views.analytics, name='analytics'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^settings', app.views.settings, name='settings'),
    url(r'^sendmass', app.views.sendmass, name='sendmass'),
    url(r'^clients', app.views.clients, name='clients'),
    url(r'^orders', app.views.orders, name='orders'),
    url(r'^coworking', app.views.coworking, name='coworking'),
    url(r'goods/(?P<pk>\d+)$', app.views.good, name='good'),
    url(r'^basic-upload/$', BasicUploadView.as_view(), name='basic_upload'),
    url(r'^basic-add-good/$', app.views.add_good, name='basic_add_good'),
    url(r'^analitycs_json/$', app.views.analitycs_json, name='analitycs_json'),
    url(r'^basic-delete-good/$', app.views.delete_good, name='basic_delete_good'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    url(r'^goods$', app.views.goods, name='goods'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls), 
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 