from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import messages
from datetime import datetime
from .forms import *
from .models import *


def index(request):
    flowers = Flowers.objects.filter(published=True)

    context = {
        'flowers': flowers,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def types(request, type_id):
    types = get_object_or_404(Types, id=type_id)
    flowers = Flowers.objects.filter(type_id=type_id, published=True)

    context = {
        'types': [types],
        'flowers': flowers,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)


def flower(request, flower_id):
    flower = get_object_or_404(Flowers, id=flower_id, published=True)

    context = {
        'flower': flower
    }

    return render(request, 'detail.html', context)


def addType(request: WSGIRequest):
    if request.method == 'POST':
        form = TypeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            if Types.objects.filter(name=form.cleaned_data['name']).exists():
                messages.success(request, "Ma'lumot saqlanmadi. Bunday tur allaqachon mavjud!")
            else:
                Types.objects.create(**form.cleaned_data)
                messages.success(request, "Ma'lumot muvaffaqiyatli saqlandi!")
            return redirect('addType')
    context = {
        'forms': TypeForm()
    }
    return render(request, 'addType.html', context)


def addFlower(request: WSGIRequest):
    if request.method == 'POST':
        form = FlowerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            Flowers.objects.create(**form.cleaned_data)
            messages.success(request, "Ma'lumotlar muvaffaqiyatli saqlandi!")
            return redirect('addFlower')
    context = {
        'forms': FlowerForm()
    }

    return render(request, 'addFlower.html', context)
