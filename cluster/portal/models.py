from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

#Classes for registration
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_secret=models.CharField(max_length=50)
    course_open=models.BooleanField(default=True)

# Create your models here.
class MPI_Job(models.Model):
    job_name = models.CharField(max_length=50)
    job_auth = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    stdin_filepath = models.CharField(max_length=50, blank=True)
    job_time = models.DateTimeField('date posted',auto_now=True)
    job_cores= models.IntegerField(default=4)
    job_file = models.FileField(upload_to='uploads/')

class UploadJobForm(ModelForm):
    class Meta:
        model = MPI_Job
        fields = ['job_name', 'job_cores', 'job_file', 'stdin_filepath']
