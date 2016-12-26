from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length=32) #指定2个字段，最大长度32，类型是char
    pwd = models.CharField(max_length=32)