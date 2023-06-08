from django.db import models


class VotingTypes(models.Model):
    voting_type = models.ForeignKey(
        to='webapp.NameVotingTypes',
        related_name='name_voting_types',
        on_delete=models.CASCADE,
        verbose_name="Тип голосования",
        null=True,
        blank=True
    )
    vote = models.ForeignKey(
        to='webapp.Vote',
        related_name='vote_type',
        on_delete=models.CASCADE,
        verbose_name="Голосование типы",
        null=False,
        blank=False
    )
    boolean_value = models.BooleanField(
        verbose_name="Булева значение",
        null=False,
        default=True
    )

    def __str__(self):
        return f"{self.voting_type} {self.vote}"
