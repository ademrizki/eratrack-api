from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class EmployeeManager(BaseUserManager):
    """Manager for Employee profiles"""

    def create_user(self, username, name, role, team, image, password=None):
        """Create a new user profile"""
        if not username:
            raise ValueError('User must have username')

        user = self.model(username=username, name=name,
                          role=role, team=team, image=image)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, name, role, team, image, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(username, name, role, team, image, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Employee(AbstractBaseUser, PermissionsMixin):
    """Employee Model"""

    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    role = models.CharField(max_length=5)
    team = models.CharField(max_length=5)
    image = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = EmployeeManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'role', 'team', 'image']

    def __str__(self):
        return self.username


class Visit(models.Model):
    """Visit Model"""

    name = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    latitude = models.FloatField(max_length=255)
    longitude = models.CharField(max_length=255)
    user_image = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.date
