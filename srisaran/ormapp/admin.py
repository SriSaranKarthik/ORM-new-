from django.contrib import admin
from .models import ZomatoOrder


class ZomatoOrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'customer_name',
        'restaurant_name',
        'food_item',
        'quantity',
        'price',
        'delivery_address',
        'order_date',
    )

    search_fields = (
        'customer_name',
        'restaurant_name',
        'food_item',
    )

    list_filter = ('order_date',)


admin.site.register(ZomatoOrder, ZomatoOrderAdmin)