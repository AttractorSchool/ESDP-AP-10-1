from django.contrib.auth import get_user_model
from django.db import models


class ListVotes(models.Model):
    name_of_the_vote = models.CharField(
        verbose_name="Наименование голосования",
        max_length=200
    )
    user_who_created_list_votes = models.ForeignKey(
        to=get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Пользователь создавший список из голосований'
    )
    date_group_was_added_from_polls = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата добавления группу из голосований"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления списка"
    )
    voting_opening_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата открытия голосования"
    )
    expiration_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата окончания"
    )
    is_deleted = models.BooleanField(
        verbose_name="Удалено голосования",
        null=False,
        default=False
    )
    vote = models.ManyToManyField(
        to="vote_app.Vote",
        related_name="vote_list",
        verbose_name="Голосование список"
    )

    def __str__(self):
        return f"{self.name_of_the_vote} {self.vote}"
