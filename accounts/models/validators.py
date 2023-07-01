import datetime

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.timezone import now
from datetime import date

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


# Валидация на возраст пользователя
def validate_age(birth_date):
    today = now()
    if (today.year - birth_date.year) < 16:
        raise ValidationError('Возраст должен быть не менее 16 лет')


# Валидация на дату начала/окончания регистрации мероприятия и даты мероприятия,
# которые не должна быть ранее даты создания самого мероприятия
def validate_date_event(start_register_at):
    today = datetime.date.today()
    date_start_register_at = start_register_at.date()
    if date_start_register_at < today:
        raise ValidationError('Указанная дата не должна быть ранее даты создания самого мероприятия')