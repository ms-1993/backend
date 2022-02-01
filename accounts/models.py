from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from multiselectfield import MultiSelectField

class CustomUser(AbstractUser):
    """ custom user model """

    USER = (
        ('admin', _('ADMIN USER')),
        ('user', _('USER'))
    )

    username = None
    first_name = None
    last_name = None
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=10, unique=True, null=False, blank=False)
    roll = MultiSelectField(max_length=50, choices=USER, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    def create_user(self):
        pass

    class Meta:
        verbose_name = 'User'
        ordering = ['-date_joined']