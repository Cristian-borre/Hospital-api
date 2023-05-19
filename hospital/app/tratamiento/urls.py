from django.urls import path
from .views import TratamientoView

urlpatterns = [
    path('tratamientos/', TratamientoView.as_view(), name='Tratamientos_list'),
    path('tratamientos/<int:id>', TratamientoView.as_view(), name='Tratamientos_process'),
    path('tratamientos/<int:id>/', TratamientoView.as_view(), name='Tratamientos_process')
]