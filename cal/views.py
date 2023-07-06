from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from webapp.models import Events
from .utils import Calendar
from .forms import EventForm


class CalendarView(generic.ListView):
    model = Events
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = self.get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['cal'] = mark_safe(html_cal)
        context['prev_month'] = self.prev_month(d)
        context['next_month'] = self.next_month(d)
        return context

    @staticmethod
    def get_date(req_month):
        if req_month:
            year, month = (int(x) for x in req_month.split('-'))
            return date(year, month, day=1)
        return datetime.today().date()

    @staticmethod
    def prev_month(d):
        first = d.replace(day=1)
        prev_month = first - timedelta(days=1)
        month = f'month={prev_month.year}-{prev_month.month}'
        return month

    @staticmethod
    def next_month(d):
        days_in_month = calendar.monthrange(d.year, d.month)[1]
        last = d.replace(day=days_in_month)
        next_month = last + timedelta(days=1)
        month = f'month={next_month.year}-{next_month.month}'
        return month


def event(request, event_id=None):
    instance = get_object_or_404(Events, pk=event_id) if event_id else None

    form = EventForm(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))

    return render(request, 'event.html', {'form': form})
