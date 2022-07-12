from django.db import models

# Create your models here.

class User(models.Model):
    # 名字
    name = models.CharField(max_length=30)

    # 用户名
    username = models.CharField(max_length=30)

    # 密码
    password = models.CharField(max_length=30)

    # 昵称
    nickname = models.CharField(max_length=30)

    # 联系电话
    phoneNumber = models.CharField(max_length=30)

    # 邮箱
    email = models.CharField(max_length=30, default='')