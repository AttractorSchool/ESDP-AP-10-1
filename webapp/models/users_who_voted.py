from django.contrib.auth import get_user_model
from django.db import models


class UsersWhoVoted(models.Model):
    possible_answer = models.ForeignKey(
        to='webapp.VotingOptions',
        related_name='possible_answer',
        on_delete=models.CASCADE,
        verbose_name="Вариант ответа",
        null=True,
        blank=True
    )
    users = models.ForeignKey(
        to=get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Пользователи'
    )
    response_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата ответа"
    )

    def __str__(self):
        return f"{self.possible_answer} {self.users}"
