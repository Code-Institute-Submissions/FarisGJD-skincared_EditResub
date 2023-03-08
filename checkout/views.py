from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your Bag Is Cuerrently Empty")
        return redirect(reverse('products'))
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LO7TFFYCwMBWuXdta0RKGGms7eAuns2U5d3arenKqlBZsRvk4CW9UubJec1anLHRlNGOLMWjetZQ7jrL4TkCEPh00yV5Sl379',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
