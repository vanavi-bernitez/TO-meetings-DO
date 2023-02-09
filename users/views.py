from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializer import UserModelSerializer, LoginModelSerializer
from rest_framework import status, response
from django.conf import settings
from django.contrib import auth
import jwt
from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework import generics 
# from .models import User

class RegisterAPI(GenericAPIView):
    
    serializer_class = UserModelSerializer
    
    def post(self,request):
        serializer = UserModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPI(GenericAPIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'register.html'
    serializer_class = LoginModelSerializer

    def post(self, request):
             
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = auth.authenticate(username=username, password=password)
        if user:
            auth_token = jwt.encode(
                {'username': user.username},
                settings.JWT_SECRET_KEY,
                algorithm="HS256"
            )

            serializer = LoginModelSerializer(user)

            data = {
                'user': serializer.data,
                'token': auth_token
            }
            # return render('register.html')
            return response.Response(data, status=status.HTTP_200_OK)

        # send response
        return response.Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class LogoutAPI(GenericAPIView):
    pass

# class UserList(generics.ListCreateAPIView):
#     serializer_class = UserModelSerializer
#     queryset = User.objects.all()

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = UserModelSerializer
#     queryset = User.objects.all()


