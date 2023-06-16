from django.db import models


class TypeEvents(models.Model):
    events_name = models.CharField(
        verbose_name="Мероприятие",
        max_length=30
    )

    def __str__(self):
        return self.events_name
