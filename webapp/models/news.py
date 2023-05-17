from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class News(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        verbose_name="Наименование"
    )
    user = models.ForeignKey(
        to=get_user_model(),
        related_name='user_for_news',
        blank=True,
        verbose_name='Организатор',
        on_delete=models.CASCADE
    )
    cities = models.ForeignKey(
        to='webapp.Cities',
        related_name='сities_for_news',
        on_delete=models.CASCADE,
        verbose_name="Город"
    )
    description = models.TextField(
        max_length=3000,
        null=False,
        verbose_name="Описание"
    )
    photo = models.ManyToManyField(
        to="webapp.Image",
        related_name="photo_for_news",
        verbose_name="Фото"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обнавления"
    )
    is_deleted = models.BooleanField(
        verbose_name="удалено",
        null=False,
        default=False
    )

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.name} - {self.description}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]

