from django.core.validators import MinLengthValidator
from django.db import models


class Vote(models.Model):
    question_to_vote = models.TextField(
        verbose_name="Вопрос на голосование",
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обнавления голосования"
    )

    def __str__(self):
        return self.question_to_vote
