from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    options=(
        ("employer","employer"),
        ("candidate","candidate")
    )
    role=models.CharField(max_length=120,choices=options,default="candidate")
    phone=models.CharField(max_length=12,null=True)





class Jobs(models.Model):
    job_title=models.CharField(max_length=150)
    company=models.ForeignKey(User,on_delete=models.CASCADE,related_name="company")
    location=models.CharField(max_length=120)
    salary=models.PositiveIntegerField(null=True)
    experience=models.PositiveIntegerField(default=0)
    created_date=models.DateField(auto_now_add=True)
    last_date=models.DateField(null=True)
    active_status=models.BooleanField(default=True)

    def __str__(self):
        return self.job_title

class CompanyProfile(models.Model):
    company_name=models.CharField(max_length=130)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="employer")
    logo=models.ImageField(upload_to="companyprofile",null=True)
    location=models.CharField(max_length=120)
    services=models.CharField(max_length=120)
    description=models.CharField(max_length=300)


class Application(models.Model):
    applicant=models.ForeignKey(User,on_delete=models.CASCADE,related_name="applicant")
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)
    options=(
        ("applied","applied"),
        ("accepted","accepted"),
        ("rejected","rejected"),
        ("pendind","pending"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="applied")
    date=models.DateTimeField(auto_now_add=True)






#on delete cascade means if u delete the user it will delete the prof also
#orm for creating a new job obj

#from employer.models import Jobs
#Jobs.objects.create(job_title="Testing",company_name="TCS",location="kochi",salary=24000,experince=3)

#fetching all records from database
# qs=Jobs.objects.all()
# qs

#controlz + enter for closing

# qs=Jobs.objects.filter(experince=3)
#  qs=Jobs.objects.filter(experince__gt=1)
  #here <,> is not work so __gt it means greater than
  # __lt less than
  #__lte less than equal to




#fetching a specific object
#qs=Jobs.objects.get(id=5)
# qs.experince=2
# qs.save()

#qs=Jobs.objects.get(id=2)
#qs.delete()
#create ,list ,detail ,update ,delete