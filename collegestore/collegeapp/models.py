from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.department)

class Courses(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    course = models.CharField(max_length=200)
    def __str__(self):
        return self.course

class Purposes(models.Model):
    purpose = models.CharField(max_length=200)
    def __str__(self):
        return self.purpose

class StudentForm(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(default="1996-09-3")
    s_gender=(('male',"Male"),('female',"Female"),('trans',"Trans"))
    gender = models.CharField(max_length=25,choices=s_gender)
    phone_number = models.IntegerField()
    mail = models.EmailField(max_length=100)
    address = models.TextField()
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True,null=True)
    course = models.ForeignKey(Courses,on_delete=models.SET_NULL,blank=True,null=True)
    purpose = models.ForeignKey(Purposes,on_delete=models.SET_NULL,blank=True,null=True)
    materials_provide_1 = models.BooleanField("Debit Note",default=False)
    materials_provide_2 = models.BooleanField("Pen", default=False)
    materials_provide_3 = models.BooleanField("Exam Papers", default=False)

    def __str__(self):
        return '{}'.format(self.name)




