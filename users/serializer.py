from rest_framework import serializers
from users.models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        # fields = ['id', 'username', 'first_name', 'email']   HyperlinkedModelSerializer