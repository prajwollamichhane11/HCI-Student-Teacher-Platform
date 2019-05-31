from django.shortcuts import render
from django.http import HttpResponse

news1 = "यार्सा टिप्न लेकतिर लर्को विद्यालय बन्द"
news2 = "के छ अर्थमन्त्रीले पूर्वअर्थमन्त्रीलाई पढाएको जीडीपीको अवस्था"
news3 = "विदेशबाट फर्केर ४० कटेसी रमाउने सपना भताभुङ्ग"
news4 = "हिरासतभित्रै युवक झुण्डिएपछि चितवनमा तनाव"


# Create your views here.
# , {'news2':news2}, {'news3':news3}, {'news4':news4}
def index(request):
    return render(request,'index.html', {'news1':news1})
