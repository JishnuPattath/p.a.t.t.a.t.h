from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import make

# Create your views here.
def index(request):
    obj = place.objects.all()
    obj2 = make.objects.all()
    return render(request,'index.html',{'result':obj,'making':obj2})



