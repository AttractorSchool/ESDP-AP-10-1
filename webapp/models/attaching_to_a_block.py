from django.contrib.auth import get_user_model
from django.db import models


class AttachingToBlock(models.Model):
    list_of_votes = models.ForeignKey(
        to='webapp.ListVotes',
        related_name='list_of_votes',
        on_delete=models.CASCADE,
        verbose_name="Список голосования",
        null=True,
        blank=True
    )
    events = models.ForeignKey(
        to='webapp.Events',
        related_name='events',
        on_delete=models.CASCADE,
        verbose_name="Мероприятия",
        null=True,
        blank=True
    )
    news = models.ForeignKey(
        to='webapp.News',
        related_name='news',
        on_delete=models.CASCADE,
        verbose_name="Новости",
        null=True,
        blank=True
    )
    users = models.ForeignKey(
        to=get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Пользователь которому дали список из голосований'
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата добавления голосования"
    )

    def __str__(self):
        return f"{self.list_of_votes} {self.users}"
