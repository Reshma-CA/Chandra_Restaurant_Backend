from django.shortcuts import render
from .models import *
from .serializers import *
# from rest_framework import viewsets
# from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.


class BlogAPI(APIView):
    
    def get(self,request):
        objs = blog.objects.all()
        serializer = blogSerializer(objs,many = True)
        return Response(serializer.data)
    
   
    
    def post(self,request):
        data = request.data
        serializer= blogSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        data = request.data
        serializer = blogSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def patch(self,request):
        data = request.data
        obj = blog.objects.get(id = data['id'] )
        serializer = blogSerializer(obj,data = data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self,request):
        data = request.data
        obj = blog.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'person deleted'})

class CategoryAPI(APIView):
    def get(self,request):
        objs = Category.objects.all()
        serializer = categorySerializer(objs,many = True)
        return Response(serializer.data)
    

class PopularPostAPI(APIView):
     def get(self,request):
        objs = blog.objects.filter(postlabel__iexact='POPULAR').order_by('-id')[0:4]
        serializer = blogSerializer(objs,many = True)
        return Response(serializer.data)
     



class DetailsAPI(APIView):
    def get(self, request, *args, **kwargs):
        blog_id = kwargs.get('id')  # Assuming the id is passed in the URL
        obj = blog.objects.get(id=blog_id)
        serializer = blogSerializer(obj)
        return Response(serializer.data)
    
    
    
class CategoryitemsAPI(APIView):
    def get(self, request, *args, **kwargs):
        blog_id = kwargs.get('id')  # Assuming the id is passed in the URL
        obj = blog.objects.filter(category=blog_id)  # Use the actual field, e.g., 'category__id'
        serializer = blogSerializer(obj, many=True)  # Assuming multiple objects can be returned
        return Response(serializer.data)
    

        
      