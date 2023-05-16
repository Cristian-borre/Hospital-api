from typing import Any
from django import http
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import ConsultorioModel
from django.http.response import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ConsultorioSerializer

# Create your views here.

class ConsultorioView(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args ,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if id > 0:
            consult = list(ConsultorioModel.objects.filter(numero=id).values())
            if len(consult) > 0:
                consult = consult[0]
                datos = {'message':'Consultorio Listado', 'Consultorio':consult}
            else:
                datos = {'message':'Consultorio no encontrado...'}
            return JsonResponse(datos)
        else:
            consult = list(ConsultorioModel.objects.filter(estado=1).values())
            if len(consult) > 0:
                datos = {'message':'Consultorios Listados',"Consultorios":consult}
            else:
                datos = {'message':'Consultorios no encontrados....'}
            return JsonResponse(datos)
    
    def post(self, request):
        data = request.body
        if data != "":
            jd = json.loads(request.body)
            ConsultorioModel.objects.create(numero=jd['numero'], nombre=jd['nombre'])
            datos = {'message':'Consultorio creado'}
            return JsonResponse(datos)
        else:
            datos = {'message':'Consultorio no creado'}
            return JsonResponse(datos)

    def patch(self, request, id):
        try:
            consult = ConsultorioModel.objects.get(numero=id)
        except ConsultorioModel.DoesNotExist:
            return Response(status=400)

        serializer = ConsultorioSerializer(consult, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        consult = list(ConsultorioModel.objects.filter(numero=id).values())
        if len(consult) > 0:
            consult = ConsultorioModel.objects.get(numero=id)
            consult.estado = False
            consult.save()
            datos = {'message':'Consultorio eliminado'}
        else:
            datos = {'message':'Consultorio no encontrado'}
        return JsonResponse(datos)