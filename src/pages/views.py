from django.http import HttpResponse 
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "test": "hi",
        "test1": [123, 456, 789, "Abc"]
    }
    return render(*args,"home.html", my_context)

def contact_view(*args, **kwargs):
    return render(*args,"contact.html", {})

