from django.contrib import admin
from .models import Brand, ProductType, SkinType


class BrandAdmin(admin.ModelAdmin):
    """ Customise Brand Admin Panel """

    prepopulated_fields = {'slug': ('friendly_name',)}
    list_display = (
        'friendly_name',
        'name',
    )
    ordering = ('friendly_name',)


class ProductTypeAdmin(admin.ModelAdmin):
    """ Customise Product Type Admin Panel """

    list_display = (
        'friendly_name',
        'name'
    )
    ordering = ('friendly_name',)


class SkinTypeAdmin(admin.ModelAdmin):
    """ Customise Skin Type Admin """

    list_display = (
        'skin_type_1',
        'skin_type_2',
        'skin_type_3',
        'skin_type_4',
        'skin_type_5'
    )


admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(SkinType, SkinTypeAdmin)
