from items.models import Category

def global_categories(request):
    categories = Category.objects.all()
    selected_category = None

    category_id = request.GET.get('category')
    if category_id and category_id.isdigit():
        try:
            selected_category = categories.get(id=category_id)
        except Category.DoesNotExist:
            pass

    return {
        'categories': categories,
        'selected_category': selected_category,
    }