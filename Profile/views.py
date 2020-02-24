from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Profile.models import Profile
from Profile.models import ModelCiudad
from Profile.models import ModelGenero
from Profile.models import ModelOcupacion
from Profile.models import ModelEstado
from Profile.models import ModelEstadoCivil

from Profile.serializer import ProfileSerializers
from Profile.serializer import CiudadSerializers
from Profile.serializer import GeneroSerializers
from Profile.serializer import OcupacionSerializers
from Profile.serializer import EstadoSerializers
from Profile.serializer import EstadoCivilSerializers



class ProfileList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Profile.objects.filter(delete = False)
        serializer = ProfileSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CiudadList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelCiudad.objects.filter(delete = False)
        serializer = CiudadSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GeneroList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelGenero.objects.filter(delete = False)
        serializer = GeneroSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelOcupacion.objects.filter(delete = False)
        serializer = OcupacionSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelEstado.objects.filter(delete = False)
        serializer = EstadoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoCivilList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelEstadoCivil.objects.filter(delete = False)
        serializer = EstadoCivilSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoCivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Create your views here.
