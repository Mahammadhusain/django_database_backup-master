from tokenize import Imagnumber
from django.contrib import admin
from .models import StudentModel,AddmissionModel
from django.contrib.contenttypes.models import ContentType
# Register your models here.


@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ("city","email", "roll", "name", "id")[::-1]


@admin.register(AddmissionModel)
class AddmissionModelAdmin(admin.ModelAdmin):
    list_display = ("status", "student","id")[::-1]


admin.site.register(ContentType)
