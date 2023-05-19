from django.urls import path
from .views import MedicamentoView

urlpatterns = [
    path('medicamentos/', MedicamentoView.as_view(), name='Medicamentos_list'),
    path('medicamentos/<int:id>', MedicamentoView.as_view(), name='Medicamentos_process'),
    path('medicamentos/<int:id>/', MedicamentoView.as_view(), name='Medicamentos_process')
]