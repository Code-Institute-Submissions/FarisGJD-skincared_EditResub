from django.db import models
from django.utils.text import slugify


class Brand(models.Model):
    """ Brands Model """

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(
        max_length=200, null=True, blank=True, unique=True
        )
    about = models.TextField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        '''Orders Brands Alphabetically '''
        ordering = ['friendly_name']

    def __str__(self):
        return self.name

    def brand_friendly_name(self):
        """ Returns Brands User Friendly Name """
        return self.friendly_name


class BrandCategory(models.Model):
    """ Categorises Brands By Name """
    identifier = models.CharField(max_length=10, primary_key=True)
    brand_name = models.ForeignKey(
        Brand, to_field='friendly_name', null=True, blank=True, on_delete=models.SET_NULL
        )
    slug = models.SlugField(max_length=200, null=True, unique=True)

    class Meta:
        """ Order By Brand Name """
        ordering = ["brand_name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.brand_name)
        super(BrandCategory(), self).save(*args, **kwargs)


class ProductType(models.Model):
    """ Product Type Model """

    class Meta:
        verbose_name_plural = 'Product Type'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        '''Orders Product Types Alphabetically '''
        ordering = ['name']

    def __str__(self):
        return self.name

    def product_type_friendly_name(self):
        """ Returns Product Type User Friendly Name """

        return self.friendly_name
