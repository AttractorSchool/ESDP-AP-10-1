from django.db import models


class VotingOptions(models.Model):
    vote = models.ForeignKey(
        to="webapp.Vote",
        related_name="vote_options",
        verbose_name="Голосование опции",
        on_delete=models.CASCADE,
    )
    option = models.TextField(
        verbose_name="Вариант",
        max_length=100
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления варианта"
    )
    is_deleted = models.BooleanField(
        verbose_name="Удаление варианта",
        null=False,
        default=False
    )

    def __str__(self):
        return f"{self.option} {self.vote}"
