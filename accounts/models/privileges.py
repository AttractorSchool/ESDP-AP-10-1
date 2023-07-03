from django.db import models


class Privileges(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name="Привилегии"
    )

    def __str__(self):
        return self.name
