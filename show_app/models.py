from django.db import models

# Create your models here.
class watchlist_tb(models.Model):
    title=models.CharField(max_length=20)
    rating=models.CharField(max_length=20,default=0)
    user_id=models.ForeignKey('admin_app.register_tb',on_delete=models.CASCADE)
