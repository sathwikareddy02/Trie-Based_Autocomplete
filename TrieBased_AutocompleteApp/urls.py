# TrieBased_AutocompleteApp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('autocomplete/', views.autocomplete_view, name='autocomplete'),
]

