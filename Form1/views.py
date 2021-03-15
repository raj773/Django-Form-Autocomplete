import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from myapp.models import Contact
from myapp.models import City
def index(request):
    if request.method == "POST":
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        city=request.POST.get('city')

        city_id=City.objects.get(name=city).city_id


        index1= Contact(email=email,phone=phone,desc=desc,city=city_id)
        index1.save()
        #autocomplete
    if 'term' in request.GET:

        qs = City.objects.filter(name__istartswith=request.GET.get('term'))
        title = list()
        for n in qs:
            title.append(n.name)

        return JsonResponse(title, safe=False)
        index1 = Contact(email=email, phone=phone, desc=desc, city=city)
        index1.save()
    return render(request, 'index.html')





