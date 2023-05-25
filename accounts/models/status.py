from django.db import models


class Status(models.Model):
    name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="Cтатус"
    )

    def __str__(self):
        return self.name
