from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import get_user_model


class Review(models.Model):
    user_write_review = models.ForeignKey(
        get_user_model(),
        related_name='reviews',
        on_delete=models.CASCADE,
        verbose_name='Создатель отзыва'
    )
    user_receive_review = models.ForeignKey(
        'accounts.Account',
        related_name='reviews_for_user_receive_review',
        verbose_name='Отзыв к профилю',
        on_delete=models.CASCADE,
        null=True
    )
    text = models.TextField(
        max_length=3000,
        null=True,
        verbose_name='Текст отзыва',
        blank=True,
        validators=[MinLengthValidator(2)]
    )
    like = models.BooleanField(
        verbose_name="Лайк",
        null=True,
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
    )

    def __str__(self):
        return f'Отзыв от {self.user_write_review.username} к профилю : {self.user_receive_review.last_name}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

