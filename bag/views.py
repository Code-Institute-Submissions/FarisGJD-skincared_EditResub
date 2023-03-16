from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from skincare.models import Skincare


def view_bag(request):
    """ A View That Renders The Users Shopping Bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ A View That Adds A Quantity of a specific Product To The Users Bag """

    product = get_object_or_404(Skincare, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request,
            f'Successfully Updated {product.name}'
            f'Quantity To X{bag[item_id]}'
            )
    else:
        bag[item_id] = quantity
        messages.success(
            request, f'Successfully Added {product.name} To Your Bag'
            )

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ A View That Adjusts A Specific Product To A Specified Amount """

    product = get_object_or_404(Skincare, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Successfully Updated {product.name}'
            f'Quantity To X{bag[item_id]}'
            )
    else:
        bag.pop(item_id)
        messages.success(
            request, f'Successfully Removed {product.name} From Your Bag'
            )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ A View That Removes A Specific Product """
    try:
        product = get_object_or_404(Skincare, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(
            request, f'Successfully Removed {product.name} From Your Bag'
            )
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error In Removing Item: {e}')
        return HttpResponse(status=500)
