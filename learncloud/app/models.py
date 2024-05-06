from django.db import models


# Create your models here.
class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=128)
