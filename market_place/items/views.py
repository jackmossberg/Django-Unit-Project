from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def detail_view(request,pk):
    #will return what item matches the id number
    #  or give not found error if none
    item = get_object_or_404(Item,pk=pk)
    similaritems = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html',{'item':item,'related_items':similaritems})