from django.shortcuts import render
from .models import Players,Message

# Create your views here.
def home(request):
    titles = Players.objects.all()
    context = {
         'titles':titles
    }
    return render(request, 'main/index.html',context)

def content(request):
    messages = Message.objects.all()
    context={
        'messages':messages
    }
    return render(request, 'main/content.html',context)

def about_us(request):
    return render(request, 'main/about_us.html')    

def contact_us(request):
    return render(request, 'main/contact_us.html')
