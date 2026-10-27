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