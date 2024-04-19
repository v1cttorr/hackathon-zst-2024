from django.shortcuts import render
from accounts.models import Client

# Create your views here.
def home(request):
    clients = Client.objects.all()
    for client in clients:
        client.checkDate()
    return render(request, 'home.html')

def scan(request):
    return render(request, 'base/scan.html')

def qr_code(request):
    return render(request, 'base/qr_code.html', {'id': request.user.id})