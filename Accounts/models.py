from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):

  def _create_user(self, email, password,is_customer, is_seller, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_customer=is_customer,
        is_seller=is_seller,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, True, True, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

###  user details ######
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address1 = models.CharField(blank=True, max_length=150)
    address2 = models.CharField(blank=True, max_length=150)
    address3 = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    zipcode = models.CharField(blank=True, max_length=10)
    country = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.user.email

    def user_name(self):
        return self.user.email


class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone1 = models.CharField(blank=True, max_length=20)
    phone2 = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    zipcode = models.CharField(blank=True, max_length=10)
    country = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.user.email

    def user_name(self):
        return self.user.email

