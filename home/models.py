from django.db import models


class Link(models.Model):
    short_code = models.CharField(max_length=30)
    redirect_to = models.URLField(blank=False, null=False)
    amount_of_views = models.IntegerField(default=0)

    def __str__(self):
        return self.short_code


