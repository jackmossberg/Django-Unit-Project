from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Category
from .forms import NewItemForm, EditItemForm
# Create your views here.

def detail(request,pk):
    #will return what item matches the id number
    #  or give not found error if none
    item = get_object_or_404(Item,pk=pk)
    similaritems = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'items/detail.html',{'item':item,'related_items':similaritems})

@login_required
def new(request):
    if request.method == "POST": 
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save() 
            return redirect('item:detail',pk=item.id)
    else:
        form = NewItemForm()
    return render(request,'items/form.html', {
        'form':form
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:createditems')


@login_required
def edit(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method == "POST": 
        form = EditItemForm(request.POST, request.FILES, instance = item)
        if form.is_valid():
            form.save()
            return redirect('item:detail',pk=item.id)
    else:
        form = EditItemForm(instance=item)
    return render(request,'items/form.html', {
        'form':form,
        'title':'Edit Item'
    })

def browsing(request):
    items_queryset = Item.objects.filter(is_sold=False)
    cat_id = request.GET.get('category')  

    view_selected_category = None
    all_categories = Category.objects.all()

    if cat_id:
        items_queryset = items_queryset.filter(category_id=cat_id)
        view_selected_category = Category.objects.filter(id=cat_id).first()

    context = {
        'filtered_items': items_queryset,
        'view_selected_category': view_selected_category,
        'all_categories': all_categories,

        'global_categories': all_categories,
        'global_selected_category': view_selected_category,
    }

    return render(request, 'app/home.html', context)