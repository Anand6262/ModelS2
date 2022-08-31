from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True)  #THIS LINE IS WRITTEN TO PUT READ ONLY IN SINGLE FIELDS
    class Meta:
        model=Student
        fields=['id','name', 'roll', 'city']
        read_only_fields=['name', 'roll']  #THIS LINE IS WRITTEN TO PUT READ ONLY IN MULTIPLE FIELDS (Here we are applying read_only in 2 fields i.e name and roll)
        # extra_kwargs={'name' : {'read_only' : True}}  #THIS LINE IS WRITTEN TO PUT READ ONLY IN SINGLE FIELDS
        #NOTE->If we use (read_only_fields) witha column then we can not POST data in the same column!!. We can read only not able to write anything
    #Here we can also write this
    # class Meta:
    #     model=Student
    #     fields='__all__'  #To use all fields!!
    #     exclude=['roll']  #To use all fields except ['roll']