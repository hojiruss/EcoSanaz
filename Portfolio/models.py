from django.db import models

# Create your models here.
class AssetsGroup(models.Model):
    asset_group_name = models.CharField(max_length=100,unique=True)
    asset_group_description = models.TextField(default="")
