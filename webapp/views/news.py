from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import NewsForm
from webapp.models import News


class NewsCreateView(CreateView):
    template_name = 'news_create.html'
    model = News
    form_class = NewsForm

    def get_success_url(self):
        return reverse('news_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        news = form.save(commit=False)
        news.save()
        return super().form_valid(form)


class NewsUpdateView(UpdateView):
    template_name = 'news_update.html'
    form_class = NewsForm
    model = News

    def get_success_url(self):
        return reverse('news_detail', kwargs={'pk': self.object.pk})


class NewsDetail(DetailView):
    template_name = 'news_detail.html'
    model = News
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NewsDeleteView(DeleteView):
    template_name = 'news_confirm_delete.html'
    model = News
    success_url = reverse_lazy('newsline')
