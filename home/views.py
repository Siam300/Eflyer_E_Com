from django.shortcuts import render
from django.http import JsonResponse
from .models import manTshirt, manShirt, womanScart,laptop, mobile, computer, jumkas, kangans, necklaces

# Create your views here.

def index(request):
    # return JsonResponse({'foo':'bar'})
    manTshirt= manTshirt.objects.all
    manShirt= manShirt.objects.all 
    womanScart= womanScart.objects.all 

    laptop= laptop.objects.all 
    mobile= mobile.objects.all 
    computer= computer.objects.all 

    jumkas= jumkas.objects.all 
    kangans= kangans.objects.all 
    necklaces= necklaces.objects.all 

    context = {
        "fasion" : [manTshirt,manShirt,womanScart]
        "electronics" : [laptop, mobile, computer]
        "jewelery" : [jumkas, kangans, necklaces]
    }
    return render(request, 'index.html', context=context)