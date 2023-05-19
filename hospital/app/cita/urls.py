from django.urls import path
from .views import CitaView

urlpatterns = [
    path('citas/', CitaView.as_view(), name='citas_list'),
    path('citas/<int:id>', CitaView.as_view(), name='citas_process'),
    path('citas/<int:id>/', CitaView.as_view(), name='citas_process')
]