import datetime

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.timezone import now


def validate_full_name(value):
    """Валидация на написание с заглавной буквы"""
    if not value.istitle():
        raise ValidationError(
            "Название не должно начинаться с маленькой буквы"
        )


# Валидация номера телефона
phoneNumberRegex = RegexValidator(
        regex=r"^\+?1?\d{8,15}$"
    )


def validate_age(birth_date):
    '''Валидация на возраст пользователя'''
    today = now()
    if (today.year - birth_date.year) < 16:
        raise ValidationError('Возраст должен быть не менее 16 лет')


