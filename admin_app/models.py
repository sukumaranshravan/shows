from django.db import models

# Create your models here.
class admin_tb(models.Model):
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class register_tb(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='pending')
    picture=models.FileField(default=0)

class category_tb(models.Model):
    category_name=models.CharField(max_length=20)    

class show_tb(models.Model):
    title=models.CharField(max_length=20)
    poster=models.FileField()
    user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    category=models.ForeignKey(category_tb,on_delete=models.CASCADE)
    genre=models.CharField(max_length=20)
    year=models.CharField(max_length=20)
    language=models.CharField(max_length=20)
    rating=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    story=models.CharField(max_length=20)