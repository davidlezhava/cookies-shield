// Get references to elements
const buyNowButton = document.getElementById('buyNowButton');
const checkoutForm = document.getElementById('checkoutForm');
const closeCheckout = document.getElementById('closeCheckout');

// Show the checkout form when "Buy Now" is clicked
buyNowButton.addEventListener('click', () => {
    checkoutForm.classList.remove('hidden');
});

// Hide the checkout form when the close button is clicked
closeCheckout.addEventListener('click', () => {
    checkoutForm.classList.add('hidden');
});
