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
from .views import todos_os_protfólios
from .views import protfólio_de_desenvolvimento
from .views import protfólio_de_desing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Todos_os_Portfólios/', todos_os_protfólios),
    path('Portfólios_de_Design_Gráfico/', protfólio_de_desing),
    path('Portfólios_de_Desenvolvimento/', protfólio_de_desenvolvimento),
]
