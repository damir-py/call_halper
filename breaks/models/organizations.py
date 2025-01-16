from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Organization(models.Model):
    name = models.CharField(max_length=225)
    director = models.ForeignKey(User, models.RESTRICT, 'organization_directors')
    employee = models.ManyToManyField(User, 'organization_employees')

    def __str__(self):
        return f'{self.name} - {self.pk}'
