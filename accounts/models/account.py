from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class Account(AbstractUser):
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=False,
        verbose_name="Имя",
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=False,
        verbose_name="Фамилия",
    )
    middle_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Отчество",
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    about_me = models.TextField(
        max_length=3000,
        null=True,
        verbose_name="Описание"
    )
    occupation = models.TextField(
        max_length=3000,
        null=True,
        verbose_name="Род деятельности"
    )
    cities = models.ForeignKey(
        to='webapp.Cities',
        related_name='сities_for_account',
        on_delete=models.CASCADE,
        verbose_name="Город"
    )
    status = models.ForeignKey(
        to='accounts.Status',
        related_name='status_for_account',
        on_delete=models.CASCADE,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
    )
    family_status = models.ForeignKey(
        to='accounts.FamilyStatus',
        related_name='family_status_for_account',
        on_delete=models.CASCADE,
        verbose_name="Семейный статус"
    )
    first_visit_app = models.BooleanField(
        verbose_name="Первое посещение приложения",
        null=False,
        default=True
    )
    likes_qty = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Количество лайков"
    )
    dislikes_qty = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Количество дизлайков"
    )
    avatar = models.ForeignKey(
        null=True,
        blank=True,
        to="webapp.Image",
        verbose_name='Аватар',
        on_delete=models.CASCADE
    )
    role = models.ForeignKey(
        to='accounts.Role',
        related_name='role_for_account',
        on_delete=models.CASCADE,
        verbose_name="Роль"
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
        unique=True,
        blank=False
    )
    phone = models.CharField(
        verbose_name="Номер телефона",
        blank=True,
        max_length=30
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class RegisterAdminUser(models.Model):
    resident = models.OneToOneField(
        get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='Профиль пользователя'
    )
    admin = models.ForeignKey(
        to=get_user_model(),
        related_name='admin',
        blank=False,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Администратор'
    )
