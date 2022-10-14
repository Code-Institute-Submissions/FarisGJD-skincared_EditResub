from django.shortcuts import render
from .models import Brand


def all_brands(request):
    """ A view to render all products aswell as sorting and seraching """

    # Retrieves brand object
    brands = Brand.objects.all()

    # Renders brand starting letters and ommits duplicate values
    brand_letters_query = Brand.objects.values_list(
        'character_identifier', flat=True
        )
    brand_letters = []
    for letters in brand_letters_query:
        if letters not in brand_letters:
            brand_letters.append(letters)

    # Filters and allocates brands by starting character
    brand_startswith = brands.filter(
        friendly_name='b')

    context = {
        'brands': brands,
        'brand_letters': brand_letters,
        'brand_startswith': brand_startswith,
    }

    return render(request, 'brands/brands.html', context)

# from .models import Skincare


# def all_products(request):
#     """ A view to render all products aswell as sorting and seraching """

#     skincare = Skincare.objects.all()

#     context = {
#         'skincare': skincare,
#     }

#     return render(request, 'skincare/skincare.html', context)
