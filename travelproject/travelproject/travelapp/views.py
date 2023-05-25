from django.http import HttpResponse
from django.shortcuts import render
from . models import Details

# Create your views here.
# class HttpsResponse:
#     pass


def demo(request):
    obj=Details.objects.all()
    return render(request,"index.html",{'result':obj})



# def addition (request):
#     x= int(request.GET['number1'])
#     y= int(request.GET['number1'])
#     res1=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#
#
#
#     return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})
