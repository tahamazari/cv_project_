from django.shortcuts import render
from . models import Items
# Create your views here.
def home(request):
    items = Items.objects
    return render(request, 'home/home.html', {'items':items})
