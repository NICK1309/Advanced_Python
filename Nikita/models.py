from django.db import models

# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")

# class Teacher(models.Model):
#     teacherName = models.CharField(max_length=200)
#     teacherSubject = models.CharField(max_length=200)
#     teacherCollegeName = models.CharField(max_length=200)    
class Table(models.Model):
    name = models.CharField(max_length=200)
    add = models.CharField(max_length=200)
    email = models.CharField(max_length=200) 