from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Brand, SkinType, SkinConcern, Skincare

from .forms import ProductForm


def all_products(request):
    """ A View To Render All Products  """

    # Retrives Skincare Object
    skincare = Skincare.objects.all()
    query = None
    usage = None
    product_type = None

    if request.GET:
        if 'usage' in request.GET:
            usages = request.GET['usage'].split(',')
            skincare = skincare.filter(usage__in=usages)

        if 'product_type' in request.GET:
            product_types = request.GET['product_type'].split(',')
            skincare = skincare.filter(product_type__name__in=product_types)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Invalid serach criterira!"
                    )
                return redirect(reverse('all_products'))

            queries = Q(name__contains=query) | Q(
                description__icontains=query) | Q(
                about__icontains=query)
            skincare = skincare.filter(queries)

    context = {
        'skincare': skincare,
        'serach_term': query,
    }

    return render(request, 'products/all_products.html', context)


def product_details(request, product_id):
    """ A View To Render A Single Product & Its Details """

    # Retrives A Single Skincare Object By Using Its ID
    product = get_object_or_404(Skincare, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


def all_brands(request):

    """ A view to render all brands and organize them alphabetically """

    # Retrieves Brand Object
    brands = Brand.objects.all()

    # Renders Brand Starting Letters & Ommits Duplicate Values
    brand_letters_query = brands.values_list(
        'character_identifier', flat=True
        )
    brand_letters = []
    for letters in brand_letters_query:
        if letters not in brand_letters:
            brand_letters.append(letters)

    # Renders & Orders Brands By Friendly Name
    brand_letter_startswith = brands.order_by('friendly_name').values

    context = {
        'brands': brands,
        'brand_letters': brand_letters,
        'brand_letter_startswith': brand_letter_startswith,
    }

    return render(request, 'brands/brands.html', context)


def full_brands(request, slug):

    """ A view to use the slug field to take user to the correct brand and
    relevant information """

    # Retrives Brand object
    queryset = Brand.objects.all()

    # Retrives the slug from the Brand object then applies it to each brand
    full_brand = get_object_or_404(queryset, slug=slug)

    context = {
        'full_brand': full_brand,
    }

    return render(request, 'brands/full_brands.html', context)


def skin_type(request):
    """ A View To Render & Filer For Skin Types  """

    # Retrives Skin Type Object
    skin_type = SkinType.objects.all()

    context = {
        'skin_type': skin_type,
    }

    return render(request, 'skin_type/skin_type.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Skincare, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
            Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Skincare, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('all_products'))
