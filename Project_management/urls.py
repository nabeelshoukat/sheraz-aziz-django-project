from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about_us, name='about-us'),
    path('our-services', views.our_services_page, name='our-services'),
    path('our-team', views.our_team, name='our-team'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('services/<int:id>', views.services_item, name='services'),
    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)