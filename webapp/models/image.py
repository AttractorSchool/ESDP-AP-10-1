from django.core.validators import validate_image_file_extension
from django.db import models
from django.contrib.auth import get_user_model


class Image(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to="user_pic",
        verbose_name="Фото",
        validators=[validate_image_file_extension]
    )
    user = models.ForeignKey(
        to=get_user_model(),
        related_name='user_image',
        blank=False,
        null=False,
        verbose_name='Организатор',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )

    def __str__(self):
        return f"Фотография {self.user} - {self.created_at}"
