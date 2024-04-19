from django.shortcuts import render, HttpResponse

# Create your views here.
def buy(request):
    return render(request, 'payment/buy.html')