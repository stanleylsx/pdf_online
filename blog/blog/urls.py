"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import include
from django.views.static import serve
from blog.settings import MEDIA_ROOT
from blog.settings import STATIC_ROOT
from django.urls import path, re_path

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('show_articles/', include('show_articles.urls', namespace='show_articles')),
    re_path(r'^upload/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
]