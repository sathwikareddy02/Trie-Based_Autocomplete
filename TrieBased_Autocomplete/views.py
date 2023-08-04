# TrieBased_Autocomplete/urls.py

from django.contrib import admin
from django.urls import path, include
from TrieBased_AutocompleteApp.views import autocomplete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autocomplete/', autocomplete_view, name='autocomplete'),
]


