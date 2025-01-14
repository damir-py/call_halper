from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Organization(models.Model):
    name = models.CharField(max_length=225)
    director = models.ForeignKey(to=User, on_delete=models.RESTRICT, related_name='organization_directors')
    employees = models.ManyToManyField(User, related_name='organization_employees')

    def __str__(self):
        return f'{self.name} - {self.id}'

class Group(models.Model):
    organization = models.ForeignKey('breaks.Organization', on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=225)
    manager = models.ForeignKey(User, models.RESTRICT, 'group_managers')
    employees = models.ManyToManyField(User, related_name='group_employees')
    min_active = models.PositiveSmallIntegerField(null=True, blank=True)

    break_start = models.TimeField(blank=True, null=True)
    break_end = models.TimeField(blank=True, null=True)
    break_max_duration = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.id}'

    @property
    def break_duration(self):
        return 500