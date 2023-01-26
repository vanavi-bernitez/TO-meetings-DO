from rest_framework import generics
from .models import User
from .serializer import UserModelSerializer

class UserList(generics.ListCreateAPIView):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

    
    # def get(self):
        
    # def post():



class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

    # def get():

    # def patch():

    # def delete():




