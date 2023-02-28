from django.shortcuts import render
from django.views.generic import ListView
from .models import Characters


# Create your views here.
class MainPage(ListView):
    """Main page"""
    model = Characters
    context_object_name = 'characters'
    extra_context = {'title': 'Main page'}
    template_name = 'index.html'

    def get_queryset(self):
        """Output characters"""
        characters = Characters.objects
        return characters
