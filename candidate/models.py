from django.db import models
from employer.models import User
# Create your models here.

class CandidateProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="candidate")
    prof_pic=models.ImageField(upload_to="candprof")
    resume=models.FileField(upload_to="cv",null=True)
    qualification=models.CharField(max_length=120)
    skills=models.CharField(max_length=120)
    exp=models.PositiveIntegerField(default=0)






