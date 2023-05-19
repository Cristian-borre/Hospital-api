from typing import Any
from django import http
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import PacienteModel
from django.http.response import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PacienteSerializer

# Create your views here.

class PacienteView(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args ,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if id > 0:
            data = list(PacienteModel.objects.filter(documento=id).values())
            if len(data) > 0:
                data = data[0]
                datos = {'message':'Paciente Listado', 'Paciente':data}
            else:
                datos = {'message':'Paciente no encontrado...'}
            return JsonResponse(datos)
        else:
            data = list(PacienteModel.objects.filter(estado=1).values())
            if len(data) > 0:
                datos = {'message':'Pacientes Listados',"Pacientes":data}
            else:
                datos = {'message':'Pacientes no encontrados....'}
            return JsonResponse(datos)
    
    def post(self, request):
        data = request.body
        if data != "":
            jd = json.loads(request.body)
            PacienteModel.objects.create(documento=jd['documento'], nombre=jd['nombre'], apellido=jd['apellido'], telefono=jd['telefono'],fecha_nacimiento=jd['fecha_nacimiento'],sexo=jd['sexo'])
            datos = {'message':'Paciente creado'}
            return JsonResponse(datos)
        else:
            datos = {'message':'Paciente no creado'}
            return JsonResponse(datos)

    def patch(self, request, id):
        try:
            paciente = PacienteModel.objects.get(documento=id)
        except PacienteModel.DoesNotExist:
            return Response(status=400)

        serializer = PacienteSerializer(paciente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        data = list(PacienteModel.objects.filter(documento=id).values())
        if len(data) > 0:
            data = PacienteModel.objects.get(documento=id)
            data.estado = False
            data.save()
            datos = {'message':'Paciente eliminado'}
        else:
            datos = {'message':'Paciente no encontrado'}
        return JsonResponse(datos)