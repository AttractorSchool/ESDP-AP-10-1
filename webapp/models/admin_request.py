from django.db import models
from django.contrib.auth import get_user_model


class AdminRequest(models.Model):
    user_reviewer = models.ForeignKey(
        to=get_user_model(),
        related_name='admin_reviewer',
        blank=True,
        verbose_name='Проверяющий',
        on_delete=models.CASCADE
    )
    user_sender = models.ForeignKey(
        to=get_user_model(),
        related_name='user_request',
        blank=True,
        verbose_name='Отправитель',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    closing_at = models.DateTimeField(
        null=True,
        default=None,
        verbose_name="Дата закрытия"
    )
    approved = models.BooleanField(
        verbose_name="Удалено",
        null=True,
        default=True
    )
    request_text = models.TextField(
        max_length=3000,
        null=True,
        verbose_name="Текст запроса"
    )
    response_text = models.TextField(
        max_length=3000,
        null=True,
        verbose_name="Ответ админа"
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
