from cProfile import label
from email.policy import default
from unittest import mock
from rest_framework import serializers
from .models import StudentModel
from datetime import datetime





class StudentSerializer(serializers.ModelSerializer):
    s_cate = serializers.IntegerField(source ='roll')
    class Meta:
        model = StudentModel
        fields = ["id", "name", "roll", "email", "s_cate"]

