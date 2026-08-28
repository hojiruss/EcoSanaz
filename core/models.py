import datetime

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    accessibility = models.IntegerField(default=0)
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'users'
        verbose_name = 'users'
        ordering = ['username']
        unique_together = (('username', 'email'),)

class UserInformations(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    current_assets = models.JSONField(default=dict)
    risk_group = models.ForeignKey('risk_groups', on_delete=models.CASCADE)
    risk_score = models.IntegerField(default=1)
    joining_date = models.DateField(default=datetime.date.today)
    subscription_end_date = models.DateField(default=0)
    package_assigned = models.ForeignKey('Packages', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    class Meta:
        db_table = 'user_informations'