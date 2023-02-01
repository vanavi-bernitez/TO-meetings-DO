from rest_framework import serializers
from django.contrib.auth.models import User
# import jwt
from django.conf import settings

#from users.models import User

#User serializer for register 
class UserModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        min_length=2
    )
    first_name = serializers.CharField(
        min_length=2
    )
    last_name = serializers.CharField(
        min_length=2
    )
    email = serializers.EmailField(
        min_length=2
    )
    password = serializers.CharField(
        min_length=8, write_only=True, style={"input_type": "password"}
    )

    class Meta:
        # What i'm gonna show the user 
        model = User 
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        # fields = ('__all__') show ALL auth.user fields

    # template function
    def validate(self, attrs):
        email = attrs.get('email', None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('email already used')})
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class LoginModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        min_length=2
    )
    password = serializers.CharField(
        min_length=8, write_only=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ['username', 'password']
                                 