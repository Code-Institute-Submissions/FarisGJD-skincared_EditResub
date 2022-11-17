from django.shortcuts import render, get_object_or_404
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

    # Filters and renders brands by starting character

    brand_a = brands.filter(
        friendly_name__istartswith="a")

    brand_b = brands.filter(
        friendly_name__istartswith="b")

    brand_c = brands.filter(
        friendly_name__istartswith="c")

    brand_d = brands.filter(
        friendly_name__istartswith="d")

    brand_e = brands.filter(
        friendly_name__istartswith="e")

    brand_f = brands.filter(
        friendly_name__istartswith="f")

    brand_g = brands.filter(
        friendly_name__istartswith="g")

    brand_h = brands.filter(
        friendly_name__istartswith="h")

    brand_i = brands.filter(
        friendly_name__istartswith="i")

    brand_j = brands.filter(
        friendly_name__istartswith="j")

    brand_k = brands.filter(
        friendly_name__istartswith="k")

    brand_l = brands.filter(
        friendly_name__istartswith="l")

    brand_m = brands.filter(
        friendly_name__istartswith="m")

    brand_n = brands.filter(
        friendly_name__istartswith="n")

    brand_o = brands.filter(
        friendly_name__istartswith="o")

    brand_p = brands.filter(
        friendly_name__istartswith="p")

    brand_q = brands.filter(
        friendly_name__istartswith="q")

    brand_r = brands.filter(
        friendly_name__istartswith="r")

    brand_s = brands.filter(
        friendly_name__istartswith="s")

    brand_t = brands.filter(
        friendly_name__istartswith="t")

    brand_u = brands.filter(
        friendly_name__istartswith="u")

    brand_v = brands.filter(
        friendly_name__istartswith="v")

    brand_w = brands.filter(
        friendly_name__istartswith="w")

    brand_x = brands.filter(
        friendly_name__istartswith="x")

    brand_y = brands.filter(
        friendly_name__istartswith="y")

    brand_z = brands.filter(
        friendly_name__istartswith="z")

    context = {
        'brand_letters': brand_letters,
        "brand_a": brand_a,
        "brand_b": brand_b,
        "brand_c": brand_c,
        "brand_d": brand_d,
        "brand_e": brand_e,
        "brand_f": brand_f,
        "brand_g": brand_g,
        "brand_h": brand_h,
        "brand_i": brand_i,
        "brand_j": brand_j,
        "brand_k": brand_k,
        "brand_l": brand_l,
        "brand_m": brand_m,
        "brand_n": brand_n,
        "brand_o": brand_o,
        "brand_p": brand_p,
        "brand_q": brand_q,
        "brand_r": brand_r,
        "brand_s": brand_s,
        "brand_t": brand_t,
        "brand_u": brand_u,
        "brand_v": brand_v,
        "brand_w": brand_w,
        "brand_x": brand_x,
        "brand_y": brand_y,
        "brand_z": brand_z,
    }

    return render(request, 'brands/brands.html', context)


def full_brands(request, slug):

    # Retrives Brand object
    queryset = Brand.objects.all()

    # Retrives the slug from the Brand object then applies it to each brand
    full_brand = get_object_or_404(queryset, slug=slug)

    context = {
        'full_brand': full_brand,
    }

    return render(request, 'brands/full_brands.html', context)
