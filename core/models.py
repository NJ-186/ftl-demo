from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.


class USER(models.Model):
    id = models.CharField(
        max_length = 10,
        primary_key = True
    )
    real_name = models.CharField(
        max_length = 50,
        null = False,
        help_text = _(
            'Name of the user.'
        )
    )
    tz = models.CharField(
        max_length = 100,
        null = False,
        help_text = _(
            'Location of the user.'
        )
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    user = models.ForeignKey(
        USER,
        on_delete = models.PROTECT,
        related_name = 'activity_periods',
        help_text = _(
            'Details of associated user'
        )
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name = 'activity period'
        verbose_name_plural = 'activity periods'