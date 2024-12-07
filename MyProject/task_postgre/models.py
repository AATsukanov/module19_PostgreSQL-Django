from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# новые добавим из 19.1:
class Buyer(models.Model):
    name = models.CharField(max_length=64)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    size = models.DecimalField(max_digits=12, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    # многие-ко-многим:
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title