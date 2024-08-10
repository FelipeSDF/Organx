from django.contrib import admin
import Organx.views as views
from django.urls import path

urlpatterns = [
    path('', views.home, name='land'),
    path('<page>', views.page, name='page'),
    path('add/', views.add_page, name='add'),
    path('admin/', admin.site.urls),
]
