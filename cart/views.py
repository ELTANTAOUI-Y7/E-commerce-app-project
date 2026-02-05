from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product


def cart_view(request):
    """View for displaying the shopping cart."""
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    
    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            item_total = float(product.price) * quantity
            total += item_total
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total,
            })
        except Product.DoesNotExist:
            pass
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, product_id):
    """Add a product to the shopping cart."""
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    
    request.session['cart'] = cart
    return redirect('cart')


def remove_from_cart(request, product_id):
    """Remove a product from the shopping cart."""
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        del cart[str(product_id)]
    
    request.session['cart'] = cart
    return redirect('cart')


def checkout(request):
    """Checkout view."""
    cart = request.session.get('cart', {})
    
    if not cart:
        return redirect('cart')
    
    # Placeholder checkout logic
    context = {
        'cart_items_count': sum(cart.values()),
    }
    return render(request, 'cart/checkout.html', context)
