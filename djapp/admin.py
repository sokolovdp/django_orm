from django.contrib import admin

from . import models


# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    fields = ['id', 'name', 'price', 'description', 'image']  # in this order fields will appear
    search_fields = ['name', 'price']  # create search box
    list_filter = ['price']  # add filter column
    list_display = ['id', 'name', 'price', 'description', 'image']  # add fields to the list view
    list_editable = ['name', 'price', 'description', 'image']  # make fields editable from the view


admin.site.register(models.Item, ItemAdmin)
