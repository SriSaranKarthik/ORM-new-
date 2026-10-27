# Ex: 2 Django ORM Web Application
# Date: 27.10.2026
## Name: K.SriSaran Karthik
## Reg No: 212224230275
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).
# ENTITY RELATIONSHIP DIAGRAM
# DESIGN STEPS

**## STEP 1:**
Clone the Django project from GitHub.

**## STEP 2:**
Create a new Django app named `ormapp` in the Django project.

**## STEP 3:**
Write the code in `models.py` to define the Zomato order details and configure `admin.py` to display and manage the orders in the Django Admin interface.

**## STEP 4:**
Execute the Django Admin interface and create details for 10 Zomato food delivery orders.

# PROGRAM

## 1.ADMIN.PY
```
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

```

## 2.MODELS.PY

```
from django.db import models


class ZomatoOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    restaurant_name = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.order_id} - {self.customer_name}"
        
```

# OUTPUT

![alt text](<Screenshot 2026-10-27 144002.png>)
![alt text](<Screenshot 2026-10-27 144017.png>)
![alt text](<Screenshot 2026-10-27 144024.png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
