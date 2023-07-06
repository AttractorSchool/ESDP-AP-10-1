from calendar import HTMLCalendar
from webapp.models import Events


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super().__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(events_at__day=day)
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
        events = Events.objects.filter(events_at__year=self.year, events_at__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal