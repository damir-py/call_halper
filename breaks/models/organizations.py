from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Organization(models.Model):
    name = models.CharField(max_length=225)
    director = models.ForeignKey(to=User, on_delete=models.RESTRICT, related_name='organization_directors')
    employees = models.ManyToManyField(User, related_name='organization_employees')

    def __str__(self):
        return f'{self.name} - {self.id}'
