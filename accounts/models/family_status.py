from django.db import models


class FamilyStatus(models.Model):
    name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="Семейный статус"
    )

    def __str__(self):
        return self.name
