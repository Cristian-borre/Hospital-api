from django.urls import path
from .views import MedicoView

urlpatterns = [
    path('medicos/', MedicoView.as_view(), name='Medicos_list'),
    path('medicos/<int:id>', MedicoView.as_view(), name='Medicos_process'),
    path('medicos/<int:id>/', MedicoView.as_view(), name='Medicos_process')
]