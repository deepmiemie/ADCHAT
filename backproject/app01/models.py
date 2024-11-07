from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import uuid

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            self.delete(name)
        return name

# Create your models here.
class Customed_User(models.Model):
    username=models.CharField(max_length=12)
    password=models.CharField(max_length=20)

class GptUser(models.Model):
    username=models.CharField(max_length=12,unique=True)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=20,unique=True)
    country=models.CharField(max_length=12)
    phone=models.CharField(max_length=20)
    organization = models.CharField(max_length=20)

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         Token.objects.create(user=user)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, password, **extra_fields)

# class GptFormUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=12, unique=True)
#     email = models.EmailField(max_length=20, unique=True)
#     country = models.CharField(max_length=12)
#     phone = models.CharField(max_length=20)
#     organization = models.CharField(max_length=20)
#     is_staff = models.BooleanField(default=False)
    
#     objects = CustomUserManager()
#     USERNAME_FIELD = 'username'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        """
        解决通过 DRF 创建用户时 密码明文的问题
        """
        password = instance.password
        instance.set_password(password)
        instance.save()
        print(instance)
        Token.objects.create(user=instance)


class GptFormUser(AbstractUser):
    email = models.EmailField(max_length=20, unique=True)
    country = models.CharField(max_length=12)
    phone = models.CharField(max_length=20)
    organization = models.CharField(max_length=20)

    # is_superuser = models.BooleanField(verbose_name='超级管理员', default=0)

    class Meta:
        verbose_name_plural = verbose_name = '用户信息'

    def __unicode__(self):
        return self.username




def rename_file(instance, filename):
    extension = filename.split('.')[-1]
    new_name = f"{uuid.uuid4()}.{extension}"
    return f"uploadspdf/{new_name}"

class Upload(models.Model):
    file = models.FileField(upload_to='uploads/',storage=OverwriteStorage())

class UploadPdf(models.Model):
    file = models.FileField(upload_to=rename_file)

class UploadJson(models.Model):
    name = models.CharField(max_length=255)  # 文件名
    content = models.JSONField()  # 用于存储 JSON 内容的字段
    created_at = models.DateTimeField(auto_now_add=True)
