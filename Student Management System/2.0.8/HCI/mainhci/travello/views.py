from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

news1 = "यार्सा टिप्न लेकतिर लर्को विद्यालय बन्द"
news2 = "के छ अर्थमन्त्रीले पूर्वअर्थमन्त्रीलाई पढाएको जीडीपीको अवस्था"
news3 = "विदेशबाट फर्केर ४० कटेसी रमाउने सपना भताभुङ्ग"
news4 = "हिरासतभित्रै युवक झुण्डिएपछि चितवनमा तनाव"

# Create your views here.
# , {'news2':news2}, {'news3':news3}, {'news4':news4}
@csrf_exempt
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def courses(request):
    return render(request,'courses.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')
