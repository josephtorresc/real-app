from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']
        verbose_name = 'User Type'
        verbose_name_plural = 'Users Type'
        db_table = 'user_type'

    def __str__(self):
        return self.name


class UserExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField()
    rut = models.PositiveIntegerField()
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'User Type'
        verbose_name_plural = 'Users Type'
        db_table = 'user_extend'

    def __str__(self):
        return self.user.username
