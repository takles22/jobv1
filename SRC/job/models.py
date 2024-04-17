from django.db import models



JOB_TYPE=[
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),
]



# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type= models.CharField(choices=JOB_TYPE, max_length= 20)
    Description = models.TextField (max_length=1000)
    published_at = models.DateField(auto_now= True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1000)
    Category = models.ForeignKey('Category',on_delete= models.CASCADE)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to='jobs_img/%Y/%m/%d/', blank=True)
    
    
    def __str__(self):
        return self.title
    
class Category (models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
   