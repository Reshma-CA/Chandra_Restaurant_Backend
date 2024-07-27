from rest_framework import serializers
from .models import *

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model= blog
        fields = '__all__' 


    
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = '__all__' 