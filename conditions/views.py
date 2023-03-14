from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':'25','b':'30'}
    return render(request,'conditions.html',context=d)