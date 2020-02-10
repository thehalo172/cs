from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Login.models import Example2

from Login.serializer import Example2Serializers


class CustonAuthToken(ObtainAuthToken):
    
    def post(self, request, * args, **kwars):
        serializer = self.serializer_class (data = request.data, 
                                            context = {
                                                    'request': request, 
                                                    }
                                            )
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

class Example2List2(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Example2.objects.filter(delete = False)
        serializer = Example2Serializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Example2Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Create your views here.
