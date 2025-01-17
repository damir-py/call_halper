from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Break(models.Model):
    replacement = models.ForeignKey('breaks.replacement', models.CASCADE, 'breaks')
    employee = models.ForeignKey(User, models.CASCADE, 'breaks')

    break_start = models.TimeField(blank=True, null=True)
    break_end = models.TimeField(blank=True, null=True)

    status = models.ForeignKey(
        'breaks.BreakStatus', models.RESTRICT, 'breaks', blank=True
    )

    class Meta:
        verbose_name = 'lunch break'
        verbose_name_plural = 'lunch breaks'
        ordering = ('-replacement__date', 'break_start')

    def __str__(self):
        return f'{self.employee} - {self.pk}'
