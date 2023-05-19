from typing import Any
from django import http
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import CitaModel
from django.http.response import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CitaSerializer

# Create your views here.

class CitaView(APIView):

    def get(self, request, id = 0):
        if id > 0:
            data = list(CitaModel.objects.filter(numero=id).values())
            if len(data) > 0:
                data = data[0]
                datos = {'message':'Cita Listada', 'Cita':data}
            else:
                datos = {'message':'Cita no encontrada...'}
            return JsonResponse(datos)
        else:
            data = list(CitaModel.objects.filter(estado=1).values())
            if len(data) > 0:
                datos = {'message':'Citas Listadas',"Citas":data}
            else:
                datos = {'message':'Citas no encontradas....'}
            return JsonResponse(datos)
    
    def post(self, request):
        try:
            serializer = CitaSerializer(data = request.data,context={"request":request})
            if serializer.is_valid():
                model = CitaModel()
                model.numero = request.data['numero']
                model.fecha = request.data['fecha']
                model.hora = request.data['hora']
                model.paciente_id = request.data['paciente_id']
                model.medico_id = request.data['medico_id']
                model.consultorio_id = request.data['consultorio_id']
                model.observacion = request.data['observacion']
                model.save()
                datos = {'message':'Cita creada'}
                return Response(datos)
            else:
                datos = {'message':'Cita no creada'}
                return Response(datos)
        except Exception as e:
            datos = {'message':'Error '+ str(e)}
            Response(datos ,status=500)


    def patch(self, request, id):
        try:
            cita = CitaModel.objects.get(numero=id)
        except CitaModel.DoesNotExist:
            return Response(status=400)

        serializer = CitaSerializer(cita, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args ,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, id):
        data = list(CitaModel.objects.filter(numero=id).values())
        if len(data) > 0:
            data = CitaModel.objects.get(numero=id)
            data.estado = False
            data.save()
            datos = {'message':'Cita eliminada'}
        else:
            datos = {'message':'Cita no encontrada'}
        return JsonResponse(datos)