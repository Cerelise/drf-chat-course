from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            return ValueError("超级用户的is_staff属性必须为True")

        if extra_fields.get("is_superuser") is not True:
            return ValueError("超级用户的is_superuser属性必须为True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=512)
    phone = models.CharField(blank=True, max_length=20)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    # 指定使用CustomUserManager进行用户管理
    objects = CustomUserManager()
    # 将用户验证时使用字段修改为email
    USERNAME_FIELD = "email"
    # 设置在创建用户账号时用户需要提供的字段
    REQUIRED_FIELDS = ["username"]

    # 设置模型在管理界面中的显示名称。
    class Meta:
        verbose_name = "Account"

    def __str__(self):
        return self.username