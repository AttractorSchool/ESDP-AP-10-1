from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from accounts.models.validators import validate_full_name, validate_age, phoneNumberRegex
from django.core.validators import MinLengthValidator, URLValidator


class Account(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=False,
        blank=True,
        null=True,
        validators=[MinLengthValidator(2)]
    )
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=False,
        verbose_name="Имя",
        validators=[validate_full_name]
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=False,
        verbose_name="Фамилия",
        validators=[validate_full_name]
    )
    middle_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Отчество",
        validators=[validate_full_name]
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения',
        validators=[validate_age]
    )
    about_me = models.TextField(
        max_length=3000,
        null=True,
        verbose_name="Описание",
        validators=[MinLengthValidator(2)]
    )
    occupation = models.TextField(
        max_length=3000,
        null=True,
        verbose_name="Род деятельности",
        validators=[MinLengthValidator(2)]
    )
    cities = models.ForeignKey(
        to='webapp.Cities',
        related_name='сities_for_account',
        on_delete=models.CASCADE,
        verbose_name="Город",
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        to='accounts.Status',
        related_name='status_for_account',
        on_delete=models.CASCADE,
        verbose_name="Статус",
        null=True,
        blank=True
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
        verbose_name="Семейный статус",
        null=True,
        blank=True
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
        verbose_name="Роль",
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
        null=True,
        unique=True,
        blank=False
    )
    phone = models.CharField(
        verbose_name="Номер телефона",
        null=True,
        blank=True,
        max_length=30,
        validators=[phoneNumberRegex]
    )
    industries = models.CharField(
        verbose_name="Отрасли",
        null=True,
        blank=True,
        max_length=250,
        validators=[MinLengthValidator(2)]
    )
    companies = models.CharField(
        verbose_name="Компании",
        null=True,
        blank=True,
        max_length=250,
        validators=[MinLengthValidator(2)]
    )
    expertise = models.CharField(
        verbose_name="Экспертиза",
        null=True,
        blank=True,
        max_length=250,
        validators=[MinLengthValidator(2)]
    )
    resources_available = models.CharField(
        verbose_name="Ресурсы имеющиеся",
        null=True,
        blank=True,
        max_length=250,
        validators=[MinLengthValidator(2)]
    )
    resources_searching = models.CharField(
        verbose_name="Ресурсы запрашиваемые",
        null=True,
        blank=True,
        max_length=250,
        validators=[MinLengthValidator(2)]
    )
    achievements = models.CharField(
        verbose_name="Достижения",
        null=True,
        blank=True,
        max_length=250,
        validators=[MinLengthValidator(2)]
    )
    goal_for_the_year = models.CharField(
        verbose_name="Цель на год",
        null=True,
        blank=True,
        max_length=250,
        validators=[MinLengthValidator(2)]
    )
    request = models.CharField(
        verbose_name="Запрос",
        null=True,
        blank=True,
        max_length=250,
        validators=[MinLengthValidator(2)]
    )
    hobby = models.CharField(
        verbose_name="Хобби",
        null=True,
        blank=True,
        max_length=250,
        validators=[MinLengthValidator(2)]
    )
    education = models.CharField(
        verbose_name="Образование",
        null=True,
        blank=True,
        max_length=250,
        validators=[MinLengthValidator(2)]
    )
    children = models.CharField(
        verbose_name="Дети",
        null=True,
        blank=True,
        max_length=50
    )
    facts_about_me = models.CharField(
        verbose_name="Факты обо мне",
        null=True,
        blank=True,
        max_length=250,
        validators=[MinLengthValidator(2)]
    )
    site = models.CharField(
        verbose_name="Сайт",
        null=True,
        blank=True,
        max_length=50,
        validators=[URLValidator()]
    )
    social_links = models.CharField(
        verbose_name="Ссылки на социальные сети",
        null=True,
        blank=True,
        max_length=250,
        validators=[MinLengthValidator(2)]
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ["first_name"]


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

    def __str__(self):
        return f'{self.admin} created {self.resident}'
