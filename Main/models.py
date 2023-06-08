from django.db import models

# Create your models here.

from accounts.models import Player
class Challenges(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255)
    points = models.IntegerField()
    description = models.TextField(max_length=1000, default='')
    hint = models.CharField(max_length=255, default='')
    flag = models.CharField(max_length=255, default='DPSS{EMPTY}')
    link = models.CharField(max_length=255, default='dashboard')
    solve_status = models.BooleanField(default=False)
    players_solved = models.ManyToManyField(Player, blank=True, related_name='challenges_solved')


    def __str__(self):
        return self.title
