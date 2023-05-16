from django.db import models


class Cities(models.Model):
    citi_name = models.CharField(
        verbose_name="Город",
        max_length=30
    )

    def __str__(self):
        return self.citi_name
