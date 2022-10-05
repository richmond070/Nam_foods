from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product", views.ProductListView.as_view(), name='product-list'),
    path("new", views.ProductCreateView.as_view(), name='product-create'),
    path("edit/<int:pk>", views.ProductUpdateView.as_view(), name="product-update"),

]
