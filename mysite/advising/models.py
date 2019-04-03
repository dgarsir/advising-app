from django.db import models
from django.utils import timezone
from users.models import CustomUser

# Create your models here.

majors = (
    ('Computer Science', 'CS'),
    ('Computer Engineering', 'CE')
)

class Advising(models.Model):
    semester = models.CharField(max_length = 100)
    major = models.CharField(max_length = 100,choices=majors)
    QPA = models.CharField(max_length=100)
    GPA = models.CharField(max_length=100)
    currently_enrolled = models.TextField()
    completed_courses = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100, unique=True)
    #should this model have a status? i.e. submitted, pending approval, approved?
    status = models.IntegerField(default = 0)