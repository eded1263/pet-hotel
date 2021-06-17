"""PetHotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from core.views import home, cadastro_cliente, listagem_clientes, cadastro_pets, listagem_pets, tabela, \
    atualiza_cliente, exclui_cliente, planos, reserva, Registrar
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_principal'),
    path('reserva/', reserva, name='url_reserva'),
    path('accounts/registrar/', Registrar.as_view(), name='registrar'),
    path('planos', planos, name='url_planos'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cadastro_clientes/', cadastro_cliente, name='url_cadastro_clientes'),
    path('listagem_clientes/', listagem_clientes, name='url_listagem_clientes'),
    path('cadastro_pets/', cadastro_pets, name='url_cadastro_pets'),
    path('listagem_pets/', listagem_pets, name='url_listagem_pets'),
    path('tabela/', tabela, name='url_tabela'),
    path('atualiza_cliente/<int:id>/', atualiza_cliente, name="atualizar_cliente"),
    path('exclui_cliente/<int:id>/', exclui_cliente, name="excluir_cliente"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
