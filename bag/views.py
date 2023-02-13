from django.shortcuts import render


def view_bag(request):
    """ A View That Renders The Users Shoppinh Bag """
    return render(request, 'bag/bag.html')
