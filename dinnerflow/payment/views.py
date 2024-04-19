from typing import Any
from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.views.generic.base import TemplateView
import stripe # type: ignore

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

        return context
    
def charge(request):
    global price
    print(price)
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=price*100,
            currency='pln',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )
    return HttpResponse('<h1>Succesfully paid</h1>')