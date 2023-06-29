from django.db import models
from django.contrib.auth import get_user_model


class ChatRequest(models.Model):
    chat_name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Наименование"
    )
    second_user = models.ForeignKey(
        to=get_user_model(),
        related_name='chat_second_user',
        blank=True,
        verbose_name='Второй пользователь',
        on_delete=models.CASCADE
    )
    cities = models.ForeignKey(
        to='webapp.Cities',
        related_name='сities_chat_request',
        on_delete=models.CASCADE,
        verbose_name="Город",
        null=True,
        blank=True
    )
    description = models.TextField(
        max_length=3000,
        null=False,
        verbose_name="Описание"
    )
    rules = models.TextField(
        max_length=3000,
        null=False,
        verbose_name="Правила"
    )