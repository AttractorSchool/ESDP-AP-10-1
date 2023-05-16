from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Events(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        verbose_name="Наименование"
    )
    cities = models.ForeignKey(
        to='webapp.Cities',
        related_name='сities',
        on_delete=models.CASCADE,
        verbose_name="Город"
    )
    type_events = models.ForeignKey(
        to='webapp.TypeEvents',
        related_name='type_events',
        on_delete=models.CASCADE,
        verbose_name="Тип мероприятия"
    )
    events_at = models.DateTimeField(
        verbose_name="Дата мероприятия",
        null=False,
        default=None
    )
    user = models.ManyToManyField(
        to=get_user_model(),
        related_name='user',
        blank=True,
        verbose_name='Организатор'
    )
    number_of_seats = models.IntegerField(
        verbose_name="Количество мест"
    )
    start_register_at = models.DateTimeField(
        verbose_name="дата начала регистрации",
        null=True,
        default=None
    )
    end_register_at = models.DateTimeField(
        verbose_name="дата конца регистрации",
        null=True,
        default=None
    )
    user_booked = models.ManyToManyField(
        to=get_user_model(),
        related_name='user_booked',
        blank=True,
        verbose_name='забронировали_место'
    )
    user_paid = models.ManyToManyField(
        to=get_user_model(),
        related_name='user_paid',
        blank=True,
        verbose_name='оплатили'
    )
    description = models.TextField(
        max_length=3000,
        null=False,
        verbose_name="Описание"
    )
    place = models.CharField(
        max_length=200,
        null=True,
        verbose_name="Место"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Цена"
    )
    is_deleted = models.BooleanField(
        verbose_name="удалено",
        null=False,
        default=False
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )
    update_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обнавления"
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to="user_pic",
        verbose_name="Фото мероприятия",
        default="user_pic/default_user_pic.jpeg"
    )

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.name} - {self.start_register_at}"
