from django.shortcuts import render
from .models import Deepthought
# Create your views here.
from django.http import HttpResponse

def default(request):
    return render(request, 'upload.html', {})
def home(request):
    return render(request, "home.html", {})
def createThought(request):
    thought_string = str(request.POST.get("thoughtText"))
    title = str(request.POST.get("title"))
    bar = Deepthought(thought=thought_string, title=title)
    bar.save()
    writings = Deepthought.objects.all()
    return render(request, "list.html", {"writings": writings})

def list(request):
    writings = Deepthought.objects.all()
    return render(request, "list.html", {"writings": writings})