from django.db import models


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
