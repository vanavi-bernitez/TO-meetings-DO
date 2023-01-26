from django.urls import path
from .views import UserList, UserDetail
urlpatterns = [
    path('item/', UserList.as_view()),
    path('item/<int:pk>/', UserDetail.as_view()),                                                                    
]