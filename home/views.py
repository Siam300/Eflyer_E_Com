from django.shortcuts import render
from django.http import JsonResponse
from .models import manTshirt, manShirt, womanScart,laptop, mobile, computer, jumkas, kangans, necklaces


# Create your views here.

def index(request):
    # return JsonResponse({'foo':'bar'})

    mantshirt= manTshirt.objects.all()
    manshirt= manShirt.objects.all()
    womanscart= womanScart.objects.all()

    laptops= laptop.objects.all()
    mobiles= mobile.objects.all()
    computers= computer.objects.all()

    jumkass= jumkas.objects.all()
    kanganss= kangans.objects.all()
    necklacess= necklaces.objects.all()

    Fashion = list(zip(mantshirt, manshirt, womanscart))
    Electronics = list(zip(laptops, mobiles, computers))
    Jewellery = list(zip(jumkass, kanganss, necklacess))

    

    context = {
        "fashion" : Fashion,
        "electronics" : Electronics,
        "ewelery" : Jewellery
    }
    return render(request, 'index.html', context=context)