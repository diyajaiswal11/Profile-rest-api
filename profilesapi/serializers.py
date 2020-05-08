from rest_framework import serializers 
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = UserProfile 
        fields= ['id','email','name','password']

        extra_kwargs = {
            'password': {
                'write_only':True,
                'style':{'input_type':'password'} #stars appear on typing not actual text
            }
        }   #not see password field on clicking on get 


    def create(self,validated_data):
        """Create and return a new user""" 

        user=UserProfile.objects.create_user(
            email=validated_data['email'], 
            name=validated_data['name'], 
            password=validated_data['password'] 
        ) 

        return user




class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name=serializers.CharField(max_length=10)


