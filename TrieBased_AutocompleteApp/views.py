# TrieBased_AutocompleteApp/views.py

from django.shortcuts import render
from .trie import Trie, populate_trie
from .models import Word

# Initialize Trie and populate it with the dataset
trie = Trie()
populate_trie(trie, 'TrieBased_AutocompleteApp/wordlist.txt')

def autocomplete_view(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        num_suggestions = int(request.GET.get('num_suggestions', 5))

        # Add the query to the Trie and database
        trie.add_word(query)
        word_obj, created = Word.objects.get_or_create(word=query)

        # Get suggestions from the Trie
        suggestions = trie.autocomplete(query, num_suggestions)

        # Check if the query exists in the dataset
        if query in suggestions:
            suggestions.remove(query)  # Remove the query from suggestions as it is already in the dataset

        # Get remembered words from the database
        remembered_words = Word.objects.filter(word__startswith=query).exclude(word=query)
        remembered_suggestions = [word.word for word in remembered_words if word.word != query]

        return render(request, 'autocomplete.html', {'suggestions': suggestions, 'remembered_suggestions': remembered_suggestions})

    # Return an empty response when there are no suggestions or invalid request method
    return render(request, 'autocomplete.html', {'suggestions': [], 'remembered_suggestions': []})







