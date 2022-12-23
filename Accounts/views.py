from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import response
from .serializers import RegisterSerializer, UserSerializer
from knox.models import AuthToken

# Create your views here.

# Register API
class RegisterAPI (generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post (self, request, *args, **kwargs):
        serializer = self.get_serializer (data=request.data)
        serializer.is_valid (raise_exception=True)
        user = serializer.save()
        return response ({
            "user": UserSerializer (user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })