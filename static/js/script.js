// E-Commerce Store - Custom JavaScript

// Initialize tooltips and popovers if using Bootstrap's JS
document.addEventListener('DOMContentLoaded', function() {
    console.log('E-Commerce Store loaded successfully');

    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Add to cart button click handler
    const addToCartButtons = document.querySelectorAll('.btn-add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productName = this.getAttribute('data-product-name') || 'Product';
            showNotification(`${productName} added to cart!`);
        });
    });

    // Search functionality
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('keyup', function(e) {
            if (e.key === 'Enter') {
                const query = this.value.trim();
                if (query) {
                    // Perform search - will be implemented later
                    console.log('Searching for:', query);
                }
            }
        });
    }
});

// Show notification function
function showNotification(message) {
    // Create a simple alert or use a toast notification
    const alertDiv = document.createElement('div');
    alertDiv.setAttribute('role', 'alert');
    alertDiv.className = 'alert alert-success alert-dismissible fade show position-fixed';
    alertDiv.style.top = '20px';
    alertDiv.style.right = '20px';
    alertDiv.style.zIndex = '9999';
    alertDiv.style.minWidth = '300px';
    
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    document.body.appendChild(alertDiv);
    
    // Auto-remove after 3 seconds
    setTimeout(function() {
        alertDiv.remove();
    }, 3000);
}

// Cart functions (placeholder)
function addToCart(productId) {
    console.log('Adding product', productId, 'to cart');
    // Will be implemented with actual cart logic
}

function removeFromCart(productId) {
    console.log('Removing product', productId, 'from cart');
    // Will be implemented with actual cart logic
}

// Format currency
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}
