from django import forms
from .models import Events
from webapp.models import News
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = (
            "name",
            "user",
            "cities",
            "description",
            "photo"
        )

        labels = {
            "name": "Наименование новости",
            "user": "Пользователь",
            "cities": "Город",
            "description": "Описание новости",
            "photo": "Фото",
        }

    def clean_title(self):
        name = self.cleaned_data.get("name")
        if len(name) < 2:
            raise ValidationError(
                "Наименование должно быть длиннее 2 символов"
            )
        if News.objects.filter(name=name).exists():
            raise ValidationError(
                "Наименование с таким именем уже есть"
            )
        return name


class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = (
            'name', 'cities', 'type_events', 'cities', 'events_at', 'sponsor', 'number_of_seats', 'start_register_at',
            'end_register_at', 'description', 'place', 'price', 'photo')
        labels = {
            "name": "Название",
            "cities": "Город",
            "type_events": "Тип мероприятия",
            "events_at": "Дата мероприятия",
            "sponsor": "Спонсор",
            "number_of_seats": "Количество мест",
            "start_register_at": "Начало регистрации",
            "end_register_at": "Конец регистрации",
            "description": "Описание",
            "place": "Место расположения",
            "price": "Цена",
            "photo": "Фото"
        }
