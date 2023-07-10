from calendar import HTMLCalendar
from webapp.models import Events
import locale


class Calendar(HTMLCalendar):
    RUSSIAN_MONTH_NAMES = [
        '',
        'Январь',
        'Февраль',
        'Март',
        'Апрель',
        'Май',
        'Июнь',
        'Июль',
        'Август',
        'Сентябрь',
        'Октябрь',
        'Ноябрь',
        'Декабрь',
    ]

    RUSSIAN_DAY_NAMES = [
        'Пн',
        'Вт',
        'Ср',
        'Чт',
        'Пт',
        'Сб',
        'Вс',
    ]

    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super().__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(events_at__day=day).exclude(is_deleted=True)
        events_html = ''
        for event in events_per_day:
            events_html += f'<li>{event.name}</li>'

        if day != 0:
            if len(events_per_day) == 0:
                return f'<td><span class="date">{day}</span><ul class="event-list">{events_html}</ul></td>'
            else:
                return f'<td><span class="date">{day}</span><ul class="event-list">{events_html}</ul>' \
                       f'<span class="event-count">{"•" * len(events_per_day)}</span></td>'
        return '<td></td>'

    def formatweek(self, theweek, events):
        week = ''
        for day, weekday in theweek:
            week += self.formatday(day, events)
        return f'<tr>{week}</tr>'

    def formatmonth(self, withyear=True):
        self.setfirstweekday(0)  # Set Monday as the first day of the week
        events = Events.objects.filter(events_at__year=self.year, events_at__month=self.month)
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'<tr><th colspan="7" class="month">{self.RUSSIAN_MONTH_NAMES[self.month]} {self.year}</th></tr>'
        cal += f'<tr class="weekheader">'
        for day in self.RUSSIAN_DAY_NAMES:
            cal += f'<th>{day}</th>'
        cal += '</tr>'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'<tr>'
            for day, _ in week:
                cal += self.formatday(day, events)
            cal += '</tr>'
        cal += '</table>'
        return cal
