from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# , {'news2':news2}, {'news3':news3}, {'news4':news4}
@csrf_exempt
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def courses(request):
    return render(request,'courses.html')

def blogs(request):
    return render(request,'blogs.html')

def contact(request):
    return render(request,'contact.html')
