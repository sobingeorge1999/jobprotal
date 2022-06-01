from django.db import models

# Create your models here.

class Jobs(models.Model):
    job_title=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    location=models.CharField(max_length=120)
    salary=models.PositiveIntegerField(null=True)
    experience=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.job_title


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