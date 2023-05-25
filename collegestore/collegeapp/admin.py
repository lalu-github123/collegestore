from django.contrib import admin
from .models import StudentForm,Purposes,Department,Courses

# Register your models here.
admin.site.register(StudentForm)
admin.site.register(Purposes)
admin.site.register(Department)
admin.site.register(Courses)