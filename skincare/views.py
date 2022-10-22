from django.shortcuts import render
from .models import Brand


def all_brands(request):
    """ A view to render all products aswell as sorting and seraching """

    # Retrieves brand object
    brands = Brand.objects.all()

    # Renders brand starting letters and ommits duplicate values
    brand_letters_query = brands.values_list(
        'character_identifier', flat=True
        )
    brand_letters = []
    for letters in brand_letters_query:
        if letters not in brand_letters:
            brand_letters.append(letters)

    # Filters and allocates brands by starting character
    brand_letters_startswith = tuple(brand_letters)
    brand_startswith = brands.filter(
        friendly_name__istartswith={brand_letters_startswith}
        ).values()

    context = {
        'brands': brands,
        'brand_letters': brand_letters,
        'brand_startswith': brand_startswith,
    }

    return render(request, 'brands/brands.html', context)
