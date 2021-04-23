from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, is_startup_founder, password=None):
        if not email:
            return ValueError("Users must have an email")
        if not username:
            return ValueError("Users must have an username")
        if not first_name or not last_name:
            return ValueError("Users must have a name")
        
        user = self.model(
            email = self.normalize_email(email),
            username=username,
            first_name = first_name,
            last_name = last_name,
            is_startup_founder = is_startup_founder
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, is_startup_founder, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            first_name = first_name,
            last_name = last_name,
            is_startup_founder=is_startup_founder,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_startup_founder = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'is_startup_founder']

    objects = MyUserManager()

    def __str__(self):
        return self.username + " - " + self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000)
    avatar = models.ImageField(upload_to="image/user/avatar", null=True)
    phn_no  = models.BigIntegerField(unique=True)
    primary_city = models.CharField(max_length=100)
    secondary_city = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    college = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    stream = models.CharField(max_length=255)
    def __str__(self):
        return self.user.username

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    job_desc = models.CharField(max_length=1000)
    def __str__(self):
        return self.user.username

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    LEVEL_CHOICES =(
    ("Beginer", "Beginer"),    
    ("Intermidiate", "Intermidiate"),
    ("Advanced", "Advanced"),
    )

    skill_name = models.CharField(max_length=255)
    skill_level = models.CharField(choices=LEVEL_CHOICES, max_length=255)
    def __str__(self):
        return self.user.username

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    proj_name = models.CharField(max_length=255)
    link = models.CharField(max_length=1250)
    proj_desc = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.user.username

class Accomplishments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000)
    def __str__(self):
        return self.user.username

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=256)
    company_desc = models.CharField(max_length=2000)
    company_logo = models.ImageField(upload_to="image/company/logo", null=True)
    company_website = models.CharField(blank=True, max_length=1000)

    def __str__(self):
        return self.company_name
    