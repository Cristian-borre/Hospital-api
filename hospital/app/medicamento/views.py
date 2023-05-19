from typing import Any
from django import http
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import MedicamentoModel
from django.http.response import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import MedicamentoSerializer

# Create your views here.

class MedicamentoView(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args ,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if id > 0:
            data = list(MedicamentoModel.objects.filter(numero=id).values())
            if len(data) > 0:
                data = data[0]
                datos = {'message':'Medicamento Listado', 'Medicamento':data}
            else:
                datos = {'message':'Medicamento no encontrado...'}
            return JsonResponse(datos)
        else:
            medico = list(MedicamentoModel.objects.filter(estado=1).values())
            if len(medico) > 0:
                datos = {'message':'Medicamentos Listados',"Medicamentos":medico}
            else:
                datos = {'message':'Medicamentos no encontrados....'}
            return JsonResponse(datos)
    
    def post(self, request):
        data = request.body
        if data != "":
            jd = json.loads(request.body)
            MedicamentoModel.objects.create(numero=jd['numero'], nombre=jd['nombre'], descripcion=jd['descripcion'])
            datos = {'message':'Medicamento creado'}
            return JsonResponse(datos)
        else:
            datos = {'message':'Medicamento no creado'}
            return JsonResponse(datos)

    def patch(self, request, id):
        try:
            medicamento = MedicamentoModel.objects.get(numero=id)
        except MedicamentoModel.DoesNotExist:
            return Response(status=400)

        serializer = MedicamentoSerializer(medicamento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        medicamento = list(MedicamentoModel.objects.filter(numero=id).values())
        if len(medicamento) > 0:
            medicamento = MedicamentoModel.objects.get(numero=id)
            medicamento.estado = False
            medicamento.save()
            datos = {'message':'Medicamento eliminado'}
        else:
            datos = {'message':'Medicamento no encontrado'}
        return JsonResponse(datos)