from django.shortcuts import render
from accounts.models import Client
from datetime import date

# Create your views here.
def home(request):
    try:
        clients = Client.objects.all()
    
        for client in clients:
            client.checkDate()
    

        human = Client.objects.get(user_id=request.user.id)
    
        days_left = (date.today() - human.date_of_purchase).days
        print(days_left)

        context = {
            'date_of_purchase': human.date_of_purchase,
            'days_left': days_left,
            }

    except:
        context = {}

    return render(request, 'home.html', context)

def scan(request):
    print(f'aaaa {request.user.pk}')
    try:
        ID = request.GET.get('var')
        print(ID)
        client = Client.objects.get(user_id=ID)
        print(client.name)
    except:
        client = None
        ID = None

    try:
        clients = Client.objects.all()
    
        for client in clients:
            client.checkDate()
    except:
        pass

    return render(request, 'base/scan.html', {'id': ID, 'client': client})

def qr_code(request):
    return render(request, 'base/qr_code.html', {'id': request.user.id})