from django.urls import path
# from .views import UserList, UserDetail
from .views import RegisterAPI, LoginAPI


urlpatterns = [
    path('login/', LoginAPI.as_view(), name = 'login'),
    path('register/', RegisterAPI.as_view(), name = 'register')
    
    # path('item/<int:pk>/', UserDetail.as_view()),                                                                 
]

