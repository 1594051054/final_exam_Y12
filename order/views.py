from django.shortcuts import render
from . models import Order
def home_page(request):

    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        address = request.POST.get("address")
        order_obj = Order.objects.create(
            order = food_name,
            address = address,
        )
        return render(request, 'order/home_page.html', {'foods': order_obj})

    return render(request, 'order/home_page.html') 