from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator

class AdminRequest(models.Model):
    user_reviewer = models.ForeignKey(
        to=get_user_model(),
        related_name='admin_reviewer',
        null=True,
        blank=True,
        verbose_name='Проверяющий',
        on_delete=models.CASCADE
    )
    user_sender = models.ForeignKey(
        to=get_user_model(),
        related_name='user_request',
        null=False,
        blank=False,
        verbose_name='Отправитель',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    closing_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        verbose_name="Дата закрытия"
    )
    approved = models.BooleanField(
        verbose_name="Утвержден?",
        null=True,
        blank=True,
        default=None
    )
    request_text = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name="Текст запроса",
        validators=[MinLengthValidator(2)]
    )
    response_text = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name="Ответ админа",
        validators=[MinLengthValidator(2)]
    )
    sub_level = models.ForeignKey(
        to='webapp.SubscriptionLevel',
        related_name='sub_level',
        on_delete=models.CASCADE,
        verbose_name="Запрос на подписку",
        null=True,
        blank=True
    )
    chat_request = models.ForeignKey(
        to='webapp.ChatRequest',
        related_name='chat_admin_request',
        on_delete=models.CASCADE,
        verbose_name="Запрос на создание чата",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user_sender} {self.created_at}"
