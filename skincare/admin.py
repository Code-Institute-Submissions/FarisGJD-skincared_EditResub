from django.contrib import admin
from .models import Brand


class BrandAdmin(admin.ModelAdmin):
    """ Customise Brand Admin Panel """

    list_display = (
        'friendly_name',
        'name'
    )
    ordering = ('friendly_name',)


admin.site.register(Brand, BrandAdmin)
