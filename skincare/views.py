from django.shortcuts import render
from .models import Brand
# from .models import Skincare


# def all_products(request):
#     """ A view to render all products aswell as sorting and seraching """

#     skincare = Skincare.objects.all()

#     context = {
#         'skincare': skincare,
#     }

#     return render(request, 'skincare/skincare.html', context)


def all_brands(request):
    """ A view to render all products aswell as sorting and seraching """

    brands = Brand.objects.all()

    context = {
        'brands': brands,
    }

    return render(request, 'brands/brands.html', context)
