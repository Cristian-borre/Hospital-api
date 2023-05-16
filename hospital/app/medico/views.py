from typing import Any
from django import http
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import MedicoModel
from django.http.response import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import MedicoSerializer

# Create your views here.

class MedicoView(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args ,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if id > 0:
            medico = list(MedicoModel.objects.filter(documento=id).values())
            if len(medico) > 0:
                medico = medico[0]
                datos = {'message':'Medico Listado', 'Medico':medico}
            else:
                datos = {'message':'Medico no encontrado...'}
            return JsonResponse(datos)
        else:
            medico = list(MedicoModel.objects.filter(estado=1).values())
            if len(medico) > 0:
                datos = {'message':'Medicos Listados',"Medicos":medico}
            else:
                datos = {'message':'Medicos no encontrados....'}
            return JsonResponse(datos)
    
    def post(self, request):
        data = request.body
        if data != "":
            jd = json.loads(request.body)
            MedicoModel.objects.create(documento=jd['documento'], nombre=jd['nombre'], apellido=jd['apellido'], telefono=jd['telefono'])
            datos = {'message':'Medico creado'}
            return JsonResponse(datos)
        else:
            datos = {'message':'Medico no creado'}
            return JsonResponse(datos)

    def patch(self, request, id):
        try:
            medico = MedicoModel.objects.get(documento=id)
        except MedicoModel.DoesNotExist:
            return Response(status=400)

        serializer = MedicoSerializer(medico, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        medico = list(MedicoModel.objects.filter(documento=id).values())
        if len(medico) > 0:
            medico = MedicoModel.objects.get(documento=id)
            medico.estado = False
            medico.save()
            datos = {'message':'Medico eliminado'}
        else:
            datos = {'message':'Medico no encontrado'}
        return JsonResponse(datos)