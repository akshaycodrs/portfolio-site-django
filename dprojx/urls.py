from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
# from django.apps import views as uv


urlpatterns = [
    path('admin/', admin.site.urls),
    url('',include('dappx.urls')),
]