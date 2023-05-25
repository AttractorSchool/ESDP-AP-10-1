from django.db import models


class Role(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name="Роль"
    )

    def __str__(self):
        return self.name