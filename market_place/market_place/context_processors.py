# items/context_processors.py

from items.models import Category
from django.db.models import Count, Q 

def global_categories(request):
    categories_with_items = Category.objects.annotate(
        num_items=Count(
            'items',
            filter=Q(items__is_sold=False)
        )
    ).filter(num_items__gt=0)
    
    selected_category = None

    category_id = request.GET.get('category')
    
    if category_id and category_id.isdigit():
        try:
            selected_category = Category.objects.get(pk=category_id) 
        except Category.DoesNotExist:
            pass
            
    return {
        'global_categories': categories_with_items, 
        'global_selected_category': selected_category, 
    }