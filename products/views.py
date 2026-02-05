from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category


def home(request):
    """Homepage view with featured products and categories."""
    featured_products = Product.objects.all()[:6]
    categories = Category.objects.all()
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
    }
    return render(request, 'products/home.html', context)


def category_products(request, slug):
    """View for displaying products in a specific category."""
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    all_categories = Category.objects.all()
    
    context = {
        'category': category,
        'products': products,
        'categories': all_categories,
    }
    return render(request, 'products/category.html', context)


def product_detail(request, pk):
    """View for displaying a specific product."""
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)


class ProductListView(ListView):
    """Class-based view for listing all products."""
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12
