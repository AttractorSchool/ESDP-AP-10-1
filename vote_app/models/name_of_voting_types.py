from django.db import models


class NameVotingTypes(models.Model):
    name_of_voting_type = models.CharField(
        verbose_name="Наименование типа голосования",
        max_length=100
    )

    def __str__(self):
        return self.name_of_voting_type
