from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

# class Teacher(models.Model):
#     teacherName = models.CharField(max_length=200)
#     teacherSubject = models.CharField(max_length=200)
#     teacherCollegeName = models.CharField(max_length=200)    
# class Teacher(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField()(max_length=200)
#    # tsubname = models.CharField(max_length=200) 

    def __str__(self):
        return self.question_text