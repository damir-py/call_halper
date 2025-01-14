from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ReplacementStatus(models.Model):
    code = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=35)
    sort = models.PositiveSmallIntegerField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.code}'


class Replacement(models.Model):
    group = models.ForeignKey('breaks.Group', models.CASCADE, 'replacement')
    date = models.DateField()
    break_start = models.TimeField()
    break_end = models.TimeField()
    break_max_duration = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.group.name} - {self.pk}'


class ReplacementEmployee(models.Model):
    employee = models.ForeignKey(User, models.CASCADE, 'replacements')
    replacement = models.ForeignKey('breaks.Replacement', models.CASCADE, 'employees')
    status = models.ForeignKey('breaks.ReplacementStatus', models.RESTRICT, 'replacement_employees')

    def __str__(self):
        return f'session {self.replacement} to {self.employee}'
