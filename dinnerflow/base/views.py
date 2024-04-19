from django.shortcuts import render
from accounts.models import Client
from datetime import date, timedelta

# Create your views here.
def home(request):
    try:
        clients = Client.objects.all()

        for client in clients:
            client.checkDate()

        human = Client.objects.get(user_id=request.user.id)
        
        end_of_the_block = timedelta(days=human.how_many_days) + human.date_of_purchase
        days_left = (end_of_the_block - date.today()).days
        
        print(days_left)
        
        context = {
            'date_of_purchase': human.date_of_purchase,
            'days_left': days_left,
            }

    except:
        context = {}

    return render(request, 'home.html', context)

def scan(request):
    

    try:
        clients = Client.objects.all()
    
        for client in clients:
            client.checkDate()
    except:
        pass

    try:
        ID = request.GET.get('var')
        print(f'ID {ID}')
        client = Client.objects.get(user_id=ID)
        print(f'client name {client.user.first_name}')
        print(f'client lastname {client.user.last_name}')
    except:
        client = None
        ID = None

    return render(request, 'base/scan.html', {'id': ID, 'client': client})

def qr_code(request):
    return render(request, 'base/qr_code.html', {'id': request.user.id})