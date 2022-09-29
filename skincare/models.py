from django.db import models


class Brand(models.Model):
    """ Brands Model """

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    first_letter = models.CharField(max_length=5, null=True, blank=True)
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
