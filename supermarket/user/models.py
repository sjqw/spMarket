from django.core import validators
from django.db import models


# Create your models here.
class User(models.Model):
    UserName = models.CharField(max_length=11,
                                verbose_name='用户名',
                                validators=[validators.MinLengthValidator(5)])

    pwd = models.CharField(max_length=20,
                           verbose_name='密码',
                           validators=[validators.MinLengthValidator(5)], )

    class Meta:
        db_table = 'userTable'
