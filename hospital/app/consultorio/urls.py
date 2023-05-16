from django.urls import path
from .views import ConsultorioView

urlpatterns = [
    path('consultorios/', ConsultorioView.as_view(), name='Consultorio_list'),
    path('consultorios/<int:id>', ConsultorioView.as_view(), name='Consultorio_process'),
    path('consultorios/<int:id>/', ConsultorioView.as_view(), name='Consultorio_process')
]