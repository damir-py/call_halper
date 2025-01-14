from django.db import models

from common.models.mixins import BaseDictModelMixin


class ReplacementStatus(BaseDictModelMixin):
    class Meta:
        verbose_name = 'shift status'
        verbose_name_plural = 'shift statuses'

class BreakStatus(BaseDictModelMixin):
    class Meta:
        verbose_name = 'lunch status'
        verbose_name_plural = 'lunch statuses'
