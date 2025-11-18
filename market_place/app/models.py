from django.db import models
<<<<<<< HEAD
=======
from django.contrib.auth.models import User

class Category(models.Model):
    name= models.CharField(max_length=225)
 
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
>>>>>>> b490e17028a96bdbc0eabd20d302d298d5ead8fd
