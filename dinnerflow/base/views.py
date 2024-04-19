from django.shortcuts import render
from accounts.models import Client

# Create your views here.
def home(request):
    clients = Client.objects.all()
    for client in clients:
        client.checkDate()
    return render(request, 'home.html')

def scan(request):
    try:
        ID = request.GET.get('var')
        print(ID)
        client = Client.objects.get(user_id=ID)
    except:
        client = None
        ID = None
    return render(request, 'base/scan.html', {'id': ID, 'client': client})

def qr_code(request):
    return render(request, 'base/qr_code.html', {'id': request.user.id})