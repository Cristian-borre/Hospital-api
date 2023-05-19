from django.urls import path
from .views import PacienteView

urlpatterns = [
    path('pacientes/', PacienteView.as_view(), name='Pacientes_list'),
    path('pacientes/<int:id>', PacienteView.as_view(), name='Pacientes_process'),
    path('pacientes/<int:id>/', PacienteView.as_view(), name='Pacientes_process')
]