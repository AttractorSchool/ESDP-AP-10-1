from django.db import models


class SubscriptionLevel(models.Model):
    level_name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Уровень подписки"
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
        verbose_name="Цена"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обнавления"
    )
