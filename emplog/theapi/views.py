from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .models import MobileUsers
from .serializers import UserSerializer


class UsersView(APIView):
    def get(self, request):
        users = MobileUsers.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class PostUsersView(APIView):

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditUsersView(APIView):

    def get_object(self, pk):
        try:
            return MobileUsers.objects.get(pk=pk)
        except MobileUsers.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        trip = self.get_object(pk)
        serializer = UserSerializer(trip)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        trip = self.get_object(pk=pk)
        serializer = UserSerializer(trip, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUsersView(APIView):

    def get_object(self, pk):
        try:
            return MobileUsers.objects.get(pk=pk)
        except MobileUsers.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
        
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)