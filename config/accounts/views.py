from django.shortcuts import render
from accounts.forms import *

# Create your views here.
def home(request):
    return render(request,'home.html')




def register(request):
    EUMFO=UserForm()
    d={'EUMFO':EUMFO}
    return render(request,'register.html',d)