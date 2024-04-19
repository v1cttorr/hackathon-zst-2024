from typing import Any
from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.views.generic.base import TemplateView
import stripe # type: ignore
from accounts.models import Client
import uuid
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm # type: ignore

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

days = 0
price = 0

class BuyPageView(TemplateView):
    template_name = 'payment/buy.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHED_KEY

        global days
        global price

        days = self.request.GET.get('days')
        print(days)
        price = int(days) * 9
        print(price)

        #PAYPAL
        host = self.request.get_host()

        paypal_checkout = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': price,
            'item_name': 'Lunch Block',
            'invoice': uuid.uuid4(),
            'currency_code': 'PLN',
            'notify-url': f'https://{host}{reverse('paypal-ipn')}',
            'return-url': f'https://{host}{reverse('payment-success')}',
            'cancel-url': f'https://{host}{reverse('payment-failed')}',
        }

        paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

        context['paypal'] = paypal_payment
        context['product'] = 'Lunch Block'



        return context
    
def charge(request):
    global price
    global days
    print(price)
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=price*100,
            currency='pln',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )

    try:
        client = Client.objects.get(user=request.user)
        client.how_many_days+=int(days)
        client.save()
    except:
        client = Client.objects.create(user=request.user, how_many_days=days)

    return render(request, 'payment/charge.html')




def PaymentSuccess(request):
    return render(request, 'payment/payment-success.html')

def PaymentFailed(request):
    return render(request, 'payment/payment-failed.html')
