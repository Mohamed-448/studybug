from django.shortcuts import render
from django.http import HttpResponse 
def index(request): 
    return render(request,'demoapp/index.html',{'name':'ahmed','age':'25'})

def about(request): 
    return HttpResponse("Hello, world. This is the about.") 


def drinks(request,drink_name):
    drink={
        'mocha':'tybe of coofe',
        'tea':'tybe of bevarege',
        'lemonadaa':'tybe of refshment'
    }
    choice_of_drink=drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)
    
    




# Create your views here.
