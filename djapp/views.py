# from django.shortcuts import render
from django.views.generic import (ListView, DetailView)  # View,TemplateView, CreateView,DeleteView, UpdateView

from . import models


# Create your views here.

class ItemListView(ListView):
    model = models.Item


class ItemDetailView(DetailView):
    model = models.Item


