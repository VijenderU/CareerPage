from django.db import models

# Create your models here.
class JobDetails(models.Model):
    job_title = models.CharField(max_length = 100)
    job_exp_years = models.CharField(max_length = 100)
    salary = models.CharField(max_length = 50)
    emp_type = models.CharField(max_length = 100)
    job_location = models.CharField(max_length = 100)
    job_discription = models.CharField(max_length = 1000)
    job_skills = models.CharField(max_length = 100)