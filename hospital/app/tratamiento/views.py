from typing import Any
from django import http
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import TratamientoModel
from django.http.response import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import TratamientoSerializer

# Create your views here.

class TratamientoView(APIView):

    def get(self, request, id = 0):
        if id > 0:
            data = list(TratamientoModel.objects.filter(numero=id).values())
            if len(data) > 0:
                data = data[0]
                datos = {'message':'Tratamiento Listado', 'Tratamiento':data}
            else:
                datos = {'message':'Tratamiento no encontrado...'}
            return JsonResponse(datos)
        else:
            data = list(TratamientoModel.objects.filter(estado=1).values())
            if len(data) > 0:
                datos = {'message':'Tratamientos Listados',"Tratamientos":data}
            else:
                datos = {'message':'Tratamientos no encontrados....'}
            return JsonResponse(datos)
    
    def post(self, request):
        try:
            serializer = TratamientoSerializer(data = request.data, context = {"request":request})
            if serializer.is_valid():
                model = TratamientoModel()
                model.numero = request.data['numero']
                model.paciente_id = request.data['paciente_id']
                model.fecha_asignada = request.data['fecha_asignada']
                model.medicamento_id = request.data['medicamento_id']
                model.fecha_inicio = request.data['fecha_inicio']
                model.fecha_fin = request.data['fecha_fin']
                model.observaciones = request.data['observaciones']
                model.save()
                datos = {'message':'Tratamiento creado'}
                return Response(datos)
            else:
                datos = {'message':'Tratamiento no creado'}
                return Response(datos)
        except Exception as e:
            datos = {'message':'Error '+ str(e)}
            Response(datos ,status=500)

    def patch(self, request, id):
        try:
            tratamiento = TratamientoModel.objects.get(numero=id)
        except TratamientoModel.DoesNotExist:
            return Response(status=400)

        serializer = TratamientoSerializer(tratamiento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args ,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, id):
        data = list(TratamientoModel.objects.filter(numero=id).values())
        if len(data) > 0:
            data = TratamientoModel.objects.get(numero=id)
            data.estado = False
            data.save()
            datos = {'message':'Tratamiento eliminado'}
        else:
            datos = {'message':'Tratamiento no encontrado'}
        return JsonResponse(datos)