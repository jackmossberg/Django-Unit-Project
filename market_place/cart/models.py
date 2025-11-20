from django.db import models
from django.contrib.auth.models import User
from items.models import Item
# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def total(self):
        return sum(item.subtotal() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.item.price * self.quantity