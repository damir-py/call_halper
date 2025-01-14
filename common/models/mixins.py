from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseDictModelMixin(models.Model):
    code = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=35)
    sort = models.PositiveSmallIntegerField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('sort',)
        abstract = True

    def __str__(self):
        return f'{self.code} - {self.name}'
