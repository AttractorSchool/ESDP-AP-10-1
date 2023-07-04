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
        null=False,
        blank=False,
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
    is_deleted = models.BooleanField(
        verbose_name="Удалено",
        null=False,
        default=False
    )

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f"{self.level_name} - {self.price}"
