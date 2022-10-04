from django.shortcuts import render
from .models import Brand


def all_brands(request):
    """ A view to render all products aswell as sorting and seraching """

    # Renders Brands Model
    brands = Brand.objects.all()
    # Filters brand starting letter and only renders single ones
    brand_letters_query = Brand.objects.values_list(
        'character_identifier', flat=True
        )
    brand_letters = []
    for letters in brand_letters_query:
        if letters not in brand_letters:
            brand_letters.append(letters)

    # Allow you to filter by brands use after letters are established
    # brand = brands.filter(character_identifier="a")

    context = {
        'brands': brands,
        'brand_letters': brand_letters,
        # 'brand': brand,
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
