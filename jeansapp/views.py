from django.shortcuts import render
from . models import Cloths

# Create your views here.
def index(request):

    cloths=Cloths.objects.all()
    return render(request,'index.html', {'cloths':cloths})