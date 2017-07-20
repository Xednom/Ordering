from django.conf.urls import include, url
from django.contrib import admin
from systems import views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^ordering/', include('ordering.urls', namespace='ordering')),
]
