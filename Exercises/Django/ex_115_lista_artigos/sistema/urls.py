"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import Todos_os_artigos
from .views import Artigos_tecnologia
from .views import Artigos_Saúde


urlpatterns = [
    path('admin/', admin.site.urls),
    path('artigos_tecnologia/', Artigos_tecnologia),
    path('artigos_saude/', Artigos_Saúde),
    path('todos_os_artigos/', Todos_os_artigos)
]
