from webapp.models import Events
from django.forms import ModelForm, TextInput, DateInput, Textarea, NumberInput, Select


class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = [
            'name', 'cities', 'type_events', 'events_at', 'sponsor', 'number_of_seats', 'start_register_at',
            'end_register_at', 'description', 'place', 'price', 'photo'
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'cities': Select(attrs={'class': 'form-control'}),
            'type_events': Select(attrs={'class': 'form-control'}),
            'booking_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'events_at': DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'sponsor': Select(attrs={'class': 'form-control'}),
            'number_of_seats': NumberInput(attrs={'class': 'form-control'}),
            'start_register_at': DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'},
                                           format='%Y-%m-%dT%H:%M'),
            'end_register_at': DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'},
                                         format='%Y-%m-%dT%H:%M'),
            'description': Textarea(attrs={'class': 'form-control'}),
            'place': TextInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
        }
