from django.shortcuts import render,HttpResponse
import requests

# Create your views here.
def index(request):
    flag = True
    while(flag):
        try:
            result = requests.get("https://api.covid19api.com/summary")
            flag= False
        except:
            flag = True
    return render(request,'index.html',{"result":result.json()})
