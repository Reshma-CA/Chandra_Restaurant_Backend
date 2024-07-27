from django.urls import path,include
from blog_api.views import *

urlpatterns = [
    path('blogs/', BlogAPI.as_view()),
    path('category/', CategoryAPI.as_view()),
    path('popular/',PopularPostAPI.as_view()),
    path('details/<int:id>/',DetailsAPI.as_view()), 
    path('items/<int:id>/',CategoryitemsAPI.as_view()),

    
]