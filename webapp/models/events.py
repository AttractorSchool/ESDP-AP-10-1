from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

from accounts.models.validators import validate_date_event


class Events(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Наименование",
        validators=[MinLengthValidator(2)]
    )
    cities = models.ForeignKey(
        to='webapp.Cities',
        related_name='сities',
        on_delete=models.CASCADE,
        verbose_name="Город",
        null=True,
        blank=True
    )
    type_events = models.ForeignKey(
        to='webapp.TypeEvents',
        related_name='type_events',
        on_delete=models.CASCADE,
        verbose_name="Тип мероприятия",
        null=False,
        blank=False
    )
    events_at = models.DateTimeField(
        verbose_name="Дата мероприятия",
        null=False,
        blank=False,
        validators=[validate_date_event]
    )
    sponsor = models.ForeignKey(
        to=get_user_model(),
        related_name='sponsor',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Организатор'
    )
    number_of_seats = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(2), MaxValueValidator(100)],
        verbose_name="Количество мест"
    )
    start_register_at = models.DateTimeField(
        verbose_name="Дата начала регистрации",
        null=True,
        default=None,
        validators=[validate_date_event]
    )
    end_register_at = models.DateTimeField(
        verbose_name="Дата конца регистрации",
        null=True,
        blank=True,
        validators=[validate_date_event]
    )
    resident_booked = models.ManyToManyField(
        to=get_user_model(),
        through='UserBooked',
        related_name='user_booked',
        blank=True,
        verbose_name='Бранированные резиденты'
    )
    description = models.TextField(
        max_length=3000,
        null=False,
        verbose_name="Описание",
        validators=[MinLengthValidator(2)]
    )
    place = models.CharField(
        max_length=200,
        null=True,
        verbose_name="Место",
        validators=[MinLengthValidator(2)]
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Цена",
        validators=[MinValueValidator(0)]
    )
    is_deleted = models.BooleanField(
        verbose_name="Удалено",
        null=False,
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обнавления"
    )
    photo = models.ForeignKey(
        to='webapp.Image',
        related_name='event_image',
        on_delete=models.CASCADE,
        verbose_name="Фото мероприятия",
        null=True,
        blank=True
    )

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"Event {self.name} - started {self.events_at}"


class UserBooked(models.Model):
    resident = models.ForeignKey(
        to=get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Забронировал'
    )
    event = models.ForeignKey(
        to=Events,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Мероприятие'
    )
    booking_date = models.DateTimeField(
        null=False,
        blank=False
    )
    date_of_payment = models.DateTimeField(
        null=True,
        blank=True
    )
    cancellation_date = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"resident id-{self.resident} booking in events id-{self.event}"
