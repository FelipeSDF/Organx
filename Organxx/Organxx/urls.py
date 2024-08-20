from django.contrib import admin
import Organx.views as views
from django.urls import path

urlpatterns = [
    path('', views.home, name='land'),
    path('<page>', views.page, name='page'),
    path('consulta/pesquisa', views.consulta, name='consulta_pesquisa'),
    path('consulta/', views.editar, name='editar'),
    path('filtrar/', views.filtrar, name='filtrar'),
    path('admin/', admin.site.urls),
]
