from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    short_code = models.CharField(max_length=30, unique=True)
    redirect_to = models.URLField(blank=False, null=False)
    amount_of_visits = models.IntegerField(default=0)

    def __str__(self):
        return self.short_code



