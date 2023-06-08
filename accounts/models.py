from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


from .managers import PlayerManager

class Player(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    username = models.CharField(_('username'), max_length=30, unique=True, null=True)
    email = models.CharField(_('email'), max_length=100, unique=True, null=True)
    score = models.IntegerField(default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('first_name', 'last_name','email')

    objects = PlayerManager()

    def __str__(self):
        return self.username
