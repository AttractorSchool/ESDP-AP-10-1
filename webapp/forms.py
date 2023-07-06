from django import forms
from .models import Events


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
