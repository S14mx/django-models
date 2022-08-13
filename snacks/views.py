from django.views.generic import ListView, DetailView, TemplateView
from .models import Snack


class HomePageView(TemplateView):
    template_name = 'home.html'


class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    # context_object_name = 'custom name' <== object_list


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
