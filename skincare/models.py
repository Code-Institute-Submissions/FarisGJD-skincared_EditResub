from django.db import models
from django.utils.text import slugify


class Brand(models.Model):
    """ Brands Model """

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(
        max_length=200, null=True, blank=True)
    character_identifier = models.CharField(
        max_length=10, null=True, blank=True
    )
    about = models.TextField()
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True)

    class Meta:
        """ Orders Brands Alphabetically """

        ordering = ['friendly_name']

    def __str__(self):
        return self.name

    def brand_friendly_name(self):
        """ Returns Brands User Friendly Name """

        return self.friendly_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.friendly_name)
        super(Brand, self).save(*args, **kwargs)


class ProductType(models.Model):
    """ Product Type Model """

    class Meta:
        verbose_name = 'Product Type'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        """ Orders Product Types Alphabetically """

        ordering = ['name']

    def __str__(self):
        return self.name

    def product_type_friendly_name(self):
        """ Returns Product Type User Friendly Name """

        return self.friendly_name


class SkinType(models.Model):
    """ Skin Type Model """

    class Meta:
        verbose_name = 'Skin Type'

    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
