
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Criar uma url para o usuario acessar 
    path('home/', include('empresa.urls'))
]
