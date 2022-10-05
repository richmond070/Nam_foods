from dataclasses import field
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
)

from .models import Product
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "base/home.html")


class ProductListView(ListView):
    model = Product
    context_object_name = "product_list"
    queryset: Product.objects.all().order_by(
        "product_name",
        'product_price',
        'picture',
        "-date_added"
    )


class ProductCreateView(CreateView):
    model = Product
    fields = ["product_name", "quantity", "product_price", "picture"]
    success_url: reverse_lazy("product-create")


class ProductUpdateView(ProductCreateView, UpdateView):
    success_url: reverse_lazy("product-create")
