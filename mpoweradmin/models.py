from django.db import models

# Create your models here.
class Test(models.Model):
    MockTest_id=models.CharField(max_length=1000)
    CompanyName=models.CharField(max_length=1000)
    companylogo=models.ImageField()
    Role_desc=models.CharField(max_length=1000)
    Technology_tag=models.CharField(max_length=200)
    Question_1=models.CharField(max_length=1000)
    Answer_1=models.CharField(max_length=1000)
    Question_2=models.CharField(max_length=1000)
    Answer_2=models.CharField(max_length=1000)
    Question_3=models.CharField(max_length=1000)
    Answer_3=models.CharField(max_length=1000)
    Question_4=models.CharField(max_length=1000)
    Answer_4=models.CharField(max_length=1000)
    Question_5=models.CharField(max_length=1000)
    Answer_5=models.CharField(max_length=1000)





class Post_Seminars(models.Model):
    Seminar_title=models.CharField(max_length=200)
    Seminar_Date=models.DateField()
    Seminar_Time=models.TimeField() 
    Seminar_Venue=models.CharField(max_length=1000,  blank=True)
    Venue_location=models.CharField(max_length=200)
    Venue_offline_location=models.CharField(max_length=200, null=True, blank=True)
    Technology_tags=models.CharField(max_length=200)
    Host_Company=models.CharField(max_length=200)
    Links=models.CharField(max_length=200 , null=True , blank=True)
    venue_offline=models.CharField(max_length=1000 ,null=True ,blank=True)



    

    

   