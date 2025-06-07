from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request,'food/index.html',context)

def item(request):
    return HttpResponse('<h1>This is item view</h1>')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context ={
        'item':item,
    }

    return render(request,'food/detail.html',context)

def create_item(request):
    forms = ItemForm(request.POST or None)

    if forms.is_valid():
        forms.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'forms':forms})
    