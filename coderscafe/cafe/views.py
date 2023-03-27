from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassTestMixin, LoginRequiredMixin
from django.urls.timezone import datetime
from customer.models import OrderModel


class Dashboard(LoginRequiredMixin, UserPassTestMixin, View):
    def get(self, request, *args, **kwargs):
        # get the current dare
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

        # loop through the orders and add the price value
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

        # pass total number of rders and total revenue into template
        context = {
            'orders': orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders),
        }
        return render(request, 'cafe/dashboard.html', context)

        def test_func(self):
            return self.request.user.groups.filter(name='staff').exists()
