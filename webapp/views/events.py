from django.views.generic import DetailView

from webapp.models import Events


class EventDetailView(DetailView):
    model = Events
    template_name = 'event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_seats = self.object.number_of_seats
        booked_seats = self.object.resident_booked.count()
        available_seats = total_seats - booked_seats
        context['available_seats'] = available_seats
        return context
