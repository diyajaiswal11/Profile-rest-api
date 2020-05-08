from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
#from rest_framework import serializers
from profilesapi import serializers
from rest_framework import viewsets 
from .models import UserProfile, UserProfileManager
from profilesapi import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handling creating and updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=UserProfile.objects.all() 

    authentication_classes=[TokenAuthentication]  
    """tells the mechanism used to authenticate"""

    permission_classes=[permissions.UpdateOwnProfile]  
    """tells how user gets permission to do anything"""

    filter_backends=[filters.SearchFilter] 
    search_fields=['name','email']


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES 



class HelloViewSet(viewsets.ViewSet):
    """Test Api Viewset"""

    serializer_class=serializers.HelloSerializer

    def list(self,request):
        a_viewset=[
            'a','b','c',
        ] 
        return Response({'msg':'Hello','a_viewset':a_viewset })


    def create(self,request):
        """Create new hello msg"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}' 
            return Response({'message':message}) 
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

        
    def retrieve(self,request,pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method':'GET'}) 

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'}) 

    def partial_update(self,request,pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'}) 

    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'}) 


        







class HelloApiView(APIView):
    """Test API View"""

    serializer_class=serializers.HelloSerializer
 

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'Uses http methods',
            'like django view',
            'control to app logic',
            'mapped manually to urls',
        ] 

        return Response({'message':'Hello!','an_apiview':an_apiview})


    def post(self,request):
        """Create hello msg with name"""
        serializer=self.serializer_class(data=request.data) 
        if serializer.is_valid():
            name=serializer.validated_data.get('name')  
            message=f'Hello {name}'
            return Response({'message':message}) 
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'}) 

    def patch(self,request,pk=None):
        """Handle partial update of object"""
        return Response({'method':'PATCH'}) 

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})